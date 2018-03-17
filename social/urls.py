from django.conf.urls import url
from . import views

app_name='social'

urlpatterns=[
            url(r'^$',views.IndexView,name='home'),
            url(r'^register/$',views.register,name='register'),
            url(r'^login/$',views.user_login,name='login'),
            url(r'^profile/$',views.profile,name='profile'),
            url(r'^logout/$',views.user_logout,name='logout'),
            url(r'^question/$',views.user_question,name='question'),
            url(r'^ask_question/$',views.ask_question,name='ask'),
            url(r'^post/$',views.post,name='post'),
            url(r'^discuss/$',views.discuss,name='discuss'),
            url(r'^add_comment/(?P<ques_id>[0-9]+)/$',views.add_comment,name='add_comment'),
]