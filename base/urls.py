from django.urls import path
from .views import TaskList ,TaskDetail,update_post
from django.views.generic import TemplateView
from .import views
from .views import repost
urlpatterns = [
   path('',TemplateView.as_view(template_name='base/task.html'),name="task"),
   path('home/',views.TaskList.as_view(),name="list"),
   path('home/<int:smpl_id>/',TaskDetail.as_view(),name="detail"),#,name="task-detail"
      path('home/<int:prk>/update',update_post.as_view(),name="update"),#,name="task-detail"

    path('home/create/',repost,name="create"),
    
    
]









#https://www.youtube.com/watch?v=k1QDS02gwws&list=PLEt8Tae2spYl6czLxMCC01dM--CtOw2Sy&ab_channel=SsaliJonathan

