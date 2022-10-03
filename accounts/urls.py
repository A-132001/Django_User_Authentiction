from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("sighup",views.sighup,name="sighup"),
    path("profile",views.profile,name="profile"),
    path("profile/edit",views.profile_edit,name="profile_edit"),
]