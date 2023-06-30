from django.urls import include, re_path
from .views import *

urlpatterns = [
    re_path(r"^signup/$", signup_api, name="signup_api"),
    re_path(r"^user-list/$", user_list, name="user_list"),
    re_path(r"^searchfromStart/$", search_StartsWith,
            name="search_StartsWith"),
    re_path(r"^searchBetween/$", search_cont, name="search__cont"),
    re_path(r"^login/$", login, name="login"),
    re_path(r"^get-profile/$", get_profile, name="get_profile"),
    re_path(r"^update-profile/$", update_profile, name="update_profile"),
    re_path(r"^add-post/$", add_post, name="add_post"),
    re_path(r"^get-post/$", get_post, name="get_post"),
    re_path(r"^change-pass/$",change_pass,name="change_pass"),
    re_path(r"^filter-date/$",filter_date,name="filter_date"),
    re_path(r"^get-all-posts/$",get_all_posts, name="get_all_posts"),
    re_path(r"^logout/$",user_logout,name="user_logout"),
    re_path(r"^follow/$",follow,name="follow"),
    re_path(r"^get-following/$",get_following,name="get_following"),
    re_path(r"^unfollow/$",unfollow,name="unfollow"),
]
# repath is same as path
