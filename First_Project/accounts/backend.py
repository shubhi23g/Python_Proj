from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import *
from django.contrib.auth import *
# from django.contrib.auth.models import User
User = get_user_model()


class EmailAuthBackend(ModelBackend):
    def authenticate(request, username=None, password=None):

        try:
            print("kkkkkkkkkkkkkkkkkkkkkkk")
            user = User.objects.get(username=username)
            print(user, "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            if user.check_password(password):
                print("password matched")
                return user
            return None
        except User.DoesNotExist:
            return "doesn't exists"
    
