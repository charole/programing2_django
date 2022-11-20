from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', index),
    path('login_page/', login_page),
    path('signup/', signup),
    path('blog/', blog),
    path('blog/<int:pk>', posting),
    path('blog/new_post', new_post),
    path('blog/<int:pk>/remove', remove_post),

    path('accounts/', account_list),
    path('accounts/<int:pk>', account),
    path('login/', login),

    path('examples/', example_list),
    path('example/<int:pk>', example)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
