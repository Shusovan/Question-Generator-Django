from typing import List

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Document, VectorStoreIndex, Settings, load_index_from_storage, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.groq import Groq
from django.conf import settings


class StringIndexer():


    def __init__(self, subject_obj) -> None:
        self.subject_model_object = subject_obj
    

    def start_indexing(self):

        # get all unindexed strings
        unindexed_strings = self.subject_model_object.get_delta_resources(isIndex = False)
        
        nodes = []

        for subject_strings in unindexed_strings['string']:
            
            document = self._get_documents(subject_strings.string_prompt)
            
            # node = use sentence spiltter class and call get_nodes_from_documents(documetn)
            # nodes.extend(node)
            sentence_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20,)
            node = sentence_splitter.get_nodes_from_documents(document)
            nodes.extend(node)

        # Creating embeddings from HuggingFace
        Settings.embed_model = HuggingFaceEmbedding(model_name = "BAAI/bge-small-en-v1.5")

        # using Llama-3 70b LLM from Groq
        Settings.llm = Groq(model = "llama3-70b-8192", api_key = settings.GROQ_API_KEY)
        
        # Retrieval-Augmented Generation (RAG)
        index = VectorStoreIndex(nodes = nodes, show_progress = True, embed_model = Settings.embed_model)

        # storing the embeddings in index folder
        index.storage_context.persist(persist_dir=settings.MEDIA_ROOT+"index")
        
        # query the model
        query_engine = index.as_chat_engine()
        response = query_engine.query("Generate 2 MCQ question in python with correct answer")
        print(response)

    
    def load_index():

        storage_context = StorageContext.from_defaults(persist_dir=settings.MEDIA_ROOT+"index")

        index_object = load_index_from_storage(storage_context, embed_model = Settings.embed_model)

        return index_object
    

    def process_query():

        
        ...

    
    def _get_documents(self,string) -> List[Document]:
        return [Document(text=string)]