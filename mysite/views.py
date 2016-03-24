# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response


def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def use_session(request):
    request.session['lucky_number'] = 8                               # 設置lucky_number

    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']                # 讀取lucky_number

        response = HttpResponse('Your lucky_number is '+lucky_number)
    del request.session['lucky_number']                               # 刪除lucky_number

    return response