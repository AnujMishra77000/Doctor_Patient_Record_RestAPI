from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_auth.api.views import Regustration_view,logout_view


urlpatterns = [
    path('register/',Regustration_view, name='Register'),
    path('login/', obtain_auth_token, name='logi'),
    path('logout/',logout_view, name='logout'),
    
]