from django.shortcuts import render, get_object_or_404
from schedule.models import *
# Create your views here.

def userlist(request) : 
    users = User.objects.all()
    return render(request, 'schedule/index.html', {'users' : users})

def detail(request, user_id) : 
    select_user = get_object_or_404(User, pk = user_id)
    try : 
        user_timetable = select_user.timetable_set.all()
        print(user_timetable)
    #user_timetable = select_user.timetable_set.all()
    except(KeyError, user_timetable.DoesNotExist) :
        return render(request, 'schedule/detail.html', {
            'user' : select_user,
            'error_message' : 'No Timetable'
        })
    
    else :
    
        return render(request, 'schedule/detail.html', {
        'user' : select_user,
        'timetable' : user_timetable
        })