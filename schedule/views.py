from django.shortcuts import render, get_object_or_404
from schedule.models import *
# Create your views here.

def userlist(request) : 
    users = User.objects.all()
    return render(request, 'schedule/index.html', {'users' : users})

def detail(request, user_id) : 
    select_user = get_object_or_404(User, pk = user_id)
    try : 
        user_timetable = select_user.timetable_set.all().order_by('day')
        user_timetable0 = select_user.timetable_set.all().get(day = 0)
        user_timetable1 = select_user.timetable_set.all().get(day = 1)
        user_timetable2 = select_user.timetable_set.all().get(day = 2)
        user_timetable3 = select_user.timetable_set.all().get(day = 3)
        user_timetable4 = select_user.timetable_set.all().get(day = 4)

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
        'timetable' : user_timetable,
        'timetable0' : user_timetable0,
        'timetable1' : user_timetable1,
        'timetable2' : user_timetable2,
        'timetable3' : user_timetable3,
        'timetable4' : user_timetable4,
        })

    

def team(request, team_id) :
    select_team = get_object_or_404(User, pk = team_id)
    select_team.all