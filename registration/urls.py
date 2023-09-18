from django.urls import path
from registration.views import RegisterView
from .views import temview,signup
from django.contrib.auth import views as auth_Views
urlpatterns = [
    path('register',RegisterView.as_view(),name="api"),
    path('temp',temview,name='site'),
    path('signup',signup,name="signup"),
    path('login',auth_Views.LoginView.as_view(template_name="login.html"),name="login"),
    path('logout',auth_Views.LogoutView.as_view(),name="logout"),
    path('settings/changepassword',auth_Views.PasswordChangeView.as_view
         (template_name="changepassword.html"),name="changepassword"),
    path('settings/changepassword/done',auth_Views.PasswordChangeDoneView.as_view
         (template_name="changepassworddone.html"),name="changepassworddone"),     
] 