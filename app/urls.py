from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name="index_page"),
    path('calendar/',views.calendar,name="calendar"),
    path('entry/<int:entry_id>/',views.details,name="details_page"),
    path('entry/add/',views.add_entry,name="add_entry"),
    path('entry/<int:entry_id>/addfavorite/',views.favorite_entry,name="favorite_entry"),
    path('entry/<int:entry_id>/remove/',views.remove,name="remove"),
    path('register/',views.register,name="register"),

    #LOGIN LOGOUT

    path('login/',auth_views.login,name="login"),
    path('logout/',auth_views.logout,{'next_page':'/'},name="logout"),
    path('accounts/profile/',views.calendar,name="login_calendar"),
]
