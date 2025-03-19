from django.urls import path
from .views import *

urlpatterns = [
    path("", chat_view, name="home"),
    path("<username>", get_or_create_chatroom, name="start_chat"),
    path("room/<chatroom_name>", chat_view, name="chatroom"),
    path("room/new_groupchat/", create_groupchat, name="new_groupchat"),
    path("room/edit/<chatroom_name>", chatroom_edit_view, name="edit_chatroom"),
    path("room/delete/<chatroom_name>", chatroom_delete_view, name="delete_chatroom"),
    path("room/leave/<chatroom_name>", chatroom_leave_view, name="leave_chatroom"),
]
