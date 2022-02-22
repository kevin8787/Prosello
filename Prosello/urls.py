"""Prosello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from proselloapp import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('ownerhome/',views.ownerhome,name="ownerhome"),
    path('userhome/',views.userhome,name="userhome"),
    path('add_property/',views.add_property,name="add_property"),
    path('view_property/',views.view_property,name="view_property"),
    path('view_property_owner/',views.view_property_owner,name="view_property_owner"),
    # path('delete_property/',views.delete_property,name="delete_property"),
    path('update_property/<int:id>',views.update_property,name="update_property"),
    # path('update_property/',views.update_property,name="update_property"),
    path('my_property/',views.my_property,name="my_property"),
    path('delete_prpoerty/<int:id>',views.delete_property, name="delete_property_url"),
    path('delete_prpoerty_owner/<int:id>',views.delete_property_owner, name="delete_property_own"),
]
   
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

