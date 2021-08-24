from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from django.contrib  import  messages 
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from  .models import Post
from .forms import Postnote
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.contrib.auth.models import User


        




def repost(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     return Http404 
    if request.method == 'POST':
       form=Postnote(request.POST,request.FILES)
       if form.is_valid():
           instance=form.save()
           instance.user=request.user
           messages.success(request,"successfully created")
           return redirect('/home/')
           
           

    else:
        print("text here")
          
     
     
        form=Postnote()
    return render(request,"base/create.html",{'form':form})
   
# @login_required   
class TaskList(LoginRequiredMixin,ListView):
    model =Post
    template_name="base/task_list.html"
    
class TaskDetail(LoginRequiredMixin,DetailView):
    
    context_object_name="obj"
    template_name='base/detail.html'
    model=Post

    # context_object_name='name'
    # success_message = "Facture mise à jour avec succes"
    def get_object(self):
         print(self.kwargs)
         pk = self.kwargs.get("pk")

         return get_object_or_404(Post, id=pk)
         
    
    # def get_context_data(self, **kwargs) :
    #     context= super().get_context_data(**kwargs)
    #or context=super(Task,self).get_context_data(**kwargs)
    #     context['Task_list']=Task.objects.all()
    #     return context
    
#, UserPassesTestMixin learn about this later
class update_post(LoginRequiredMixin,UpdateView):
     model=Post
     
     form_class =Postnote
     template_name="base/update_post.html"
    #  fields=['title','field','content','comment']
     success_url='/home/1'
     
     def get_object(self):
         print(self.kwargs)
         pk = self.kwargs.get("pk")
         return get_object_or_404(Post, id=pk)
     
    #  def test_func(self):
    #        contact = self.get_object()
    #        if self.request.user == contact.user:
    #         return True
    #         return False
    
    
# class TaskDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    
#     context_object_name="obj"
#     template_name='base/post_confirm_delete.html'
#     model=Post
    
#     def test_func(self):
        
#         post=self.get_object()
#         if self.request.user == post.user:
#             return True 
#         else:
#             return False
        
        
        
        
    # context_object_name='name'
    # success_message = "Facture mise à jour avec succes"
    # def get_object(self):
    #      print(self.kwargs)
    #      id = self.kwargs.get("id")
    #      return get_object_or_404(Post, id=id)
     
#     def get_success_url(self):
#          return reverse('base:home')
@login_required
def post_delete_view(request,pk):
    obj=get_object_or_404(Post, id=pk)
  
    
    if request.method== "POST":
        obj.delete()
        return redirect("/home")
    context={"obj":obj}
    
    return render(request,"base/post_confirm_delete.html",context)








