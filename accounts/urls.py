from django.urls import path, re_path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),

    path('reset_password/',
         PasswordResetView.as_view(template_name='accounts/reset_password.html',
                                   email_template_name='accounts/reset_password_email.html',
                                   success_url=reverse_lazy('accounts:password_reset_done'),
                                   ),
         name='password_reset'),

    path('reset_password/done/',
         PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
         name='password_reset_done'),

    path('reset_password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html',
                                          success_url=reverse_lazy('accounts:password_reset_complete')
                                          ),
         name='password_reset_confirm'),

    path('reset_password/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),
         name='password_reset_complete')
]