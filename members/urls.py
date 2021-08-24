from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_profile,register
from .import views

urlpatterns = [

   path('login/', LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
        path('profile/', user_profile, name='profile'),
          path('about/',views.about_page,name="about"),
           path('register/',register,name="register"),
        
]