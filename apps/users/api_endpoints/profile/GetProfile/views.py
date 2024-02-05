from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.GetProfile.serializers import GetProfileSerializer


class GetProfileAPIView(RetrieveAPIView):
    serializer_class = GetProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=GetProfileSerializer)
    def get_object(self):
        return self.request.user


__all__ = ['GetProfileAPIView']
