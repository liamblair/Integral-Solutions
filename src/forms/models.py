from django.db import models
from django.forms import BooleanField
from multiselectfield import MultiSelectField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Course(models.Model):
    """
    Model representing the course work table for PhD and Masters
    """
    
    SEMESTER_CHOICES = (('FALL', 'Fall'),
                        ('SPRING', 'Spring'),
                        ('SUMMER', 'Summer'),
                        ('WINTER', 'Winter'))

    type = models.CharField(max_length=1, help_text='P for prerequisite; T for transfer; otherwise - blank')
    instituion = models.CharField(max_length=150, help_text='UMaine')
    number = models.CharField(max_length=10, help_text='INT 699')
    title = models.CharField(max_length=150, help_text='Research/Thesis')
    grade = models.CharField(max_length=2, help_text='A')
    credits = models.IntegerField(help_text='3')
    semester = MultiSelectField(max_length=6, choices=SEMESTER_CHOICES)
    year = models.IntegerField(help_text=2012)

    # These lines are needed for Generic Relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return self.number


class Course_Grad(models.Model):
    """
    Model representing the course work table for the Graduate Certificate
    """
    
    SEMESTER_CHOICES = (('FALL', 'Fall'),
                        ('SPRING', 'Spring'),
                        ('SUMMER', 'Summer'),
                        ('WINTER', 'Winter'))

    number = models.CharField(max_length=10, help_text='GRN 500')
    title = models.CharField(max_length=150, help_text='Opportunities and Challenges of Aging')
    credits = models.IntegerField(help_text='3')
    semester = MultiSelectField(max_length=6, choices=SEMESTER_CHOICES)
    year = models.IntegerField(help_text=2012)

    # These lines are needed for Generic Relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return self.number


class Comment(models.Model):
    """
    Model representing comments
    """
    comment = models.TextField()
    author = models.CharField(max_length=30)

    # These lines are needed for Generic Relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return self.comment


class GraduateCertificate(models.Model):
    """
    Model representing the Graduate Certificate program of study form
    """

    CERTIFICATE_CHOICES = ((1, 'Graduate Certificate in Geographic Information Systems'),
                           (2, 'Graduate Certificate in Information Systems'),
                           (3, 'Graduate Certificate in Data Science and Engineering'),
                           (4, 'Graduate Certificate in Computing for Educators SCIS'))

    certificate = MultiSelectField(choices=CERTIFICATE_CHOICES)
    courses = GenericRelation(Course_Grad)
    comments = GenericRelation(Comment)

    esign_student = models.BooleanField()
    esign_gradcoord = models.BooleanField()


    def __str__(self):
        return self.certificate
    

class MastersDegree(models.Model):
    """
    Model representing the Masters degree program of study form
    """
    
    DEGREE_CHOICES = ((1, 'MS Computer Science'),
                      (2, 'MS Data Science and Engineering'),
                      (3, 'MS Spatial Information Science and Engineering'),
                      (4, 'MS Spatial Informatics'))
    
    QUESTION_CHOICES = ((1, 'Yes'),
                        (2, 'Not Applicable'))

    degree = MultiSelectField(choices=DEGREE_CHOICES)
    institutional_req = models.TextField()
    conduct_of_research = MultiSelectField(choices=QUESTION_CHOICES)
    conduct_course = models.CharField(max_length=150)
    human_subjects_review = MultiSelectField(choices=QUESTION_CHOICES)
    animal_subjects_review = MultiSelectField(choices=QUESTION_CHOICES)
    dissertation_topic = models.CharField(max_length=150)
    dissertation_plan = models.TextField()

    courses = GenericRelation(Course)
    comments = GenericRelation(Comment)

    esign_student = models.BooleanField()
    esign_adviser = models,BooleanField()
    esign_gradcoord = models.BooleanField()
    esign_comm1 = models.BooleanField()
    esign_comm2 = models.BooleanField()
    esign_comm3 = models.BooleanField()
    esign_comm4 = models.BooleanField()


    def __str__(self):
        return self.degree


class PhDDegree(models.Model):
    """
    Model representing the PhD program of study form
    """

    DEGREE_CHOICES = ((1, 'PhD Computer Science'),
                      (2, 'PhD Spatial Information Science and Engineering'))

    QUESTION_CHOICES = ((1, 'Yes'),
                        (2, 'Not Applicable'))
    
    degree = MultiSelectField(choices=DEGREE_CHOICES)
    institutional_req = models.TextField()
    conduct_of_research = MultiSelectField(choices=QUESTION_CHOICES)
    conduct_course = models.CharField(max_length=150)
    human_subjects_review = MultiSelectField(choices=QUESTION_CHOICES)
    animal_subjects_review = MultiSelectField(choices=QUESTION_CHOICES)
    dissertation_topic = models.CharField(max_length=150)
    dissertation_plan = models.TextField()

    courses = GenericRelation(Course)
    comments = GenericRelation(Comment)

    esign_student = models.BooleanField()
    esign_adviser = models,BooleanField()
    esign_gradcoord = models.BooleanField()
    esign_comm1 = models.BooleanField()
    esign_comm2 = models.BooleanField()
    esign_comm3 = models.BooleanField()
    esign_comm4 = models.BooleanField()


    def __str__(self):
        return self.degree
  