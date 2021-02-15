import io

import requests
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

from images import models


class ImageForm(forms.ModelForm):

    img_url = forms.URLField(label='Ссылка', required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = models.Image
        fields = ['image']

    def clean(self):
        cleaned_data = super(ImageForm, self).clean()
        img_url = cleaned_data.get('img_url')
        image = cleaned_data.get('image')

        if img_url and image:
            raise ValidationError('Нельзя указать ссылку из интренета и файл из компьютера одновременно')

        if not img_url and not image:
            raise ValidationError('Для загрузки картинки необходимо указать одно из значений')

        if img_url and not image:
            response = requests.get(img_url)
            filename = img_url.split('/')[-1]
            data = InMemoryUploadedFile(
                io.BytesIO(response.content),
                'image',
                filename,
                response.headers.get('Content-Type'),
                response.headers.get('Content-Length'),
                None
            )
            self.cleaned_data['image'] = self.fields['image'].clean(data)


class ImageSizeForm(forms.Form):
    width = forms.IntegerField(label='Ширина', required=False)
    height = forms.IntegerField(label='Высота', required=False)