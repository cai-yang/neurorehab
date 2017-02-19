from rest_framework import serializers
from page.models import *
from django.contrib.auth.models import User


class CateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cate
        fields = ('url','name')

class Cate2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cate2
        fields = ('url','name')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        fields = ('url','title','date_add','description','cate','cate2','content','place','pic','pic_disc')


class ResearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Research
        fields = ('url','title','article','pic')


class CollaborationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaboration
        fields = ('url','name')


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ('url','title','link','author','publish','doi','pdf')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('url','name','link','title','email','content','simple','pic')

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    patient = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='patient-detail')
#    test = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='dateandvalue-detail')
#    class Meta:
#        model = User
#        fields = ('url','username','patient','test')
