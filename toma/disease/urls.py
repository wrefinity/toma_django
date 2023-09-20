
from django.urls import path
from .views import (
    DiseaseView,
    TomatoesDetailView,
    TomatoesListView,
    TomatoesDeleteView,
    TomatoesSearchView,
    TomatoesMultiFieldSearchView,
)

urlpatterns = [
    path('/create', DiseaseView.as_view(), name="disease_create"),
    path('/<int:pk>/', TomatoesDetailView.as_view(), name='detail-tomatoes'),
    path('', TomatoesListView.as_view(), name='list-tomatoes'),
    path('/search/', TomatoesSearchView.as_view(), name='search-tomatoes'),
    path('/<int:pk>/delete/',
         TomatoesDeleteView.as_view(), name='delete-tomatoes'),
    path('search_multi/', TomatoesMultiFieldSearchView.as_view(),
         name='multi-field-search-tomatoes'),
]
