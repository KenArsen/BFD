from django.urls import path
from card import views

urlpatterns = [
    path('cards/', views.CardList.as_view(), name='card-list'),
    path('cards/create/', views.CardCreate.as_view(), name='card-create'),
    path('cards/<uuid:pk>/', views.CardDetail.as_view(), name='card-detail'),
    path('cards/<uuid:pk>/update/', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<uuid:pk>/delete/', views.CardDelete.as_view(), name='card-delete'),
    path('healthcheck/', views.HealthCheckView.as_view(), name='health-check'),
]
