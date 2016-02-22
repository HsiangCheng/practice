# --coding: utf-8--
from rest_framework import renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class AuthTokenView(ObtainAuthToken):
    renderer_classes = (
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
    )
    def post(self, request, *args, **kwargs):
        """
        ---
        serializer: rest_framework.authtoken.serializers.AuthTokenSerializer
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        groups = list()
        for group in user.groups.all():
            groups.append(str(group))
        return Response(
            {
                'token': token.key,
                'username': user.username,
                'groups': groups,
            }
        )

# class APIRootView(APIView):
#     def get(self, request):
#         data = {
#             'account-root':
#                 reverse(
#                     'api:v1:account:account-root',
#                     request=request
#                 ),
#             'student-root':
#                 reverse(
#                     'api:v1:student:student-root',
#                     request=request
#                 ),
#             'hr-root':
#                 reverse(
#                     'api:v1:hr:hr-root',
#                     request=request
#                 ),
#         }
#         return Response(data)