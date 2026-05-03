# Chapter 19 — User Accounts
# Adds login, logout, registration, and data ownership to the Learning Log app.

# --- Include Django's built-in auth URLs (ll_project/urls.py) ---
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('django.contrib.auth.urls')),  # login/logout built-in
#     path('', include('learning_logs.urls')),
# ]

# --- Login template (templates/registration/login.html) ---
# {% extends "learning_logs/base.html" %}
#
# {% block content %}
#   <form action="{% url 'login' %}" method='post'>
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button name="submit">Log in</button>
#     <input type="hidden" name="next" value="{% url 'learning_logs:index' %}" />
#   </form>
# {% endblock content %}

# --- Restrict views with @login_required ---
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def topics(request):
#     topics = Topic.objects.filter(owner=request.user).order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'learning_logs/topics.html', context)
#
# # Set redirect for unauthenticated users (settings.py):
# LOGIN_URL = '/accounts/login/'

# --- Registration view (users/views.py) ---
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
#
# def register(request):
#     if request.method != 'POST':
#         form = UserCreationForm()
#     else:
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             login(request, new_user)   # log in immediately after registration
#             return redirect('learning_logs:index')
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

# --- Add ownership to Topics (learning_logs/models.py) ---
# from django.contrib.auth.models import User
#
# class Topic(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#
# # Migration will ask for a default — use option 1, then enter 1 (superuser id)

# --- Protect data: verify ownership in views ---
# from django.http import Http404
#
# def topic(request, topic_id):
#     topic = Topic.objects.get(id=topic_id)
#     if topic.owner != request.user:
#         raise Http404                  # don't reveal the topic exists at all
#     ...

# --- Forms (learning_logs/forms.py) ---
# from django import forms
# from .models import Topic, Entry
#
# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ['text']
#         labels = {'text': ''}
#
# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text': ''}
#         widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# --- Key ideas ---
# 1. django.contrib.auth.urls gives you login/logout for free — just include them
# 2. @login_required redirects unauthenticated users to LOGIN_URL
# 3. Always filter by owner: Topic.objects.filter(owner=request.user)
# 4. raise Http404 is safer than a 403 — it doesn't reveal the resource exists
# 5. {% csrf_token %} is required in every POST form — prevents cross-site forgery

print("Chapter 19: See the comments above for user accounts and data ownership.")
