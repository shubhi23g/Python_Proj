from rest_framework import serializers
from .models import *
from .views import *


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    followers=serializers.SerializerMethodField()
    # posts = serializers.SerializerMethodField()
    # posts = PostSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'username', 'DOB', 'posts','followers']
        # fields = ['id', 'first_name', 'last_name','email', 'username', 'DOB', 'posts']

    def get_posts(self, obj):
        print("obj:", obj)
        lst = []

        # posts=all_user_post
        all_user_post = Post.objects.filter(user_id=obj.id)
        # here we are trying to filter the user field of the Post model which is foreign key it gets implicitly converted to user_id
        #   
        # or
        # all_user_post = Post.objects.filter(user=obj)
        for i in all_user_post:
            lst.append(
                {
                    'id': i.id,
                    'title': i.title,
                    'text':i.text
                }
            )

        # post = PostSerializer(all_user_post, many=True).data
        # return all_user_post
        return lst
    def get_followers(self,obj):
        # lst=[]
        print("obj:", obj)
        all_user_followers = FollowingList.objects.filter(from_user_id=obj.id)
        print("ssssssssssssssss",all_user_followers)
        follower = FollowingListSerializer(all_user_followers, many=True).data
        return follower

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'user']
class FollowingListSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model=FollowingList
        fields=['from_user_id','to_user_id',"created_at"]
        # fields=['user','from_user_id','to_user_id',"created_at"]
