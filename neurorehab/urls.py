"""neurorehab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from page import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter(trailing_slash=False)
router.register(r'article',views.ArticleViewSet)
router.register(r'research',views.ResearchViewSet)
router.register(r'cate',views.CateViewSet)
router.register(r'cate2',views.Cate2ViewSet)
router.register(r'achievement',views.AchievementViewSet)
router.register(r'collaboration',views.CollaborationViewSet)
router.register(r'member',views.MemberViewSet)

urlpatterns = [
    url(r'^home/$',views.index),
    url(r'^about_us/$',views.about_us),
    url(r'^hottopics/$',views.topic),
    url(r'^researchs/$', views.research),
    url(r'^members/$', views.member),
    url(r'^achievements/$', views.achievement),
    url(r'^collaborations/$', views.collaboration),
    url(r'^contact/$', views.contact),
    url(r'^article/(\d+)/', views.article),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^',views.redirect_to_home),
]
