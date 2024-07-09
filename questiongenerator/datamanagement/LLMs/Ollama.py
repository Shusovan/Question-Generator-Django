from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings

class Ollama():

    def __init__(self) -> None:
        ...

    def _initialize_embedding(self):

        return OllamaEmbedding(
            model_name="llama3",
            base_url="http://localhost:11434",
            ollama_additional_kwargs={"mirostat": 0},
        )
