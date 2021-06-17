from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.views.generic import DetailView, UpdateView, CreateView
from VBlog.models import Profile, TrendingEmailNotification, Post, Categories
from django.urls import reverse_lazy, reverse
from django import forms
from VBlog.forms import ProfilePageForm, UpdateProfilePageForm, SignupForm,LoginForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Count, Sum, Value as V
from django.db.models.functions import Coalesce

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have registered successfully!')
            return redirect('login') 


    else:
        form = SignupForm()
    return render(request, 'accounts/register.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.success(request,'Logged out Successfully!')
    return redirect("home")

def dashboard(request):
    # return render(request, 'accounts/dashboard.html')
    return render(request, 'home.html')

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    auth.login(request, user)
                    messages.success (request,'Logged in successfully')
                    return redirect('home')
        else:
            form=LoginForm()
        return render(request,'accounts/login.html',{'form':form})
    else:
         return HttpResponseRedirect('/home')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'accounts/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        categories_count = []
        users = Profile.objects.all()
        month_list = [0,0,0,0,0,0,0,0,0,0,0,0]
        context = super (ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        categories = Categories.objects.filter(created_by_id = self.kwargs['pk'])
        grouping = Post.objects.filter(author_id = self.kwargs['pk']).extra({'month':"Month(published_date)"}).values('month').annotate(created_count=Count('id')).order_by('month')
        for i in grouping:
            month_list[i['month']-1] = i['created_count']
        for category in categories:
            categories_count.append(Post.objects.filter(Categories__icontains=category).count())
        context["page_user"] = page_user
        posts = Post.objects.filter(author_id = self.kwargs['pk']).order_by("-published_date")
        context["posts"] = posts
        context["categories"] = categories
        context["count"] = categories.count()
        categories_count.reverse()
        context["categories_count"] = categories_count
        context['month_list'] = month_list
        return context

class EditProfilePageView(UpdateView):
    model=Profile
    template_name='accounts/edit_profile_page.html'
    form_class = UpdateProfilePageForm
    success_url = reverse_lazy('home')
    
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name='accounts/create_user_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('home')
