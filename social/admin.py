from django.contrib import admin
from .models import Question,post_question,answer


class answerinline(admin.TabularInline):
	model = answer
	extra = 2

class postquestionAdmin(admin.ModelAdmin):
	inlines = [answerinline,]




admin.site.register(Question)
admin.site.register(post_question,postquestionAdmin)
admin.site.register(answer)
