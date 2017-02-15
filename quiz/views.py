from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from models import Question,Result
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.contrib.auth import authenticate,login
from .forms import RegistrationForm,AdminLoginForm
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User

# Create your views here.




class IndexView(generic.ListView):
	template_name="quiz/index.html"
	context_object_name='question_set'
	
	def get_queryset(self):
		return Question.objects.all()

class DetailView(generic.DetailView):
	model=Question
	template_name='quiz/detail.html'


def index(request):
	question_set=Question.objects.all()
	context={ 
	          "question_set":question_set
	       }
	return render(request,"quiz/index.html",context)


def register(request):
	return render(request,"quiz/register.html")

def process_data(request):
	question_set=Question.objects.all()
	choice_list=[]
	question_set
	for k, v in request.POST.items():
		if k.startswith('choice'):
			choice_list.append(v)
	i=0
	score=0
	for question in question_set:
			if question.answer1==choice_list[i]:
				print question.answer1
				i=i+1
				score=score+1
	user_score=score
	print request.user
	user_object=Result.objects.get(username=request.user)
	user_object.score=user_score
	user_object.save()
	
	#saving score to db


	return render(request,'quiz/logout.html',{'user_object':user_object})


#regstration for the participants

class RegistrationView(View):
	form_class=RegistrationForm
	template_name='quiz/user_login_form.html'


	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():

			user=form.save(commit=False)

			#cleaned (normalized) data
			username =form.cleaned_data['username']
			password =form.cleaned_data['password']
			email=form.cleaned_data['email']

			user.set_password(password)
			user.save()

			user_object=Result()
			user_object.username=user.username
			user_object.email=user.email
			user_object.score=0
			current_user=username
			user_object.save()
	

			#authenticatin

			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
						login(request,user)
						question_set=Question.objects.all()
						return render(request,'quiz/quiz_page.html',{'question_set':question_set})

		return render(request,self.template_name,{'form':form,})


#login interface for the admin

class AdminLoginView(View):
	form_class=AdminLoginForm
	template_name='quiz/user_login_form.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})


	def post(self,request):
		form=self.form_class(request.POST)

		admin_name="admin"
		admin_password="admin1234"

		if form.is_valid():

			#cleaned (normalized) data
			username =form.cleaned_data['username']
			password =form.cleaned_data['password']

		if admin_name==username and admin_password==password:
			question_set=Question.objects.all()
			return render(request,"quiz/admin.html",{"question_set":question_set})
		
		else:
			return HttpResponse("Incorrect password or admin name")




#------admin page view using generic views



class QuestionCreate(CreateView):
	model=Question
	fields=['question_no','question_text','option1','option2','option3','option4','option5','answer1']

class QuestionUpdate(UpdateView):
	model= Question
	fields=['question_no','question_text','option1','option2','option3','option4','option5','answer1']

class QuestionDelete(DeleteView):
	model=Question
	success_url=reverse_lazy('quiz:simple_admin')


#-------------------detail view

def detail(request,pk):
	question=Question.objects.get(pk=pk)
	return render(request,'quiz/detail.html',{"question":question})



#---------- for the viewing the results

def results(request):
	result_objects=Result.objects.all()
	return render(request,'quiz/result_table.html',{'result_objects':result_objects})











