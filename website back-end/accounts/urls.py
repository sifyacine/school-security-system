from django.urls import path
from accounts.views import login_view, signup_view, logout_view
from django.contrib.auth.views import LoginView
from django.contrib import admin

name1 = 'login'
name2 = 'signup'
name3 = 'logout'
name4 = 'admin_login'

urlpatterns = [
    path('login/', login_view, name=name1),
    path('signup/', signup_view, name=name2),
    path('logout/', logout_view, name=name3),
    path('admin/', admin.site.urls),
    path('admin/login/', LoginView.as_view(template_name='admin_login.html'), name=name4),
]