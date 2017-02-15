from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^data/$', views.process_data,name='process_data'),
  	url(r'^register/$',views.RegistrationView.as_view(), name='registration'),

  	#urls for the admin inteface

  	url(r'^simple_admin/$',views.AdminLoginView.as_view(), name='simple_admin'),
  	url(r'^simple_admin/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
  	url(r'^simple_admin/add/$', views.QuestionCreate.as_view(), name='add_question'),
  	url(r'^simple_admin/update/(?P<pk>[0-9]+)/$', views.QuestionUpdate.as_view(), name='update_question'),
  	url(r'^simple_admin/delete/(?P<pk>[0-9]+)/$', views.QuestionDelete.as_view(), name='delete_question'),
  	url(r'^simple_admin/results/$', views.results, name='results'),

]
