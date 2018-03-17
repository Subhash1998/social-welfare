from django.shortcuts import render,render_to_response
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
		else:
			print form.errors

	else:
		form=discuss_form()

	return render_to_response('social/ask.html',{'form':form,'registered':registered},context)

def post(request):
  post=post_question.objects.all()
  post2=answer.objects.all()
  return render(request,'social/public.html',{'post':post,'post2':post2})


def discuss(request):
    return render(request, 'social/public.html')


def add_comment(request,ques_id):
  ans=get_object_or_404(post_question,pk=ques_id)
  form=comment_form(request.POST)
  print ques_id
  print form.is_valid()
  if form.is_valid():
    print "this"
    user_name=form.cleaned_data['user_name']
    comment=form.cleaned_data['comment']
    add=answer()
    add.user_name=user_name
    add.comment=comment
    add.pub_date = datetime.datetime.now()
    ob=post_question.objects.get(id=ques_id)
    add.ques=ob
    add.save()
    return HttpResponseRedirect(reverse('social:add_comment', args=(ans.id,)))
    
  return render(request, 'social/comment.html', {'ans': ans, 'form': form})

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import Question
from .serializers import StockSerializer

 
class Users_List(APIView):

      def get(self,request):
          stocks = User.objects.all()
          serializer=StockSerializer(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


class Question_List(APIView):

      def get(self,request):
          stocks = Question.objects.all()
          serializer=StockSerializer(stocks,many=True)
          return Response(serializer.data)


      def post(self):
          pass

