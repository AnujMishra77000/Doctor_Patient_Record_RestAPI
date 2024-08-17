from django.urls import path
from PD.API.views import (Doctors_List,Perticular_doctor,PeitentList,
                           Perticular_Peitent, Record_peitent,Perticular_Pet_Record,
                           All_department,doctors_by_department,Pateint_by_department)


urlpatterns = [
     path('doctors/',Doctors_List.as_view()),
     path('perticular/<int:pk>/', Perticular_doctor, name='perticular_doct'),
     path('peitent/',PeitentList.as_view()),
     path('peitent/<int:pk>/',Perticular_Peitent, name='Perticular_peit'),
     path('pet_record/',Record_peitent.as_view()),
     path('perticular_pet_rec/<int:pk>/',Perticular_Pet_Record, name='perticular_record'),
     path('all_department/', All_department.as_view()),
     path('dr_by_dprtmnt/<int:pk>/',doctors_by_department, name='dr_by_dept'),
     path('Pnt_by_dept/<int:pk>/', Pateint_by_department, name='patient_by_department')
]

