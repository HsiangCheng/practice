# --coding: utf-8--
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from webuser.models import *

class IsOwnerPermission(permissions.BasePermission):
    # 对象级权限
    # 检查user是不是创建者

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsOwnerOrViewerPermission(permissions.BasePermission):
    pass

class IsUserPermission(permissions.BasePermission):
    # 对象级权限
    # 检查user是不是关联者

    def has_object_permission(self, request, view, obj):

        return (
            request.user and
            request.user.is_authenticated() and
            obj.user == request.user
        )

class IsHr(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated() and
            request.user.groups.filter(name='hr').exists()
        )

class IsHrOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user.is_authenticated() and
            request.user.groups.filter(name='hr').exists()
        )

class IsHrOrOwner(IsHr):
    def has_object_permission(self, request, view, obj):
        return (
            super(IsHrOrOwner, self).has_permission(request, view) or
            obj.owner.user == request.user
        )

class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated() and
            request.user.groups.filter(name='student').exists()
        )

