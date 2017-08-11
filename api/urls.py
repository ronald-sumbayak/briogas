from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = [
    url (r'^token', obtain_auth_token),
    url (r'^data/retrieve', views.retrieve_data),
    url (r'^data/update', views.update_data),
    url (r'^toggle-katup', views.toggle_katup)
]