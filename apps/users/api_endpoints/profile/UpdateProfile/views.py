from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.users.api_endpoints.profile.UpdateProfile.serializers import UpdateProfileSerializer


class UpdateProfileAPIView(UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user


__all__ = ['UpdateProfileAPIView']
