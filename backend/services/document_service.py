import pandas as pd
import tempfile
import os
from typing import Tuple, Optional, Any
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

class DocumentService:
    """Serviço para processamento de documentos"""
    
    def __init__(self):
        self.supported_formats = ['.pdf', '.csv', '.xlsx', '.txt']
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    def process_uploaded_file(self, uploaded_file) -> Tuple[Optional[Any], Optional[Any], str]:
        """Processa arquivo uploadado"""
        try:
            if uploaded_file is None:
                return None, None, "no_file"
            
            file_ext = f".{uploaded_file.name.split('.')[-1].lower()}"
            
            if file_ext not in self.supported_formats:
                raise ValueError(f"Formato não suportado: {file_ext}")
            
            # Salvar arquivo temporário
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
                tmp.write(uploaded_file.getvalue())
                file_path = tmp.name
            
            try:
                if file_ext == '.csv':
                    df = pd.read_csv(file_path)
                    # Simular query engine para CSV
                    return df, {"type": "csv", "data": df}, 'csv'
                
                elif file_ext == '.pdf':
                    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
                    index = VectorStoreIndex.from_documents(documents, embed_model=self.embed_model)
                    return documents, index, 'pdf'
                
                else:
                    raise ValueError(f"Tipo de arquivo não implementado: {file_ext}")
                    
            finally:
                # Limpar arquivo temporário
                if os.path.exists(file_path):
                    os.unlink(file_path)
                
        except Exception as e:
            print(f"Erro no processamento: {e}")
            return None, None, 'error'
    
    def extract_content(self, processed_data, data_type):
        """Extrai conteúdo para sumarização"""
        try:
            if data_type == "csv":
                df, _, _ = processed_data
                return df.head(100).to_string()  # Limitar para 100 linhas
            else:
                docs, _, _ = processed_data
                content = "\n".join([doc.text for doc in docs])
                return content[:50000]  # Limitar conteúdo
        except:
            return "Conteúdo não disponível para sumarização"