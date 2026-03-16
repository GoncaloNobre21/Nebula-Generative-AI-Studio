# Nebula Generative AI Studio

Nebula Generative AI Studio is a professional-grade LLM orchestration framework designed for building, managing, and deploying advanced Generative AI applications. It provides a unified interface for multiple LLM providers, structured prompt management, and a robust API layer.

## Architecture

The system follows a modular architecture:

- **Orchestrator**: Manages connections and failover between different LLM providers (OpenAI, Anthropic, HuggingFace).
- **Prompt Engine**: Advanced prompt engineering templates and management using LangChain.
- **API Layer**: FastAPI-based endpoints for text generation, summarization, and more.
- **Infrastructure**: Containerized deployment using Docker.

## Project Structure

```
Nebula-Generative-AI-Studio/
â”œâ”€â”€ README.md
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ api/
â”‚   â”‚   â””â”€â”€ app.py
â”‚   â”œâ”€â”€ orchestrator/
â”‚   â”‚   â””â”€â”€ llm_manager.py
â”‚   â””â”€â”€ prompts/
â”‚       â””â”€â”€ templates.py
â””â”€â”€ docker/
    â””â”€â”€ Dockerfile
```

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment variables (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`)
3. Run the API: `uvicorn src.api.app:app --reload`
