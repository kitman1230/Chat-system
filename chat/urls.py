from django.urls import path
from .views import *

urlpatterns = [
    path("", chat_view, name="home"),
    path("<username>", get_or_create_chatroom, name="start_chat"),
    path("room/<chatroom_name>", chat_view, name="chatroom"),
]
