from django.urls import path
from . import views  # Import your views from the current app
from .views import get_all_assessments,get_all_patients,DevelopmentalTask,get_assessments,pediatric_assessment_list,get_patients_report, register_referral_doctor, get_referral_doctors
urlpatterns = [
    path('register/', views.create_registration, name='register'),  # For patient registration
    path('next-registration-number/', views.get_latest_registration_number, name='next_registration_number'),
    path('all-assessments/', get_all_assessments, name='all-assessments'),
    path('all-patients/', get_all_patients, name='all-patients'),
    path('save-assessments/', views.save_assessments, name='save-assessments'),
    # path('empregister/',views.registerView,name='RegisterView'),
    path('login/',views.LoginView,name='LoginView'),
    path('developmental-tasks/', DevelopmentalTask, name='DevelopmentalTask'),
    path('get-assessments/', get_assessments, name='get-assessments'),
    path('pediatric-assessment/',views.PediatricAssessment, name='pediatric-assessment'),
    path('save-patient-skill/', views.save_patient_skilltest, name='save-patient-skill'),
    path('pediatric_assessment_list/', pediatric_assessment_list, name='pediatric_assessment_list'),
    path('reg_no/<str:prefix>/<str:id>/<str:year>/', views.get_patient_by_registration, name='get_patient_by_registration'),
    path('all-patients/', get_patients_report, name='pediatric_assessment_list'),
    path('therapy_billing/', views.therapy_billing, name='therapy_billing'),
    path('therapybillinggetall/', views.therapybillinggetall, name='therapybillinggetall'),
    path('pendingPayment/', views.pendingPayment, name='pendingPayment'),
    path('updatePayment/', views.update_payment, name='update_payment'),
    path('get-latest-billing-no/', views.get_latest_billing_no,name='get_latest_billing_no'),
    path('employeeregistration/', views.employeeregistration,name='employeeregistration'),
    path('get_patient_assessments/', views.get_patient_assessments, name='get_patient_assessments'),
    path('referrals/', views.get_referrals, name='get_referrals'),
    path('therapy-reports/', views.get_therapy_reports, name='therapy-reports'),
    path('save-mchat-response/', views.saveMCHATResponses, name='save-mchat-response'),
    path('get-mchat/<path:registration_number>/', views.getMCHATResponse, name='get-mchat-response'),
    path("referral-doctor/register/", register_referral_doctor, name="register-referral-doctor"),
    path("referral-doctor/list/", get_referral_doctors, name="list-referral-doctors"),
]
