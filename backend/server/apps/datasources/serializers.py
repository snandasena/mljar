from rest_framework import serializers
from apps.datasources import models


class FileDataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FileDataSource
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
            "parent_organization",
            "parent_project",
        )
        fields = (
            "id",
            "title",
            "description",
            "absolute_path",
            "file_name",
            "file_size",
            "created_at",
            "updated_at",
            "created_by",
            "parent_organization",
            "parent_project",
        )
