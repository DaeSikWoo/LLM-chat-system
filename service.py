from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFacePipeline
from transformers import LlamaTokenizer, LlamaForCausalLM, pipeline
import click

from constants import CHROMA_SETTINGS, PERSIST_DIRECTORY

def load_model():
    #model_id = "ureca07/korean-vicuna-7b-1.1"
    model_id = "TheBloke/vicuna-7B-1.1-HF"
    tokenizer = LlamaTokenizer.from_pretrained(model_id)
    model = LlamaForCausalLM.from_pretrained(model_id)
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=2048,
        temperature=0,
        top_p=0.95,
        repetition_penalty=1.15
    )
    local_llm = HuggingFacePipeline(pipeline=pipe)
    return local_llm

def initialize_qa():
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl", model_kwargs={"device": "cpu"})
    db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever()
    loaded_model = load_model()
    qa = RetrievalQA.from_chain_type(llm=loaded_model, chain_type="stuff", retriever=retriever, return_source_documents=True)
    return qa

@click.command()
@click.option('--device_type', default='cpu', help='device to run on')
def main(device_type):
    initialize_qa()
    # Rest of the code...

if __name__ == "__main__":
    main()

