from django.urls import include, path, re_path
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt
#from werobot.contrib.django import make_view
from . import views

app_name = "mclient"

urlpatterns = [
    path('login/', csrf_exempt(views.loginView), name='loginView'),
    path('reg/', csrf_exempt(views.regView), name='regView'),
    path('userinfo/', csrf_exempt(views.userInfoView), name='userInfoView'),
]