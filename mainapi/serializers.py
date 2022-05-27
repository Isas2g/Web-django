from rest_framework.serializers import ModelSerializer
from .models import Recipe, Category, SFC, Users


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SFCSerializer(ModelSerializer):
    class Meta:
        model = SFC
        fields = '__all__'

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
