from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('dashboard/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('insert/',views.insertData,name="insertData"),
    path('update/<id>/',views.updateData,name="updateData"),
    path('delete/<id>/',views.deleteData,name="deleteData"),

    path('login/',views.user_login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.user_logout,name="logout"),
]