from django.urls import path
from authapp.views import edit, Dashboard, register, privacy
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'authapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('privacy/', privacy, name='privacy'),
    path('edit/', edit, name='edit'),
    path('dashboard/', login_required(Dashboard.as_view(), login_url='authapp:login'), name='dashboard'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html',success_url=reverse_lazy('authapp:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),

]