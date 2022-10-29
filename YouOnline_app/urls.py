from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from YouOnline_app.views import posts

router = routers.DefaultRouter()
router.register('posts', posts)

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
