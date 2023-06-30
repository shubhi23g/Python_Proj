from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import (post_save, pre_save, pre_delete, post_delete)

# User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    DOB = models.DateField(auto_now_add=True)

    class Meta:
        managed = True


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id= models.ForeignKey(settings.AUTH_USER_MODLE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name_plural = 'Post'


@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    # created is not there in the pre_save i.e. becoz pre_save happens before creation
    # before saved in the database
    print(instance.username, instance.id)
    # Trigger pre_save
    # instance.save()
    # trigger post_save
    # (uncomment:instance.save() )error: RecursionError: maximum recursion depth exceeded
    # becoz the save function is calling itself over and over again

# OR  pre_save.connect(user_pre_save_receiver,sender=User)


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    # after saved in the database
    if created:
        print("Send email to ", instance.username)
        # Trigger pre_save
        # instance.save()
        # trigger post_save
        # here it resaves it again. recursive max depth error doesn't come
    else:
        print(instance.username, "was just saved ")


@receiver(pre_delete, sender=Post)
def blogpost_pre_delete_receiver(sender, instance, *args, **kwargs):
    print(f"{instance.id} will be removed")


@receiver(post_delete, sender=Post)
def blogpost_post_delete_receiver(sender, instance, *args, **kwargs):
    print(f"{instance.id} has removed")


class FollowingList(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='from_user')
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    created_at=models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('from_user', 'to_user')