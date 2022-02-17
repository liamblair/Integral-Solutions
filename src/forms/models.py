from django.db import models

class GraduateCertificate(models.Model):
    
    pass

    def __str__(self) -> str:
        return

class Courses(models.Model):
    """Model representing the course work table for PhD and Masters"""
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
    title = models.CharField(max_length=40, help_text='Research/Thesis')
    grade = models.CharField(max_length=2, help_text='A')
    credits = models.IntegerField(help_text='3')
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)
    year = models.IntegerField(help_text=2012)

    def __str__(self) -> str:
        return self.number
class Courses_Grad(models.Model):

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

    number = models.CharField(max_length=8, help_text='GRN 500')
    title = models.CharField(max_length=40, help_text='Opportunities and Challenges of Aging')
    credits = models.IntegerField(help_text='3')
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)
    year = models.IntegerField(help_text=2012)

    def __str__(self) -> str:
        return self.number


class Comment(models.Model):
    pass
