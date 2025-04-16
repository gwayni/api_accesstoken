from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import itemViewSet, SecureHelloView



router = DefaultRouter()
router.register(r'list', itemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('secure-hello/', SecureHelloView.as_view()),

]