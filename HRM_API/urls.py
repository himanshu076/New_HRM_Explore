from django.urls import path
from HRM_API import views


urlpatterns = [
    # Authentication Routes
    path('home', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='reg'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),

    path('about/', views.About.as_view(), name='about'),

]
