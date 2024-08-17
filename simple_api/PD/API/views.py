from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from PD.models import Petient_Record, Department, Doctors
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from PD.API.serializers import (DepartmentSerializer,DoctorsSerializer, PetientSerializer)
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

#it gives proper doctor list
class Doctors_List(APIView):
 permission_classes=[IsAuthenticated]
 def get(self, many=True):
        res=Doctors.objects.all()
        serializer=DoctorsSerializer(res,many=True)
        return Response(serializer.data)
 def post(self, request):
        serializer=DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
#it gives perticular doctor only
@api_view(['GET','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def Perticular_doctor(request, pk):
    if request.method =='GET':
       res=Doctors.objects.get(pk=pk)
       serializer=DoctorsSerializer(res)
       return Response(serializer.data)

    elif request.method =='PATCH':
        obj=Doctors.objects.get(pk=pk)
        serializer=DoctorsSerializer(obj, data=request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        obj=Doctors.objects.get(pk=pk)
        obj.delete()
        return Response({
          'message':'data deleted successfully',
          'status':'204'
        })
#it gives patitent Id and name only
class PeitentList(generics.ListCreateAPIView):
      queryset=Petient_Record.objects.all()
      serializer_class = PetientSerializer

#it gives perticular peitent contains only id name department
@api_view(['GET','PATCH','DELETE'])
def Perticular_Peitent(request, pk):
    if request.method =='GET':
       res=Petient_Record.objects.get(pk=pk)
       serializer=PetientSerializer(res)
       return Response(serializer.data)
    
    elif request.method =='PATCH':
        obj=Petient_Record.objects.get(pk=pk)
        serializer=PetientSerializer(obj,data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        obj=Petient_Record.objects.get(pk=pk)
        obj.delete()
        return Response({
          'message':'data deleted successfully',
          'status':'204'
        })
#it gives all pateint record
class Record_peitent(generics.ListCreateAPIView):
     queryset=Petient_Record.objects.all()
     serializer_class = PetientSerializer

#it gives perticular full patient record.
@api_view(['GET','PATCH','DELETE'])
def Perticular_Pet_Record(request, pk):
    if request.method =='GET':
       res=Petient_Record.objects.get(pk=pk)
       serializer=PetientSerializer(res)
       return Response(serializer.data)
    
    elif request.method =='PATCH':
        obj=Petient_Record.objects.get(pk=pk)
        serializer=PetientSerializer(obj,data=request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
       
    elif request.method == 'DELETE':
        obj=Petient_Record.objects.get(pk=pk)
        obj.delete()
        return Response({
          'message':'data deleted successfully',
          'status':'204'
        }) 
class All_department(generics.ListCreateAPIView): 
      queryset=Department.objects.all()
      serializer_class=DepartmentSerializer 

#get and update for doctors from perticular department
@api_view(['GET','PATCH'])
def doctors_by_department(request, pk):
    if request.method=='GET':
     try:
        department = get_object_or_404(Department,pk=pk) #Need to learn more about queryset
        drlist= Doctors.objects.filter(department=department)
        serializer = DoctorsSerializer(drlist,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     except Doctors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)      
     
    elif request.method == 'PATCH':
     try:
         res= Doctors.objects.get(pk= pk)
     except Doctors.DoesNotExist:
         return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
     serializer = DoctorsSerializer(res, data=request.data, partial=True)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)     
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PATCH'])
def Pateint_by_department(request, pk):
    if request.method=='GET':
      try:  
        department= get_object_or_404(Department, pk=pk)
        paient_list= Petient_Record.objects.filter(DepartmentId=department)
        serializer=  PetientSerializer(paient_list,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      except Petient_Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
      
    elif request.method == 'PATCH':
        try:
            res= Petient_Record.objects.get(pk=pk)
        except Petient_Record.DoesNotExist:
            return Response({"error":"Do not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer= PetientSerializer(res, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
