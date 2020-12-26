"""produtos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import produto_new
from .views import produto_list
from .views import produto_update
from .views import produto_delete

urlpatterns = [
    path('list/', produto_list, name="produto_list"),
    path('new/', produto_new, name="produto_new"),
    path('update/<int:id>/', produto_update, name="produto_update"),
    path('delete/<int:id>/', produto_delete, name="produto_delete")
]