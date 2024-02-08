from rest_framework import serializers


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField()

    class Meta:
        ref_name = "VerifyCodeEmailSerializer"
