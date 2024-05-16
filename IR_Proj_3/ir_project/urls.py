"""
URL configuration for Assignment_4_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ir_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.file_upload_view, name='home'),
    path('upload/', views.file_upload_view, name='file_upload'),
    path('search-results/', views.search_results_test, name='search_results'),
    path('display_doc/<int:doc_id>/', views.display_doc_test, name='display_doc'),
    path('reset/', views.reset_database, name='reset_database'),
    path('show_pdf/<str:query>/', views.show_pdf, name='show_pdf'),
]
