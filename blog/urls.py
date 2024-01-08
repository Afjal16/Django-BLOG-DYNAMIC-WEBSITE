from django.urls import path
from blog import views

urlpatterns = [
    path('', views.INDEX, name='index'),
    path('about/', views.ABOUT, name='about'),
    path('contact/', views.CONTACT, name='contact'),
    path('blog_single/<str:slug>/', views.BLOG_SINGLE, name='blog_single'),
    path('search/', views.SEARCH, name='search'),
    path('all_blogs/', views.ALL_BLOGS, name='all_blogs'),
    path('register/', views.handleRegister, name='register'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='logout'),
    
]