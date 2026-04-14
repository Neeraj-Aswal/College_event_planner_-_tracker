from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from organizer.models import Event
from .models import Participation



# ----------------------
# STUDENT DASHBOARD
# ----------------------
def dashboard(request):
    return render(request, 'student/dashboard.html')


# ----------------------
# ALL EVENTS LIST
# ----------------------
def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'student/event_list.html', {'events': events})


# ----------------------
# EVENT DETAILS
# ----------------------
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'student/event_detail.html', {'event': event})

@login_required
def join_event(request, id):
    event = get_object_or_404(Event, id=id)

    # prevent duplicate join
    if Participation.objects.filter(student=request.user, event=event).exists():
        messages.warning(request, "You already joined this event")
        return redirect('event_detail', id=event.id)

    Participation.objects.create(
        student=request.user,
        event=event
    )

    messages.success(request, "Successfully joined the event!")
    return redirect('event_detail', id=event.id)

@login_required
def my_events(request):
    participations = Participation.objects.filter(student=request.user)
    return render(request, 'student/my_events.html', {'participations': participations})