from rest_framework.viewsets import ModelViewSet
from .serializers import RecipeSerializer, CategorySerializer, SFCSerializer, UsersSerializer
from .models import Recipe, Category, SFC, Users
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
import django_filters.rest_framework
from django.db.models import Q

class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(methods=['GET'], detail=False)
    def get_data(self, request, **kwargs):
        queryset = Recipe.objects.filter(Q(title.length <= 10))
        return Response(queryset)

    @action(methods=['POST'], detail=True)
    def publish(self, request, **kwargs):
        recipe = self.get_object()
        text = json.loads(request.POST.get('text'))
        if text:
            recipe.text = text
        recipe.save()
        return Response()

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    
class SFCViewSet(ModelViewSet):
    queryset = SFC.objects.all()
    serializer_class = SFCSerializer


class GetRecipeView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title','ingredients']



class GetCategoryView(ListAPIView):
    queryset = Category.objects.filter( Q(name='Выпечки') | Q(name='Закуски') )
    serializer_class = CategorySerializer

