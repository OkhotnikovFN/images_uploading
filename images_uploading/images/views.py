import os

from django.views import generic
from django.views.generic import DetailView, ListView, TemplateView
from PIL import Image

from images import models, forms
from images_uploading.settings import MEDIA_URL, MEDIA_ROOT


class MainView(TemplateView):
    template_name = 'images/index.html'


class ImageListView(ListView):
    model = models.Image
    context_object_name = 'images'


class ImageDetailView(DetailView):
    model = models.Image
    context_object_name = 'image'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        form = forms.ImageSizeForm(request.GET)
        context['form'] = form
        img_url = context['image'].image.url

        if form.is_valid():
            image = Image.open(context['image'].image.path)
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            width = width if width else image.size[0]
            height = height if height else image.size[1]

            image_resize = image
            image_resize.thumbnail((width, height))

            img_name = context['image'].image.name.split('/')[-1]
            tmp_dir = os.path.join(*context['image'].image.name.split('/')[:-1], 'tmp')
            img_dir = os.path.join(MEDIA_ROOT, tmp_dir)

            os.makedirs(img_dir, exist_ok=True)

            resize_image_url = os.path.join(MEDIA_URL, tmp_dir, img_name)
            image_resize.save(os.path.join(img_dir, img_name))
            img_url = resize_image_url

        context['img_url'] = img_url

        return self.render_to_response(context)


class ImageCreateView(generic.CreateView):
    template_name = 'images/image_create.html'
    form_class = forms.ImageForm
