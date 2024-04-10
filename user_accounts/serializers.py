from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerilizer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model Account
        fields = "__all__"