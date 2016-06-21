# _*_ coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Create your models here.

#建表

class Article(models.Model):
    title = models.CharField(max_length=255)
    brief = models.CharField(null=True,blank=True,max_length=255)
    category = models.ForeignKey('Category')   #从上往下执行，此时表还未创建，此表在下面需要先引起来，不然找不到
    content = models.TextField(u'文章内容')
    author = models.ForeignKey("UserProfile")
    pub_date = models.DateTimeField(blank=True,null=True)      #auto_now  修改后就保存一个新的时间  auto_now_add  自动创建陈当前时间
    last_modify = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(u'优先级',default=1000)
    head_img = models.ImageField(u'文章标题图片',upload_to="uploads")
    status_choices = (('draft',u'草稿'),
                      ('published',u'已发布'),
                      ('hidden',u'隐藏'),
                      )
    status = models.CharField(max_length=50,choices=status_choices,default='published')
    def __str__(self):
        return self.title

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name=u'所属文章')
    parent_comment = models.ForeignKey('self',related_name='my_childern',blank=True,null=True)
    comment_choices = ((1,u'评论'),
                       (2,u'点赞'))
    comment_type = models.IntegerField(choices=comment_choices,default=1)
    user = models.ForeignKey('UserProfile')
    comment = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.comment_type == 1 and len(self.comment)==0:
            raise ValidationError(u'内容不能为空......')

    def __str__(self):
        return "C:%s" %(self.comment)

class Category(models.Model):
    name = models.CharField(max_length=64)
    brief = models.CharField(null=True,blank=True,max_length=255)
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField('UserProfile',blank=True)
    def __str__(self):
        return self.name
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255,blank=True,null=True)
    head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)

    def __str__(self):
        return self.name