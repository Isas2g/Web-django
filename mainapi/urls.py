from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SFCViewSet, UsersViewSet, RecipeViewSet, CategoryViewSet, GetRecipeView, GetCategoryView

router = DefaultRouter()
router.register('sfc', SFCViewSet, )
router.register('users', UsersViewSet, )
router.register('recipes', RecipeViewSet, )
router.register('categories', CategoryViewSet, )



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/recipes/filtering', GetRecipeView.as_view()),
    path('api/categories/filtering', GetCategoryView.as_view()),
]
