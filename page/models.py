from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Cate(models.Model):
    name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Cate2(models.Model):
    name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title=models.CharField(max_length=200)
    date_posted=models.DateTimeField
    date_add=models.DateTimeField(default=timezone.now)
    date_last_edit=models.DateTimeField(auto_now=True)
    description=models.TextField(blank=True)
    cate=models.ForeignKey(Cate,null=True,blank=True)
    cate2=models.ForeignKey(Cate2,null=True,blank=True)
    content=models.TextField(blank=True)
    place=models.CharField(max_length=50)
    pic=models.CharField(max_length=200)
    pic_disc=models.TextField(blank=True)

    def previous_num(self):
        try:
            return Article.objects.get(pk=self.pk-1).pk
        except:
            return 0
    def next_num(self):
        try:
            return Article.objects.get(pk=self.pk+1).pk
        except:
            return 0

    def __unicode__(self):
        return self.title


class Research(models.Model):
    title=models.CharField(max_length=200)
    article=models.ForeignKey(Article,null=True, blank=True)
    pic=models.CharField(max_length=100,blank=True)

    def __unicode__(self):
        return self.title


class Achievement(models.Model):
    title=models.CharField(max_length=200)
    link=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    publish=models.CharField(max_length=200)
    pdf=models.CharField(max_length=200)
    doi=models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.title + 'by' + self.author)

class  Collaboration(models.Model):
    name=models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class Member(models.Model):
    name=models.CharField(max_length=20)
    link=models.CharField(max_length=50)
    title=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    content=models.TextField(blank=True)
    simple=models.TextField(blank=True)
    pic=models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
