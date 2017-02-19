# -*- coding: utf-8 -*-

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from page.models import *
from page.serializers import *
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, renderers, viewsets

# Create your views here.

def redirect_to_home(request):#这是一个类
    return HttpResponseRedirect("/home/") #任何未路由的url直接跳转到首页


def about_us(request):#这个括号里是传入参数的意思，传入的是一个HTTP请求
    return render_to_response('about_us.html') #这是返回，返回一个http响应

def index(request):
    member=Member.objects.all()
    research=Research.objects.all()
    return render_to_response('index.html',{'member':member, 'research':research})


def topic(request):
    A = Article.objects.all().order_by('-date_add')
    return render_to_response('hottopics.html',{'A':A})


def research(request):
    research=Research.objects.all()
    return render_to_response('researchs.html',{'research':research})


def collaboration(request):
    collaboration=Collaboration.objects.all()
    return render_to_response('collaborations.html',{'collaboration':collaboration})


def achievement(request):
    achievement=Achievement.objects.all()
    return render_to_response('achievements.html',{'achievement':achievement})


def member(request):
    member=Member.objects.all()
    return render_to_response('members.html',{'member':member})


def contact(request):
    return render_to_response('contact.html')


def article(request, num='1'):
    try:
        a = Article.objects.get(id=num)
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('article.html',{'a':a})


class CateViewSet(viewsets.ModelViewSet):
    queryset = Cate.objects.all()
    serializer_class = CateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Cate2ViewSet(viewsets.ModelViewSet):
    queryset = Cate2.objects.all()
    serializer_class = Cate2Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CollaborationViewSet(viewsets.ModelViewSet):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
