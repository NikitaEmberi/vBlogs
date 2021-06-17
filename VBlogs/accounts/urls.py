from django.urls import path
from . import views
from .views import ShowProfilePageView, EditProfilePageView, CreateProfilePageView, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout_request,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('<int:pk>/profile',ShowProfilePageView.as_view(),name="show_profile_page"),
    path('<int:pk>/edit_profile_page',EditProfilePageView.as_view(),name="edit_profile_page"),
    path('create_profile_page/',CreateProfilePageView.as_view(),name="create_profile_page"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html')),
#    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/',PasswordsChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
]
