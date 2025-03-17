from django.urls import path
from .views import *

urlpatterns = [
    path("", profile_view, name="profile"),
    path("edit/", profile_edit_view, name="profile_edit"),
    path("onboarding/", profile_edit_view, name="profile_onboarding"),
    path("settings/", profile_settings_view, name="profile_settings"),
    path("emailchange/", profile_emailchange, name="profile_emailchange"),
]
