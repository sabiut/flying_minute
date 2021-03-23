from django.db import models

# Create your models here.
from partial_date import PartialDateField


class fly_minute(models.Model):
    mode = (
        ('Email', 'Email'),
        ('Zoom', 'Zoom'),
        ('Alternative', 'Alternative'),
    )
    mode_of_meeting = models.CharField(max_length=100, choices=mode, blank=False, )
    date = models.DateField()
    Time = models.TimeField()
    minute_prepared_by = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    authorize_by = models.CharField(max_length=25)
    item = models.TextField()
    owner = models.CharField(max_length=25)
    recommendations = models.TextField()
    notes = models.TextField()
    issues = models.TextField()
    resolutions = models.TextField()
    resolution_Owner = models.CharField(max_length=25)
    due_date = models.DateField()
    Action = models.TextField()
    department_or_person_responsible = models.CharField(max_length=25)
    people = (
        ('Andrew Kausiama', 'Andrew Kausiama'),
        ('Simeon Athy', 'Simeon Athy'),
        ('Votasui Maclemzie Reur', 'Votasui Maclemzie Reur'),
        ('Serah Obed', 'Serah Obed'),
        ('Steven Tahi', 'Steven Tahi'),
    )

    authorize_by_chairman = models.CharField(max_length=100, choices=people, blank=False, )
    authorize_by_director_ex_officio = models.CharField(max_length=100, choices=people, blank=False, )
    authorize_by_directors = models.TextField(max_length=100, choices=people, blank=False, )
    Minute_approved_by_the_Chairmen = models.CharField(max_length=25)
    Approval_date = models.DateField(null= True)

    def __str__(self):
        return self.mode_of_meeting


class MembersPresent(models.Model):
    flyminute = models.ForeignKey(fly_minute,
                                  related_name='memberspresent_set',
                                  on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class BoardMembers(models.Model):
    name = models.CharField(max_length=100, default='')
    island = models.CharField(max_length=100, default='', null=True)
    region = (
        ('Torba', 'Torba'),
        ('Sanma', 'Sanma'),
        ('Penama', 'Penama'),
        ('Malampa', 'Malampa'),
        ('Shefa', 'Shefa'),
        ('Tafea', 'Tafea'),

    )

    province = models.CharField(max_length=100, choices=region, blank=False, null=True)

    residential_address = models.CharField(max_length=100, default='', null=True)
    status = models.CharField(max_length=100, default='', null=True)
    email = models.EmailField(max_length=100, default='', null=True)
    phone = models.CharField(max_length=100, default='', null=True)
    emergency_contact_person = models.CharField(max_length=100, null=True)
    relationship = models.CharField(max_length=100, default='', null=True)
    emergency_contact = models.IntegerField(default='0', null=True)
    blood = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),

    )

    blood_type = models.CharField(max_length=100, choices=blood, blank=False, null=True)
    CV = models.FileField(upload_to='board_cv/pdf/')
    start_date = models.DateField(max_length=100, null=True)

    def __str__(self):
        return self.name
