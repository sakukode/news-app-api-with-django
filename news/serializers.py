# import class serializers
from rest_framework.serializers import ModelSerializer

# import Category model
from .models import Category


# Membuat class Serializers untuk API endpoint "Get List of Categories"
class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', )


# Membuat class Serializers untuk API endpoint "Get Detail of Category"
class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', )