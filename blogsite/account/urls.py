from django.urls import path
from .views import *

urlpatterns=[
   path('reg/',Signup.as_view(),name="reg"),
   path('logi/',SignIn.as_view(),name="logi"),
   path('logo/',SignOut.as_view(),name="logo"),

]