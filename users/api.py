
from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers

from knox.models import AuthToken
from knox import views as knox_views
from rest_framework.response import Response


from .serializers import LoginSerializer, UserSerializer


class LoginApiView(generics.GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer._validated_data
        token = AuthToken.objects.create(user)[1]
        return Response(
            {
                'username' : UserSerializer(user, context=self.get_serializer_context()).data,
                'token' : token
            }
        )
 
class UserApiView(generics.GenericAPIView):
     serializer_class = UserSerializer
     permission_classes = (permissions.IsAuthenticated,)


     def get_queryset(self): 
        user = self.request.user
        return user

     def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        return Response(
             self.serializer_class(queryset, context=self.get_serializer_context()).data,
         )  
