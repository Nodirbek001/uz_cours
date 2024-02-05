from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from apps.users.api_endpoints.registration.SetPassword.serializers import SetPasswordSerializer
from apps.users.models import CustomUser


class SetPasswordAPIView(APIView):
    @swagger_auto_schema(request_body=SetPasswordSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        session = serializer.validated_data['session']
        password = serializer.validated_data['password']

        session_data = cache.get(session, None)
        print(session_data)
        if session_data is None:
            return Response(data={"error": _("Invalid session")}, status=status.HTTP_400_BAD_REQUEST)
        is_verified = session_data.pop('is_verified', None)
        if is_verified is None:
            return Response(data={"error": _("User is not virefied")}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser(**session_data)
        user.set_password(password)
        user.save()
        print("token")
        print(user.get_tokens())
        session_data.update(user.get_tokens())

        return Response(data=session_data, status=status.HTTP_200_OK)
