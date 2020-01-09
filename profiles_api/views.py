from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view """

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
