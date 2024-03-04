from django.urls import path

from categories.apps import CategoriesConfig
from categories.views import CategoryListAPIView

app_name = CategoriesConfig.name


urlpatterns = [
    path('list/', CategoryListAPIView.as_view(), name='list-category'),
]
