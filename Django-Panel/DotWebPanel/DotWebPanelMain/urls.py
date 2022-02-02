from django.urls import include, path
from .views import index_page, user_signup, user_login, image_page

urlpatterns = [
    path('', index_page),
    path('image/', image_page),
    path('login/', user_login),
    path('register/', user_signup),
]
