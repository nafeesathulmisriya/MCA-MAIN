from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from insurance import views as insurance_views 



urlpatterns = [
    # Authentication & Dashboard
    path('customerclick', views.customerclick_view, name='customerclick'),
    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view, name='customer-dashboard'),
    path('customerlogin', LoginView.as_view(template_name='insurance/adminlogin.html'), name='customerlogin'),

    # Claims Management
    path('upload_claim', views.upload_claim, name='upload_claim'),
    path('claim_success/', views.claim_success, name='claim_success'),  # ✅ Added missing success URL
    path('my-claims/', views.my_claims, name='my-claims'),
    path("claim-status/", views.claim_status, name="claim_status"),
    
    
    # Admin Claims Management
    path("claims/", insurance_views.claim_list_admin, name="claim_list_admin"),
    path("admin/claims/", insurance_views.claim_list_admin, name="claim_list_admin"),
    path('claims/update/<int:claim_id>/<str:new_status>/', insurance_views.update_claim_status, name='update_claim_status'),
    





    # Policies
    path('apply-policy', views.apply_policy_view, name='apply-policy'),
    path('apply/<int:pk>', views.apply_view, name='apply'),
    path('history', views.history_view, name='history'),
    path('policy-categories/', views.customer_view_categories, name='policy-categories'),

    # Questions & Contact
    path('ask-question', views.ask_question_view, name='ask-question'),
    path('question-history', views.question_history_view, name='question-history'),
    path('contactus', insurance_views.contactus_view, name='contact'),
    path("contactsuc/", insurance_views.contactus_success_view, name="contactussuccess"),

    # Success Pages

    path('success-page/', views.success_view, name='success-page'),





   






]
