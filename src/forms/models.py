from django.db import models

class GraduateCertificate(models.Model):
    
    grad_program_of_study = models.Inte

    def __str__(self) -> str:
        return

class Courses(models.Model):
    FALL = 'Fall'
    WINTER = 'Winter'
    SPRING = 'Spring'
    SUMMER = 'Summer'

    SEMESTER_CHOICES = [
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
    ]

    type = models.CharField(max_length=1, help_text='P for prerequisite; T for transfer; otherwise - blank')
    instituion = models.CharField(max_length=30, help_text='UMaine')
    number = models.CharField(max_length=10, help_text='INT 699')
    title = models.CharField(max_length=40, help_text='Research/thesis')
    grade = models.CharField(max_length=2, help_text='A')
    credits = models.IntegerField()
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    year = models.IntegerField()