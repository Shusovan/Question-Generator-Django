from operator import index
from pyexpat import model
import uuid
from xml.dom.minidom import Document
from django.db import models
from sqlalchemy import true

class Question(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    subject = models.CharField(max_length = 100)
    
    question = models.TextField()
    
    option1 = models.TextField()
    
    option2 = models.TextField()
    
    option3 = models.TextField()
    
    option4 = models.TextField()
    
    row_created = models.DateTimeField(auto_now_add = True)

    isDeleted = models.BooleanField(default = False)

    # meta of database
    class Meta:
        db_table = "question"
        managed = True
        verbose_name = "Question"
        verbose_name_plural = "Questions"


'''
    Register subjects for generating questions
    
    get_delta_resources(): 
        Description : Fetch the resource whose isIndex is false
        @param : self, isIndex
        Return : dict
'''
class SubjectRegister(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    subject = models.CharField(max_length = 100)

    index_location = models.CharField(max_length=500, default = None, null=True, blank = True)

    row_created = models.DateTimeField(auto_now_add = True)

    isDeleted = models.BooleanField(default = False)

    
    def get_delta_resources(self, isIndex : False) -> dict:

        # Filtering data with isIndex and subject
        unindexed_string = UploadString.objects.filter(isIndexed = isIndex, subjects = self.subject)

        # creating a dictionary
        resources = {"string" : unindexed_string}

        return resources

    
    def __str__(self) -> str:
        return self.subject


'''
    Generates questions from documents
'''
class UploadDocuments(models.Model):

    DOCUMENT_TYPE = [("pdf" , "pdf")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    subject = models.CharField(max_length = 100)

    # name and location of the folder "docs/"
    document = models.FileField(upload_to="docs/")

    type = models.CharField(max_length = 100, choices = DOCUMENT_TYPE, default = "pdf")

    row_created = models.DateTimeField(auto_now_add = True)

    isDeleted = models.BooleanField(default = False)


'''
    Generates questions from strings
'''
class UploadString(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    subjects = models.ForeignKey(SubjectRegister, on_delete = models.CASCADE, null=True, blank = True)

    string_prompt = models.CharField(max_length = 1000)

    isIndexed = models.BooleanField(default = False)

    row_created = models.DateTimeField(auto_now_add = True)

    isDeleted = models.BooleanField(default = False)