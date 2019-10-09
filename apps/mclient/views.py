from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.shortcuts import render
from django.http import JsonResponse
from apps.sspanel.models import User

# Create your views here.
def loginView(request):#登录视图
    username = request.GET.get("username",'')
    password = request.GET.get("password", '')

    try:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return JsonResponse({"status_code": 401, "message": "Wrong Password"})
    except ObjectDoesNotExist:
        return JsonResponse({"status_code": 401, "message": "User Does not exist"})

    token = user.jwtoken
    return JsonResponse({"status_code": 200, "message": "","token":token})