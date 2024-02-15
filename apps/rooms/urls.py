from django.urls import path
from .views import RoomListView, room_detail

app_name = 'rooms'

urlpatterns = [
    path('rooms_list/', RoomListView.as_view(), name='rooms_list'),
    path('rooms/<slug:slug>/', room_detail, name='room_detail'),
]

