from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.owner.id


# class IsOwnerOrReadOnly(permissions.BasePermission):
# 	"""
# 	Custom permission to allow owner of an object to edit it.
# 	"""
# 	def has_object_permission(self, request, view, obj):
# 		# Read permissions are allowed for any object
# 		# Request allowed - GET, HEAD, or OPTIONS
# 		# Write permissions are allowed to creater only
# 		if request.method in permissions.SAFE_METHODS:
# 			return True

# 		return obj.owner == request.user


# class IsAuthenticated(permissions.BasePermission):
# 	"""To allow access to the authenticated users only"""
# 	def has_permission(self, request, view):
# 		message = 'Authenticated users allowed only'
# 		status = bool(request.user and request.user.is_authenticated)
# 		if status:
# 			return status
# 		else:
# 			raise PermissionDenied(detail=message)