from rest_framework.decorators import api_view
from user_auth.api.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_auth import models
from rest_framework import status


@api_view(['POST'])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HHTP_200_OK)


@api_view(['POST',])
def Regustration_view(request):
    if request.method=='POST':
        serializer=RegisterSerializer(data=request.data)

        data={}

        if serializer.is_valid():
            account=serializer.save()

            data['response']="Registration is successfull"
            data['username']=account.username
            data['email']=account.email

            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)  
     

