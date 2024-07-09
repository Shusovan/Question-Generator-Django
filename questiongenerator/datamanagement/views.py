from webbrowser import get
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .indexers.string_indexer import StringIndexer

from .models import HelloWorld, Question, UploadDocuments, UploadString, SubjectRegister
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


class HelloWorldVew(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(HelloWorld().word)
    

class StartIndexView(APIView):

    def post(self, request, *args, **kwargs):

        # id passes as query parameter
        get_id = request.query_params.get("id")

        if get_id is None:
            return JsonResponse({'error': 'id parameter is required'}, status=400)

        try:
            # fetching details of id (UUID)
            subject_register_object = get_object_or_404(SubjectRegister, id = get_id)

            string_indexer = StringIndexer(subject_register_object)

            string_indexer.start_indexing()

            # returning JSON response
            return JsonResponse(
                {
                    "id" : subject_register_object.id,
                    "subject" : subject_register_object.subject,
                    "index_location" : subject_register_object.index_location,
                    "row_created" : subject_register_object.row_created,
                    "isDeleted" : subject_register_object.isDeleted
                })
        
        except SubjectRegister.DoesNotExist:
            return JsonResponse({'error': 'Object with given id does not exist'}, status=404)