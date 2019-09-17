from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EveTimerForm
from .models import EveTimer
from datetime import datetime, timedelta 

def add_timer(request):
    if request.method == "POST":
        days = request.POST['days']
        hours = request.POST['hours']
        minutes = request.POST['minutes']
        seconds = request.POST['seconds']
        request.POST['timer'] = datetime.utcnow() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        form = EveTimerForm(request.POST)

        if form.is_valid():
            EveTimer(
                name=form.cleaned_data['name'],
                timer=form.cleaned_data['timer'],
                user=request.user,
                type=type,
            ).save()
            messages.success(request, 'Succesfully added timer: %s' % form.cleaned_data['name'])
            return redirect('django-eveonline-timerboard-view')
        else:
            messages.error(request, 'Failed to add timer: %s' % form.cleaned_data['name'])
            return redirect('django-eveonline-timerboard-view')

    else: 
        form = EveTimerForm()  

def remove_timer(request, pk):
    EveTimer.objects.get(pk=pk).delete()
    return redirect('django-eveonline-timerboard-view')
      

def view_timerboard(request):
    timers = EveTimer.objects.filter(timer__gte=datetime.utcnow())
    context = {
        'timers': timers
    }
    return render(request, 'django_eveonline_timerboard/adminlte/timerboard.html', context)