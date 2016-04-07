# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

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

'''
def login(request):

    #如果用戶已經登入，則HttpRequest.user是一個User物件，也就是具名用戶。
    #所以如果使用者已經認證過，我們將他重導回首頁
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/')

    #如果使用者尚未登入，HttpRequest.user是一個AnonymousUser物件，也就是匿名用戶。
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    #使用auth中的authenticate方法來確認用戶
    user = auth.authenticate(username=username, password=password)
    
                            #帳戶沒有被凍結
    if user is not None and user.is_active:
        auth.login(request, user) #真正登入使用者並保持他的登入狀態
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html')
'''
def index(request):
    return render_to_response('index.html',locals())
'''
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    '''
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',locals())
