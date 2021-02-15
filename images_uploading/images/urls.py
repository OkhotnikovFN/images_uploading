from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from images import views


app_name = 'images'

urlpatterns = [
    path('', views.MainView.as_view(), name="index"),
    path('images/', views.ImageListView.as_view(), name='image_list'),
    path('images/<int:pk>/', views.ImageDetailView.as_view(), name='image_detail'),
    path('images/create/', views.ImageCreateView.as_view(), name='image_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
