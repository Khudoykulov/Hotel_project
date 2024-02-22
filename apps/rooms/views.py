from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from apps.rooms.models import Room, Image, Booking
from .form import RoomForm


def room_list(request):
    check_in = request.GET.get('checkin-date')
    check_out = request.GET.get('checkout-date')
    max_adults = request.GET.get('adults')
    max_children = request.GET.get('children')
    price = request.GET.get('price')
    rooms = Room.objects.all()
    if check_in and check_out:
        rooms = rooms.filter(~Q(rooms_booking__check_in__lte=check_out) | ~Q(rooms_booking__check_out__gte=check_in))
        if int(max_adults) != 0 or int(max_children) != 0:
            rooms_max_person = rooms.filter(Q(max_person=int(max_adults)+int(max_children)))
            rooms = rooms.intersection(rooms_max_person)
        # if int(price) != 0:

    cnt = {
        'object_list': rooms,
    }
    return render(request, 'rooms/room.html', cnt)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST,)
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
