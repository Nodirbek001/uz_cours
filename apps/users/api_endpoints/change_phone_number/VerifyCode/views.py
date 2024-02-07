from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from apps.users.api_endpoints.change_phone_number.VerifyCode.serializers import VerifyCodeSerializer


class VerifyCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(request_body=VerifyCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        given_code = serializer.validated_data['code']
        cache_data = cache.get(user.id, None)
        if cache_data is None:
            return Response(data={"error": _("Verify code is expired")}, status=status.HTTP_400_BAD_REQUEST)
        if given_code != cache_data["code"]:
            return Response(data={"error": _("Verify code is incorrect")}, status=status.HTTP_400_BAD_REQUEST)
        user.phone_number = cache_data["phone_number"]
        user.username = user.phone_number
        user.save()
        return Response(data={"massage": _("Your phone number changed successfully")}, status=status.HTTP_200_OK)


__all__ = ['VerifyCodeAPIView']
