from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
    path("lobby/", views.lobby, name="lobby"),
    path("room/<str:room_name>/", views.room),
    path("get_token/", views.getToken),
    path("create_member/", views.createMember),
    path("get_member/", views.getMember),
    path("delete_member/", views.deleteMember),
]
