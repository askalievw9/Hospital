from tkinter.font import names

from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'departments', DepartmentViewSet, basename='departments'),
router.register(r'specialty', SpecialtyViewSet, basename='specialty'),
router.register(r'patients', PatientViewSet, basename='patients'),
router.register(r'wards', WardViewSet, basename='wards'),
router.register(r'schedule', ScheduleViewSet, basename='schedule'),

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('doctors/', DoctorListAPIView.as_view(), name='doctors_list'),
    path('doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctors_detail'),
    path('doctors/create/', DoctorCreateAPIView.as_view(), name='doctors_create'),
    path('feedback/', FeedbackListAPIView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback_detail'),
    path('feedback/create/', FeedbackCreateAPIView.as_view(), name='feedback_create'),
    path('feedback/create/<int:pk>', FeedbackEditAPIView.as_view(), name='feedback_create_detail'),
    path('appointment/', AppointmentListAPIView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentDetailAPIView.as_view(), name='appointment_detail'),
    path('appointment/create/', AppointmentCreateAPIView.as_view(), name='appointment_create'),
    path('appointment/create/<int:pk>', AppointmentCreateAPIView.as_view(), name='appointment_create_detail'),
    path('medical_records/', MedicalRecordListAPIView.as_view(), name='medical_records_list'),
    path('medical_records/<int:pk>/', MedicalRecordDetailAPIView.as_view(), name='medical_records_detail'),
    path('medical_records/create/', MedicalRecordDetailAPIView.as_view(), name='medical_records_create'),
    path('medical_records/create/<int:pk>/', MedicalRecordDetailAPIView.as_view(), name='medical_records_create'),

]