from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.orchestrator.llm_manager import LLMManager
from src.prompts.templates import SUMMARIZATION_PROMPT

app = FastAPI(title="Nebula Generative AI Studio")
llm_manager = LLMManager()

class GenerationRequest(BaseModel):
    """Data model for a text generation request."""
    prompt: str
    provider: str = "openai"
    model: str = "gpt-4"

class SummarizationRequest(BaseModel):
    """Data model for a text summarization request."""
    text: str

@app.post("/generate")
async def generate_text(request: GenerationRequest):
    """Endpoint for generating text using a specified provider and model."""
    try:
        if request.provider == "openai":
            return {"result": llm_manager.generate_openai(request.prompt, request.model)}
        elif request.provider == "anthropic":
            return {"result": llm_manager.generate_anthropic(request.prompt, request.model)}
        elif request.provider == "huggingface":
            return {"result": llm_manager.generate_hf(request.prompt, request.model)}
        else:
            raise HTTPException(status_code=400, detail="Invalid provider")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def summarize_text(request: SummarizationRequest):
    """Endpoint for summarizing text using OpenAI's model and the summarization prompt."""
    try:
        prompt = SUMMARIZATION_PROMPT.format(text=request.text)
        return {"summary": llm_manager.generate_openai(prompt)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Welcome to Nebula Generative AI Studio"}
