from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_core.documents import Document
from pathlib import Path
from typing import List


def doc_loader(data_path: str) -> List[Document]:
    data_dir=Path(data_path).resolve()
    try:
        data_loader=DirectoryLoader(
                    path=data_dir,
                    glob='**/*.pdf',
                    loader_cls=PyPDFLoader
                )
        document=data_loader.load()
        return document
    except Exception as e:
        print('The error in the Data loading and the type: ',e)
        raise

def doc_filter(document : List[Document]) -> (List[Document]):
    try:
        new_doc=[]
        for doc in document:
            src=doc.metadata.get('source')
            new_doc.append(Document(metadata={'source':src, 'lesson': 'Economically Useful Plants and Entrepreneurial Botany'},
                        page_content=doc.page_content))
        return new_doc
    except Exception as e:
        print('Error in the Doc_filter: ',e)
        raise

