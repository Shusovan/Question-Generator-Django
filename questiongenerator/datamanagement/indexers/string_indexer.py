import string
from typing import List

from ..LLMs.Ollama import Ollama
from ..models import SubjectRegister

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

class StringIndexer():

    def __init__(self, subject_obj) -> None:
        self.subject_model_object = subject_obj
    

    def start_indexing(self):

        # get all unindexed strings
        unindexed_strings = self.subject_model_object.get_delta_resources(isIndex = False)
        
        nodes = []

        for subject_strings in unindexed_strings:
            
            document = self._get_documents(subject_strings)
            
            # node = use sentence spiltter class and call get_nodes_from_documents(documetn)
            # nodes.extend(node)
            sentence_splitter = SentenceSplitter()
            node = sentence_splitter.get_nodes_from_documents(document)
            nodes.extend(node)

        local_model = Ollama()

        # build index
        index = VectorStoreIndex(nodes, embed_model = local_model._initialize_embedding())

    
    def _get_documents(self,string) -> List[Document]:
        return [Document(text=string)]
        


