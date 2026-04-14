from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from organizer.models import Event


# -------------------
# DASHBOARD
# -------------------
@login_required
def dashboard(request):
    return render(request, 'organizer/dashboard.html')


# -------------------
# CREATE EVENT
# -------------------
@login_required
def create_event(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        location = request.POST['location']

        Event.objects.create(
            title=title,
            description=description,
            date=date,
            location=location,
            created_by=request.user
        )

        return redirect('my_events')

    return render(request, 'organizer/create_event.html')


# -------------------
# MY EVENTS
# -------------------
@login_required
def my_events(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'organizer/my_events.html', {'events': events})


# -------------------
# EDIT EVENT
# -------------------
@login_required
def edit_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.date = request.POST['date']
        event.location = request.POST['location']
        event.save()

        return redirect('my_events')

    return render(request, 'organizer/edit_event.html', {'event': event})


# -------------------
# DELETE EVENT
# -------------------
@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('my_events')