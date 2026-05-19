from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')


class RagPipeline:

    def __init__(self):
        pass

    def retriver(self, retriever):

        chat_model = ChatGroq(
            model="llama-3.1-8b-instant",
            groq_api_key=GROQ_API_KEY,
            temperature=0.7,
            max_tokens=512
        )

        system_prompt = (
                    "You are an expert Botany tutor helping students understand plant science deeply. "
                    "Your answers must always be grounded in the retrieved context provided — do not answer from general knowledge alone. "
                    "If the retrieved context does not contain enough information to answer the question, clearly say: "
                    "'I don't have enough information in my reference material to answer this.' "
                    "\n\n"
                    "Follow this structured response format:\n"
                    "1. **Direct Answer** — (answer should satrt with two newline) Give a clear, concise answer to the question using information from the retrieved context and if there any types or examples are there, mention it.\n"
                    "2. **Scientific Classification** — Mention the correct biological/scientific name (genus, species) using proper italicized notation (e.g., *Oryza sativa*). Include family, order, class or if there may be a origin and area of cultivation.\n"
                    "3. **Detailed Explanation** — Expand the answer using accurate botanical terminology (e.g., parenchyma, meristem, phloem, photosynthesis, auxin, gynoecium, etc.). Explain mechanisms, structures, or processes as applicable using the retrived .\n"
                    "4. **Origin and Area of cultivation** - Mention the correct area of cultivation and origin deatiled, if mentioned "
                    "Answer ONLY from the retrieved context below. "
                    "If the answer is not present in the context, say: "
                    "'This information is not in my reference material.' "
                    "Always maintain a patient, encouraging teaching tone. Use simple language to explain complex terms so a student can truly understand, not just memorize."
                    "Where possible, reference the section or topic from the retrieved material to help the student locate it for further study."
                    "\n\n"
                    "{context}"
                    )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])

        que_doc_chain = create_stuff_documents_chain(
            chat_model,
            prompt
        )

        rag_chain = create_retrieval_chain(
            retriever,
            que_doc_chain
        )

        return rag_chain