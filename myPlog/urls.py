from django.urls import path
from .views import TaskList ,TaskDetail,update_post,post_delete_view
from django.views.generic import TemplateView
from .import views
from .views import repost


urlpatterns = [
   path('',TemplateView.as_view(template_name='base/task.html'),name="task"),
   path('home/',views.TaskList.as_view(template_name='base/task_list.html'),name="home"),
   path('home/<int:pk>/',TaskDetail.as_view(template_name='base/detail.html'),name="detail"),
   path('home/<int:pk>/delete/',post_delete_view,name="delete"),
      path('home/<int:pk>/update/',update_post.as_view(),name="update"),

    path('home/create/',repost,name="create"),
   
       

      #   path('login/',views.login_user,name="login"),
  


    
    
]


#https://www.youtube.com/watch?v=k1QDS02gwws&list=PLEt8Tae2spYl6czLxMCC01dM--CtOw2Sy&ab_channel=SsaliJonathan
