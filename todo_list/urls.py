
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'myPlog'

urlpatterns = [
    path('', include('myPlog.urls')),
    # path('', include('django.contrib.auth.urls')), 
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)