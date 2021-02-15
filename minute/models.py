from django.db import models


# Create your models here.
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
    name = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    item = models.TextField()
    owner = models.CharField(max_length=25)
    recommendations = models.TextField()
    notes = models.TextField()
    issues = models.TextField()
    resolutions = models.TextField()
    Owner = models.CharField(max_length=25)
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
    Approval_date = models.DateField()

    def __str__(self):
        return self.mode_of_meeting
