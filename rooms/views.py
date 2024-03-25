from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import RoomType, Room


def room_list(request: HttpRequest) -> HttpResponse:
    rooms = Room.objects.all().filter(is_available=True)
    return render(request, "rooms/room_list.html", {"rooms": rooms})


def room_detail(request: HttpRequest, room_id: int) -> HttpResponse:
    room = Room.objects.get(id=room_id)
    return render(request, "rooms/room_detail.html", {"room": room})
