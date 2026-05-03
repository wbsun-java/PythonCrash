# Chapter 18 — Getting Started with Django
# Install first: pip install django
# All commands run from the project directory.

# --- Create a new Django project and app ---
# django-admin startproject ll_project .    # '.' puts manage.py in current dir
# python manage.py startapp learning_logs

# --- settings.py: register your app ---
# INSTALLED_APPS = [
#     'learning_logs',         # add your app here
#     'django.contrib.admin',
#     ...
# ]

# --- Define a model (learning_logs/models.py) ---
# from django.db import models
#
# class Topic(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text
#
# class Entry(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         return f"{self.text[:50]}..."

# --- Apply migrations ---
# python manage.py makemigrations learning_logs
# python manage.py migrate

# --- Register models in admin.py ---
# from django.contrib import admin
# from .models import Topic, Entry
#
# admin.site.register(Topic)
# admin.site.register(Entry)

# --- Create superuser ---
# python manage.py createsuperuser

# --- URL routing (ll_project/urls.py) ---
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('learning_logs.urls')),
# ]

# --- App-level URL (learning_logs/urls.py) ---
# from django.urls import path
# from . import views
#
# app_name = 'learning_logs'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('topics/', views.topics, name='topics'),
#     path('topics/<int:topic_id>/', views.topic, name='topic'),
# ]

# --- Views (learning_logs/views.py) ---
# from django.shortcuts import render
# from .models import Topic
#
# def index(request):
#     return render(request, 'learning_logs/index.html')
#
# def topics(request):
#     topics = Topic.objects.order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'learning_logs/topics.html', context)
#
# def topic(request, topic_id):
#     topic = Topic.objects.get(id=topic_id)
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'learning_logs/topic.html', context)

# --- Template (learning_logs/templates/learning_logs/topics.html) ---
# {% extends "learning_logs/base.html" %}
#
# {% block content %}
#   <ul>
#     {% for topic in topics %}
#       <li><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></li>
#     {% empty %}
#       <li>No topics yet.</li>
#     {% endfor %}
#   </ul>
# {% endblock content %}

# --- Key ideas ---
# 1. Project = config container. App = one feature (e.g., learning_logs, users)
# 2. Models → makemigrations → migrate — three steps every time you change a model
# 3. ForeignKey with CASCADE: deleting a Topic deletes all its Entries
# 4. context dict passed to render() becomes available in the template
# 5. {% url 'app_name:view_name' arg %} generates URLs — never hardcode paths

print("Chapter 18: See the comments above for Django project/model/view patterns.")
print("Run: django-admin startproject ll_project .")
