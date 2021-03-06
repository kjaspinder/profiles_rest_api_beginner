from rest_framework import permissions

class updateOwnProfile(permissions.BasePermission):
    """ allow users to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """ check user is trying to edit its own profile"""
        """ safe method is get method that does not make any change in model db"""
        if request.method in permissions.SAFE_METHODS:
            return True

            """ check if the profile user is updating is authenticated login profile"""
            """ obj is the object user trying to update"""
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ allow users to update own status """

    def has_object_permission(self,request,view,obj):
        """ check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
