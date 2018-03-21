from django.shortcuts import render,render_to_response,redirect
from .forms import UserForm,question_form,discuss_form,comment_form
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,answer,post_question
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime
import requests
# Create your views here.

def IndexView(request):
	return render(request,'social/index.html')

def register(request):
	context=RequestContext(request)

	registered=False
	if request.method=='POST':	
		user_form=UserForm(data=request.POST)

		if user_form.is_valid():
			user=user_form.save()

			user.set_password(user.password)
			user.save()

			registered=True

			subject='Thankyou for registering'
			message='Welcome to the website'
			from_email=settings.EMAIL_HOST_USER
			to_list=user_form.cleaned_data['email'],  
			send_mail(subject,message,from_email,to_list,fail_silently=True)

		else:
			print user_form.errors

	else:
		user_form=UserForm()

	return render_to_response('social/registration_form.html',{'user_form':user_form,'registered':registered},context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(username=username, password=password)

        
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                
                login(request, user)
                return HttpResponseRedirect('/social/profile/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
           
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('social/login.html', {}, context)


def profile(request):
    args={'user':request.user}
    return render(request,'social/profile.html',args)


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/social/')


def user_question(request):
	context=RequestContext(request)
	registered=False
	if request.method=='POST':	
		
		form=question_form(data=request.POST)

		if form.is_valid():
			print form
			form.save()

			registered=True
			"""
			subject='Thankyou for asking Question'
			message='you will be soon updated with your answer'
			from_email=settings.EMAIL_HOST_USER
			to_list=request.user.username
			send_mail(subject,message,from_email,to_list,fail_silently=True)"""

		else:
			print form.errors

	else:
		form=question_form()

	return render_to_response('social/question_form.html',{'form':form,'registered':registered},context)


def ask_question(request):
  context=RequestContext(request)
  registered=False
  if request.method=='POST':	

    form=discuss_form(data=request.POST)

    if form.is_valid():
      form.save()
      registered=True
      return redirect('/social/post/')
    else:
      print form.errors

  else:
    form=discuss_form()

  return render_to_response('social/ask.html',{'form':form,'registered':registered},context)

def post(request):
  post=post_question.objects.all()
  post2 = answer.objects.all()
  return render(request,'social/public.html',{'post':post,'post2':post2})


def add_comment(request,ans_id):
  ans=get_object_or_404(post_question,pk=ans_id)
  form=comment_form(request.POST)
  print form.is_valid()
  if form.is_valid():
    print "this"
    user_name=form.cleaned_data['user_name']
    comment=form.cleaned_data['comment']
    add=answer()
    add.user_name=user_name
    add.comment=comment
    add.pub_date = datetime.datetime.now()
    ob=post_question.objects.get(id=ans_id)
    add.ques=ob
    add.save()
    return redirect('/social/post/')

  return render(request, 'social/comment.html', {'ans': ans, 'form': form})


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import Question
from .serializers import StockSerializer1,StockSerializer2,StockSerializer3,StockSerializer4

 
class Users_List(APIView):

      def get(self,request):
          stocks = User.objects.all()
          serializer=StockSerializer1(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


class Question_List(APIView):

      def get(self,request):
          stocks = Question.objects.all()
          serializer=StockSerializer2(stocks,many=True)
          return Response(serializer.data)


      def post(self):
          pass

class POST_QUESTION(APIView):

      def get(self,request):
          stocks = post_question.objects.all()
          serializer=StockSerializer3(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


class ANSWER_LIST(APIView):

      def get(self,request):
          stocks = answer.objects.all()
          serializer=StockSerializer4(stocks,many=True)
          return Response(serializer.data)


      def post(self):
          pass


def like_article(request,ans_id):
  if ans_id:
    a=post_question.objects.get(id=ans_id)
    count=a.likes
    count+=1
    a.likes=count
    a.save()
  return redirect('/social/post/') 
    

from django.http import JsonResponse
def search_names(request):
  if request.method=='POST':
    search_text=request.POST['search_text']
  else:
    search_text=''
  names=answer.objects.filter(user_name__contains=search_text)
  level_list = []
  temp_data = {}
  for name in names:
    temp_data = {
                "name": name.user_name,
              }
    level_list.append(temp_data)
    temp_data = {}
  data = {
    "success": True,
    "names" : level_list,
  }
  return JsonResponse(data,safe=False)


from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
class CommentDelete(DeleteView):
  model=answer
  success_url=reverse_lazy('social:post')


from .forms import weather_form
def weather1(request):
  form=weather_form()
  return render_to_response('social/weather.html',{'form':form})



def weather2(request):
  if request.method=='POST':
    form=weather_form(data=request.POST)
    if form.is_valid:
      city=form['city'].value()
      city=city.upper()
      api_address='http://api.openweathermap.org/data/2.5/weather?appid=578d43fc73ac077f3e7666baf2444681&q='
      url = api_address + city

      json_data = requests.get(url).json()
      formatted_data = json_data['weather'][0]['description']

      print(formatted_data)
  return HttpResponse(formatted_data)























  
























































































































































































































































































































































































































































































































































































































































































































