from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from API.models import Enterprise
from API.serializers import EnterpriseSerializer

class EnterpriseView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
