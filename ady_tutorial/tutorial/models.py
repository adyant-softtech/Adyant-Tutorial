
# pre_save post_save
# pre_delete post_delete

from django.db.models.signals  import post_save, pre_save
from django.dispatch import receiver

from django.db import models
from tutorial import mail
# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=100) # default:  null=True blank=True
    stu_class = models.CharField(max_length=20)
    stu_branch = models.CharField(max_length=100)
    collage_name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    address = models.TextField()

@receiver(post_save, sender=Student)
def send_mail(sender, **kwargs):
    print('Hello after student registration')
    mail.notify()


@receiver(pre_save, sender=Student)
def send_mail(sender, **kwargs):
    print('Hello before student registration')




