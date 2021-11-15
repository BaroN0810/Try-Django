"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from accounts.views import (
    login_view,
    logout_view,
    register_view
)
from .view import home_view
from stockdata.views import (
    search_stock_view,
    create_stock_view,
    detail_stock_view
)

urlpatterns = [
    path('', home_view),  # Index / Home page
    path('login/', login_view),  # LoginView
    path('logout/', logout_view),  # LogoutView
    path('register/', register_view),  # RegisterView
    path('stockdata/', search_stock_view),  # SearchStockView
    path('stockdata/create/', create_stock_view),  # CreateStockView
    path('stockdata/<str:stock_title>', detail_stock_view),  # Each stock page
    path('admin/', admin.site.urls),
]

LOGIN_URL = '/login/'
