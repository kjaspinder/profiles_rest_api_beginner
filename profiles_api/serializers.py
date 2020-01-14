from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """serilaizes the name field for testing out apiview"""
    """accept name of max 10 char"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    class Meta:
        model = models.User_Profile
        fields = ('id','email','name','password')
        extra_kwargs = {
        'password': {'write_only':True,
                    'style':{'input_type':'password'}
                    }

        }

    def create(self,validated_data):
        """create and return the new user"""
        user = models.User_Profile.objects.create_user(email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
                )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ serializes profile feed item """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {
            'user_profile':{'read_only':True
            }
        }
