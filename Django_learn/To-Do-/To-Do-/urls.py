"""
URL configuration for Booktore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import task_list, task_create, task_update, task_delete 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    path('about/',views.about,name='About'),
    path('contact/',views.contact,name='Contact'),
    path('Books/',include('Books.urls')),
    path('', task_list, name='task_list'), path('create/', task_create, name='task_create'), path('update/<int:pk>/', task_update, name='task_update'), path('delete/<int:pk>/', task_delete, name='task_delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


