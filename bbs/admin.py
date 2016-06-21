from django.contrib import admin
from  bbs import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.
class ArtileAdmin(admin.ModelAdmin):
    list_display = ('title','category','author','pub_date','last_modify','status','priority')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','parent_comment','comment_type','comment','user','date')
class CategoruAdmin(admin.ModelAdmin):
    list_display = ('name','set_as_top_menu','position_index')
admin.site.register(models.Article,ArtileAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.Category,CategoruAdmin)
