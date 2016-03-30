# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib import auth

def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def use_session(request):
    request.session['lucky_number'] = '8'                               # 設置lucky_number

    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']                # 讀取lucky_number

        response = HttpResponse('Your lucky_number is ' + lucky_number)
    del request.session['lucky_number']                               # 刪除lucky_number
    
    return response

def session_test(request):
    sid = request.COOKIES['sessionid']
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + str(sid) + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.') 
        
def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response

        
def login_page(request):
    
    #如果用戶已經登入，則HttpRequest.user是一個User物件，也就是具名用戶。
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/index/')
        
    #如果使用者尚未登入，HttpRequest.user是一個AnonymousUser物件，也就是匿名用戶。
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')
        