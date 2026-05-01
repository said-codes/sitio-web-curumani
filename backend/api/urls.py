from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NegocioViewSet, EventoViewSet, NewsAPIView

router = DefaultRouter()
router.register(r'negocios', NegocioViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('news/', NewsAPIView.as_view(), name='news_api'),
]
