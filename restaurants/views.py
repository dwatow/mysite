# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response

from restaurants.models import Restaurant, Food, Comment
import datetime

from restaurants.forms import CommentForm

'''
def menu(request):
    path = request.path
    restaurants = Restaurant.objects.all()
    return render_to_response('menu.html',locals())
'''
def menu(request):
    if id:
        r = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html',locals())
    
def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
        
    errors = []
    if 'ok' in request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            user = request.POST['user']
            content = request.POST['content']
            email = request.POST['email']
            date_time = datetime.datetime.now()
            c = Comment(user=user, email=email, content=content, date_time=date_time, restaurant=r)
            c.save()
            f = CommentForm()
    else:
        f = CommentForm()
        return HttpResponse("run this")

    return render_to_response('comments.html',locals())