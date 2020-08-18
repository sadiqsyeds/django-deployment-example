from django.urls.conf import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('',views.home,name='index'),
    path('register',views.register, name='register'),
    path('login',views.user_login, name='login'),
    path('logout',views.user_logout, name='logout'),
]