from django.shortcuts import render
from rest_framework import viewsets

from .models import Question, UploadDocuments, UploadString, SubjectRegister
from .serializer import QuestionSerializer, UploadDocumentsSerializer, UploadStringSerializer, SubjectRegisterSerializer

# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UploadDocumentsViewSet(viewsets.ModelViewSet):
    queryset = UploadDocuments.objects.all()
    serializer_class = UploadDocumentsSerializer


class UploadStringViewSet(viewsets.ModelViewSet):
    queryset = UploadString.objects.all()
    serializer_class = UploadStringSerializer


class SubjectRegisterViewSet(viewsets.ModelViewSet):
    queryset = SubjectRegister.objects.all()
    serializer_class = SubjectRegisterSerializer