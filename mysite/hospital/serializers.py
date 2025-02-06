from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        ref_name = "DJRestAuthLoginSerializer"

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учутные данные")


    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name']



class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'specialty_name',]


class SpecialtySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['specialty_name',]


class DoctorListSerializer(serializers.ModelSerializer):
    specialty = SpecialtySimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialty', 'work_day',]


class DoctorDetailSerializer(serializers.ModelSerializer):
    specialty = SpecialtySimpleSerializer(read_only=True, many=True)
    department = DepartmentSimpleSerializer()

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'department','shift_start',
                  'shift_start', 'shift_end', 'work_day',]


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'department','shift_start', 'role',
                  'shift_start', 'shift_end', 'work_day', 'experience', 'service_price']


class DoctorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name',]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientSimpleSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Patient
        fields = ['user',]


class AppointmentListSerializer(serializers.ModelSerializer):
    patient = PatientSimpleSerializer()
    doctor = DoctorSimpleSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor',]


class AppointmentDetailSerializer(serializers.ModelSerializer):
    patient = PatientSimpleSerializer()
    doctor = DoctorSimpleSerializer()

    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_tame', 'status']


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_tame', 'status']


class MedicalRecordListSerializer(serializers.ModelSerializer):
    patient = PatientSimpleSerializer()
    doctor = DoctorSimpleSerializer()

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication']


class MedicalRecordDetailSerializer(serializers.ModelSerializer):
    patient = PatientSimpleSerializer()
    doctor = DoctorSimpleSerializer()

    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']


class FeedbackListSerializer(serializers.ModelSerializer):
    patient = PatientSimpleSerializer()
    doctor = DoctorSimpleSerializer()

    class Meta:
        model = Feedback
        fields = ['id', 'doctor', 'patient', 'rating', 'comment']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    patient = PatientSimpleSerializer()
    doctor = DoctorSimpleSerializer()

    class Meta:
        model = Feedback
        fields = ['doctor', 'patient', 'rating', 'comment']


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['doctor', 'patient', 'rating', 'comment']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'doctor', 'day_of_week', 'start_time', 'end_time']

