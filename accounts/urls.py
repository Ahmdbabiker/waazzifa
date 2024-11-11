from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logining/' , views.loggining , name='login'),
    path('logout' , views.logginout , name='logout' ),
    path('add-files/' ,  views.add_files , name="addfiles"),
    path('registration_complete/',views.registration_complete , name='registration_complete'),
    path('profile/<int:profile_id>' , views.profile_data , name="profile")
]
