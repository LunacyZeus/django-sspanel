from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.shortcuts import render
from django.http import JsonResponse
from apps.sspanel.models import User,UserTraffic
from apps.mclient.utils import auth_permission_required

# Create your views here.
def loginView(request):#登录视图
    username = request.POST.get("username",'')
    password = request.POST.get("password", '')

    try:
        user = authenticate(username=username,password=password)
        #if user.password != password:
        if not user:
            return JsonResponse({"status_code": 401, "message": "Wrong Password","token":""})
    except ObjectDoesNotExist:
        return JsonResponse({"status_code": 404, "message": "User Does not exist","token":""})

    token = user.jwtoken
    return JsonResponse({"status_code": 200, "message": "","token":token})

def regView(request):#注册视图
    username = request.POST.get("username",'')
    password1 = request.POST.get("password1",'')
    email = request.POST.get("email",'')
    invitecode = request.POST.get("invitecode",'')

    if request.method != "POST":
        return JsonResponse({"status_code": 0, "message": "Request only supported method 'POST'"})
    if username == "":
        return JsonResponse({"status_code": 0, "message": "username empty"})
    if password1 == "":
        return JsonResponse({"status_code": 0, "message": "password empty"})
    if email == "":
        return JsonResponse({"status_code": 0, "message": "email empty"})
    if invitecode == "":
        return JsonResponse({"status_code": 0, "message": "invitecode empty"})

    user = User.add_new_user({"username":username,"password1":password1,"email":email,"invitecode":invitecode,})
    if not user:
        return JsonResponse({"status_code": 0, "message": "something error,pls contact admin"})
    else:
        return JsonResponse({"status_code": 200, "message": "success reg"})

@auth_permission_required('account.select_user')
def userInfoView(request):#用户数据
    if request.method == 'GET':
        try:
            TrafficInfo = UserTraffic.objects.get(user_id=request.user.id)
        except ObjectDoesNotExist:
            #print(request.user)
            return JsonResponse({"status_code": 404, "message": "UserInfo Does not exist"})

        _jsondata = {
            "upload_traffic": TrafficInfo.upload_traffic,
            "download_traffic": TrafficInfo.download_traffic,
            "total_traffic": TrafficInfo.total_traffic,
            "last_use_time": TrafficInfo.last_use_time,
        }
        return JsonResponse({"status_code": 200, "message": _jsondata})
    else:
        return JsonResponse({"status_code": 0, "message": "Request method 'POST' not supported"})