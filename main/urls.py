from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('blog/<int:pk>', posting),
    path('blog/new_post', new_post),
    path('blog/<int:pk>/remove', remove_post),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
