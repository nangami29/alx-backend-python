from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    def has_permission(self, request, view):
       if request.user.is_authenticated:
           return True
       else:
           return False
    def has_object_permission(self, request, view, obj):
        if request.user in obj.participants.all():
            return True
        else:
            return False
   