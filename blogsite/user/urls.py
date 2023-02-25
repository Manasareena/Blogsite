from django.urls import path
from user.views import *
urlpatterns=[
    path('home/',User.as_view(),name="uhome"),
    path('upro/',ViewProfile.as_view(),name="upro"),
    path('blogs/',MyBlogs.as_view(),name='blog'),
    path('addbio/',UserProView.as_view(),name="addbio"),
    path('chpsw/',PasswordView.as_view(),name="change-password"),
    path('updatebio/<int:user_id>',UpdateBioView.as_view(),name="updatebio"),
    path('addcmnt/<int:id>',add_comment,name='add-cmnt'),
    path('blog/like/<int:bid>',add_like,name='add_like')
]