from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView

from apps.rooms.models import Room, Image, Booking
from .form import RoomForm


# class RoomListView(CreateView):
#     form_class = RoomForm
#     model = Booking
#
#     def get_context_data(self, **kwargs):
#         cnt = super().get_context_data(**kwargs)
#         cnt['object_list'] = Room.objects.all()
#         return cnt
#
#     def get(self, request, *args, **kwargs):
#         check_in = request.GET.get('checkInDate')
#         check_out = request.GET.get('checkOutDate')
        # adults = request.GET.get('adults')
        # children = request.GET.get('children')
        # print('dssss..............')
        # if check_in or check_out:
        #     object_list = Room.objects.filter(booking__check_in__gte=check_in, booking__check_out__lte=check_out)
        #     print('ds..............')
            # cnt = super().get_context_data(**kwargs)
            # cnt['object_list'] = object_list
            # return cnt

    # template_name = 'rooms/room.html'

def room_list(request):
    # form = RoomForm()
    check_in = request.GET.get('checkInDate')
    check_out = request.GET.get('checkOutDate')
    rooms = Room.objects.all()
    # if check_in:
    #     rooms = rooms.filter(rooms_booking__check_in__gte=check_in)
    #     print('............................................')
    cnt = {
        'object_list': rooms,
        # 'form': form
    }
    return render(request, 'rooms/room.html', cnt)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.room = room
            form.save()
            return redirect('.')
    ctx = {
        'room': room,
        'form': form
    }
    return render(request, 'rooms/single-room.html', ctx)
