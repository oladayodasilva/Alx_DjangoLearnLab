from rest_framework import serializers
from .models import Book
from datetime import datetime, timezone

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_days_since_created(self, obj):
        return (datetime.now(timezone.utc) - obj.created_at).days

