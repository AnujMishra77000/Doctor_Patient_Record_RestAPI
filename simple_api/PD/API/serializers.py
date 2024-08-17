from rest_framework import serializers
from PD.models import models, Department, Petient_Record, Doctors

class DepartmentSerializer(serializers.ModelSerializer):
     class Meta:
       model= Department
       fields = '__all__'

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctors
        fields = '__all__'

class PetientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Petient_Record
        fields = '__all__'

