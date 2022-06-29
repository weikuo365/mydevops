from django.http import HttpResponse
from django.shortcuts import render
from scanhosts.models import *
import json


# Create your views here.

def getinfo(request):
    remote_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']
    user_obj = UserIPInfo.objects.filter(ip=remote_addr)
    if not user_obj:  # 查询IP不存在
        res = UserIPInfo.objects.create(ip=remote_addr)
        ip_addr_id = res
    else:
        ip_addr_id = user_obj[0]

    BrowseInfo.objects.create(only_id=user_ua, userip=ip_addr_id)

    result = {
        "STATUS": "success",
        "INFO": "User info",
        "IP": remote_addr,
        "UA": user_ua
    }
    return HttpResponse(json.dumps(result), content_type="application/json")


def userinfos(request):
    ip_list = UserIPInfo.objects.all()
    infos = {}
    for item in ip_list:
        infos[item.ip] = [b_obj.only_id for b_obj in BrowseInfo.objects.filter(userip=item.id)]
    result = {
        "STATUS": "success",
        "INFO": infos
    }
    return HttpResponse(json.dumps(infos), content_type="application/json")
