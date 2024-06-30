from django.urls import path, include
from rest_framework import routers

from .views import QuestionViewSet, UploadDocumentsViewSet, UploadStringViewSet, SubjectRegisterViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'upload/documents', UploadDocumentsViewSet)
router.register(r'upload/strings', UploadStringViewSet)
router.register(r'subject/register', SubjectRegisterViewSet)

QUESTION = router.registry

urlpatterns = [
    path('', include(router.urls))
]