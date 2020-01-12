from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """test api view """
    serilaizer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """ return the list of apiview features"""
        an_apiview =[
        'uses http methods as function (get,post,patch,put,delete)',
        'is similar to traditional django view ',
        'gives you the most control over your app logic',
        'is mapped manually to URLs'
        ]
        """return a dictionery in response which will be converted to json when response is delivered"""
        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        """ create a hello message with the input name"""
        """ the data from HelloSerializer of serializer class get passed in data field request.data"""
        serializer = self.serilaizer_class(data=request.data)

        """ check data received is calid """
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            """ f string is used to insert variable into string"""
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            """if input is not valid return 400:bad request response"""
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """ pk is primary key : id of object to be updated"""
        """ handle updating an object """
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ handle partial update of object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """ delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSets(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset =[
        'uses actions list, create, retrieve,upadte partial update',
        'automatically maps to url using routers',
        'provides more functionality with less code'

        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """pk is for primary key
        handle getting object by its id """
        return Response({'method':'GET'})

    def update(self,request,pk=None):
        """pk is for primary key
        handle UPDATING object by its id """
        return Response({'method':'PUT'})

    def partial_update(self,request,pk=None):
        """pk is for primary key
        handle UPDATING part of an object by its id """
        return Response({'method':'PATCH'})

    def destroy(self,request,pk=None):
        """handle deleting an object"""
        return Response({'method':'DELETE'})


class UserProfileViewSets(viewsets.ModelViewSet):
    """ handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User_Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
