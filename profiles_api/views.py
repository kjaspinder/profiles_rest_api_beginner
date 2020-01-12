from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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
