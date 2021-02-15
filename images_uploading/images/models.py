from django.db import models
from django.urls import reverse


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='images/images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def get_absolute_url(self):
        return reverse('images:image_detail', args=[str(self.id)])

    def __str__(self):
        return self.image.name.split('/')[-1]
