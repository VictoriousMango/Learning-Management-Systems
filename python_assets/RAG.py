from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
# from langchain.vectorstores import Chroma
from groq import Groq
from LMS import Config
from Logger import logger
import json
import os

# Set Groq API Key
# GROQ_API_KEY = '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'  # Replace with your actual Groq API key
groq_client = Groq(api_key=Config.GROQ_API_Key)

class RAG():
    def __init__(self):
        # Load PDF document
        pdf_path = "C:/Users/yadas/Downloads/1.) deep_learning.pdf"
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.texts = text_splitter.split_documents(documents)

        # Generate embeddings using Sentence Transformer
        self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Function to generate 5 MCQs using LLaMA 70B via Groq
    def generate_mcq(self, text):
            response = groq_client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": Config.prompt(text)}],
            )

            # Get the raw response from Groq API
            raw_response = response.choices[0].message.content
            logger.debug("Raw Response:", raw_response)

            # Try to extract the JSON part
            try:
                # Find the position of the first '{' and the last '}'
                start_pos = raw_response.find('{')
                end_pos = raw_response.rfind('}')
                
                if start_pos != -1 and end_pos != -1:
                    json_str = raw_response[start_pos:end_pos+1]
                    mcqs = json.loads(json_str)
                    
                    # Additional validation to ensure CorrectOption contains text, not just option references
                    for question_key, question_data in mcqs.items():
                        # If CorrectOption is just a reference like "Option1", replace it with the actual text
                        if question_data["CorrectOption"].startswith("Option"):
                            option_num = question_data["CorrectOption"].replace("Option", "")
                            if option_num.isdigit() and 1 <= int(option_num) <= 4:
                                option_key = f"Option{option_num}"
                                question_data["CorrectOption"] = question_data[option_key]
                    
                    if isinstance(mcqs, dict):  
                        return mcqs
                
                print("Unexpected response format, skipping...")
                return {}
            except json.JSONDecodeError:
                print(f"Error parsing JSON response: {raw_response}")
                return {}
    
    # Generate MCQs from document chunks
    def get_MCQ(self):
        all_mcqs = {}
        question_counter = 1

        for text in self.texts:
            chunk_mcqs = self.generate_mcq(text.page_content)
            if chunk_mcqs:
                for question_key, question_data in chunk_mcqs.items():
                    new_key = f"Question{question_counter}"
                    all_mcqs[new_key] = question_data
                    question_counter += 1
        return all_mcqs
    
PDF_MCQ = RAG()
mcqs = PDF_MCQ.get_MCQ()
logger.info("MCQs generated successfully.")
logger.debug(mcqs)
logger.info("MCQs generated successfully.")