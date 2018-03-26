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
            url(r'^add_comment/(?P<ans_id>[0-9]+)/$',views.add_comment,name='add_comment'),
            url(r'^search/$',views.search_names,name='search'),
            url(r'^post/(?P<pk>[0-9]+)/delete/$',views.CommentDelete.as_view(),name='comment-delete'),
            url(r'^weather1/$',views.weather1,name='post'),
            url(r'^weather2/$',views.weather2,name='weather2'),
            url(r'^place1/$',views.place1,name='place1'),
            url(r'^place2/$',views.place2,name='place2'),
]