from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.loginuser, name='login'),
    path('register/', views.register_post, name='register'),
    path('loan_request/', views.loan_request, name='loan_request'),
    path('view_loan_requests/', views.view_loan_requests, name='view_loan_requests'),
    path('create_loan_request/', views.create_loan_request, name='create_loan_request'),
    path('lender_dashboard/', views.give_loan, name='lender_dashboard')

]

# from django.urls import path
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/', views.loginuser, name='login'),
#     path('register/', views.registeruser, name='register'),  # Route for GET requests to /register
#     path('register/', views.register_post, name='register_post'),  # Route for POST requests to /register
#     path('loan_request/', views.loan_request, name='loan_request'),
#     path('view_loan_requests/', views.view_loan_request, name='view_loan_requests'),
#     # Other URL patterns
# ]