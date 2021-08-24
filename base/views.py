from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from django.contrib  import  messages 
from django.views.generic import ListView,DetailView,UpdateView

from  .models import Post
from .forms import Postnote



def repost(request):
    if request.method == 'POST':
       form=Postnote(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           messages.success(request,"successfully created")
           return redirect('/home/')
           
           

    else:
        print("text here")
          
     
     
        form=Postnote()
    return render(request,"base/create.html",{'form':form})
   
    
class TaskList(ListView):
    model =Post
    template_name="base/task_list.html"
    
class TaskDetail(DetailView):
    
    context_object_name="obj"
    template_name='base/detail.html'
    model=Post
    
    # context_object_name='name'
    # success_message = "Facture mise à jour avec succes"
    def get_object(self):
         print(self.kwargs)
         smpl_id = self.kwargs.get("smpl_id")
         return get_object_or_404(Post, id=smpl_id)
         
    
    # def get_context_data(self, **kwargs) :
    #     context= super().get_context_data(**kwargs)
    #or context=super(Task,self).get_context_data(**kwargs)
    #     context['Task_list']=Task.objects.all()
    #     return context
    
    
class update_post(UpdateView):
     model=Post
     form_class =Postnote
     template_name="base/update_post.html"
    #  fields=['title','field','content','comment']
     success_url='/home/'
   
     

     
     def get_object(self):
         print(self.kwargs)
         prk = self.kwargs.get("prk")
         return get_object_or_404(Post, id=prk)
    
    
