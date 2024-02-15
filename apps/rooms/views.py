from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from apps.rooms.models import Room, Image


class RoomListView(ListView):
    queryset = Room.objects.all()

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        return cnt
    template_name = 'rooms/room.html'


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    ctx = {
        'room': room
    }
    return render(request, 'rooms/single-room.html', ctx)
