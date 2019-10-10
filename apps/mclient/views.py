from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.shortcuts import render
from django.http import JsonResponse
from apps.sspanel.models import User
from apps.mclient.utils import auth_permission_required

# Create your views here.
def loginView(request):#登录视图
    username = request.POST.get("username",'')
    password = request.POST.get("password", '')

    try:
        user = User.objects.get(username=username)
        if user.password != password:
            return JsonResponse({"status_code": 401, "message": "Wrong Password"})
    except ObjectDoesNotExist:
        return JsonResponse({"status_code": 401, "message": "User Does not exist"})

    token = user.jwtoken
    return JsonResponse({"status_code": 200, "message": "","token":token})

@auth_permission_required('account.select_user')
def userInfoView(request):#用户数据
    if request.method == 'GET':
        _jsondata = {
            "user": "ops-coffee",
            "site": "https://ops-coffee.cn"
        }

        return JsonResponse({"state": 1, "message": _jsondata})
    else:
        return JsonResponse({"state": 0, "message": "Request method 'POST' not supported"})