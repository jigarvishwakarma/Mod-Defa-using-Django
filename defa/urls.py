"""mod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



app_name ='defa'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('list/', views.list_view,name='list'),
    path('addvideo/',views.addvideo,name='addvideo'),
    path('submitvideo/',views.submitvideo,name='submitvideo'),
    path('deletevideo/<int:deleteid>/',views.deletevideo,name='deletevideo'),
    path('deleteallvideo/',views.deleteallvideo,name='deleteallvideo'),
    #path('//',views.home,name='home'),
    #path('create',views.create_app,name='create'),
    #path('home/',views.home_app),
    #path('sv/',views.singlevideo_view,name='sv'),
    #path('books/',views.book_list,name='book_list'),
    #path('edit/',views.editfun,name='edit'),
    #path('listedit/',views.listedit,name='listedit'),
    path('books/upload/',views.upload_book,name='upload_list'),
    
   
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
