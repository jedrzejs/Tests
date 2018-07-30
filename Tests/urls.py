"""Tests URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.urls import path
from django.views.generic import TemplateView

from tests.views import AddTestView, AddTestFillInView, TestListView, AnswerTestView, AnswerFillInTestView, \
    AnswerListView, AnswerDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/<test_type>', AddTestView.as_view()),
    path('solve/', AddTestFillInView.as_view()),
    path('answer/<pk>', AnswerTestView.as_view()),
    path('answerfillin/<pk>', AnswerFillInTestView.as_view()),
    path('test_list/', TestListView.as_view()),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('choose/', TemplateView.as_view(template_name='tests/admin_test_choose.html')),
    path('answers/<pk>', AnswerListView.as_view()),
    path('answer_details/<pk>', AnswerDetailsView.as_view())
]
