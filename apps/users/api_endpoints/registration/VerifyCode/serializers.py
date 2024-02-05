from rest_framework import serializers




class VerifyCodeSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField()
    session = serializers.CharField(max_length=32)
    code = serializers.CharField(max_length=6)

    class Meta:
        ref_name: "VerifyCodeRegistrationSerializer"
