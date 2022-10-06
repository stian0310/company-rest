from rest_framework import serializers

from API.models import Enterprise


class EnterpriseSerializer(serializers.ModelSerializer):

  class Meta:
    model = Enterprise
    fields = [
      'id',
      'name',
      'address',
      'nit',
      'phone',
      'created_at',
      'updated_at',
    ]
