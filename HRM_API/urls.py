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

    # Employee Routes
    path('dashboard/employee/all', views.Employee_All.as_view(), name='employee_all'),    
    path('dashboard/employee/new', views.Employee_New.as_view(), name='employee_new'),    
    path('dashboard/employee/view/', views.Employee_View.as_view(), name='employee_view'),

]
