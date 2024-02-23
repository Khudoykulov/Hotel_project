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
    room_number = request.GET.get('room_number')
    rooms = Room.objects.all()
    if check_in and check_out:
        rooms = rooms.filter(~Q(rooms_booking__check_in__lte=check_out) | ~Q(rooms_booking__check_out__gte=check_in))
        if room_number:
            rooms = rooms.filter(Q(room_number1=room_number))
        if int(max_adults) != 0 or int(max_children) != 0 or room_number:
            rooms_max_person = rooms.filter(Q(max_person=int(max_adults)+int(max_children)))
            rooms = rooms.intersection(rooms_max_person)
    cnt = {
        'object_list': rooms,
    }
    return render(request, 'rooms/room.html', cnt)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    form = RoomForm()

    if request.method == 'POST':
        check_in = '20'+'-'.join(request.POST['check_in'].split('/')[::-1])
        check_out = '20' + '-'.join(request.POST['check_out'].split('/')[::-1])
        data = {
            'check_in': check_in,
            'check_out': check_out
        }
        form = RoomForm(data)
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
