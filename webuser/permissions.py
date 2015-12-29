# --coding: utf-8--
from rest_framework import permissions
from webuser.models import *

class IsOwnerPermissions(permissions.BasePermission):
    # 对象级权限
    # 检查user是不是创建者

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsUserPermissions(permissions.BasePermission):
    # 对象级权限
    # 检查user是不是关联者

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        user_id = request.user.id


# class IsReadPermissions(permissions.DjangoModelPermissions):
#     # 检查是否有读取的权限
#
#     perms_map = {
#         'GET': ['%(app_label)s.read_%(model_name)s'],
#         'OPTIONS': ['%(app_label)s.read_%(model_name)s'],
#         'HEAD': ['%(app_label)s.read_%(model_name)s'],
#         'POST': [],
#         'PUT': [],
#         'PATCH': [],
#         'DELETE': [],
#     }