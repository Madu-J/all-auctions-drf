from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AccountSerializer
from .models import Account
from django.db.models import Count


class AccountList(APIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.annotate(
        allauctions_count=Count("owner__allauctions", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__following__followed__profile",
        "owner__followed__owner__profile",
    ]
    ordering_fields = [
        "allauctions_count",
        "followers_count",
        "following_count",
        "owner__following__created_at",
        "owner__followed__created_at",
    ]


class AccountDetails(RetrieveUpdateAPIview):
    """
    Retrieve, edit or delete user account.
    """
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.annotate(
        allauctions_count=Count("owner__allauctions", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
