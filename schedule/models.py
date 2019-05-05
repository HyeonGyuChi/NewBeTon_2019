from django.db import models

# Create your models here.

class User(models.Model) : 
    name = models.CharField(max_length = 20) # 유저이름

    def __str__(self) : 
        return self.name

class TimeTable(models.Model) : 
    DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
    )

    TABLE_TIME = (
    (9, '9시'),
    (10, '10시'),
    (11, '11시'),
    (12, '12시'),
    (13, '13시'),
    (14, '14시'),
    (15, '15시'),
    (16, '16시'),
    (17, '17시'),
    (18, '18시'),
    )

    subject_name = models.CharField(max_length = 30) # 과목명
    day = models.IntegerField(choices = DAYS_OF_WEEK) # 요일
    start_time = models.IntegerField(choices = TABLE_TIME) # 시작시간
    end_time = models.IntegerField(choices = TABLE_TIME) # 종료시간
    user_id = models.ForeignKey(User, on_delete = 'CASCADE')# 외래키 User_id


    
    #def __str__(self) : 
    #    return self.subject_name

class Team(models.Model) : 
    name = models.CharField(max_length = 20) # 프로젝트이름
    a = models.IntegerField() # 참가자 a id
    b = models.IntegerField() # 참가자 b id
    c = models.IntegerField() # 참가자 c id 
    d = models.IntegerField() # 참가자 d id 
    
    
