# -*- coding: utf-8 -*-
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from restaurants.forms import CommentForm
from restaurants.models import Restaurant, Food, Comment
import datetime


def menu_id(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def menu(request):
    if id:
        r = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

@login_required
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    print request.user.user_permissions.all()
    return render_to_response('restaurants_list.html',
                               locals(),
                               context_instance=RequestContext(request))

def user_can_comment(user):
    return user.is_authenticated and user.has_perm('restaurants.can_comment')
    
@user_passes_test(user_can_comment, login_url='/accounts/login/')
def comment(request,id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")

    if request.user.is_authenticated and request.user.has_perm('restaurants.can_comment'):
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
    else:
        return HttpReponseRedirect('/restaurants_list/')
        
    return render_to_response('comments.html',locals())
    
