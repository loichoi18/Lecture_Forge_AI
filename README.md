# Lecture_Forge_AI
🎓 LectureForge AI
Upload a lecture. Get a full learning module.An end-to-end AI pipeline that transforms raw video lectures, audio recordings, or transcripts into structured, LMS-ready learning modules — complete with summaries, learning objectives, flashcards, and quizzes.
INPUT:  Any lecture file (MP4 / MP3 / PDF / transcript)
            ↓
OUTPUT: A complete structured learning module:
        ✅ Auto-generated transcript (Whisper AI)
        ✅ 150-word executive summary
        ✅ 6 learning objectives (Bloom's Taxonomy aligned)
        ✅ Full lesson outline with sections
        ✅ Key concept flashcards
        ✅ 10-question multiple choice quiz with explanations
        ✅ Glossary of domain terms
        
The Problem It Solves
Educators and content creators record hours of expert knowledge — workshops, lectures, interviews — but turning that raw content into structured, learnable material takes days of manual work. Transcription, writing objectives, building quizzes, formatting for an LMS — all done by hand.
LectureForge AI does all of that in under 60 seconds.
This is especially relevant for organisations like startup communities, bootcamps, and EdTech platforms that run frequent expert-led sessions and need to scale their content production without scaling their team.

System Architecture
┌─────────────────────────────────────────────────────┐
│              USER UPLOADS FILE                      │
│       (MP4 / MP3 / PDF / DOCX / TXT)               │
└─────────────────┬───────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────────────────┐
│             BACKEND — FastAPI (Python)              │
│                                                     │
│  1. TRANSCRIBER  →  Whisper converts audio to text  │
│  2. CHUNKER      →  Splits transcript into pieces   │
│  3. EMBEDDER     →  FAISS vector store (RAG)        │
│  4. GENERATOR    →  GPT-4o with engineered prompts  │
│  5. ASSEMBLER    →  Builds the complete module      │
└─────────────────┬───────────────────────────────────┘
                  │ JSON
                  ▼
┌─────────────────────────────────────────────────────┐
│             FRONTEND — React + Tailwind             │
│  Upload → Summary → Objectives → Flashcards → Quiz  │
└─────────────────────────────────────────────────────┘

Project Structure
lectureforge-ai/
├── backend/
│   ├── main.py                   # FastAPI entry point
│   └── core/
│       ├── transcriber.py        # Whisper audio-to-text
│       ├── chunker.py            # Smart text chunking
│       ├── embedder.py           # FAISS vector store
│       ├── generator.py          # All LLM prompt engineering
│       └── module_builder.py     # End-to-end pipeline
├── frontend/
│   └── src/
│       ├── App.jsx
│       └── components/
│           ├── UploadPanel.jsx   # Drag-and-drop upload
│           ├── ModuleViewer.jsx  # Full module display
│           ├── QuizMode.jsx      # Interactive quiz
│           └── FlashcardDeck.jsx # Flip-card flashcards
├── notebooks/
│   ├── 01_transcription_demo.ipynb
│   ├── 02_rag_pipeline_demo.ipynb
│   └── 03_prompt_engineering.ipynb
├── docs/
│   ├── HOW_IT_WORKS.md
│   ├── PROMPT_ENGINEERING.md
│   └── API_REFERENCE.md
├── examples/
│   └── sample_transcript.txt
├── requirements.txt
├── .env.example
└── demo.py
Quick Start
1. Clone and install
hgit clone https://github.com/badungluong/lectureforge-ai.git
cd lectureforge-ai
pip install -r requirements.txt
2. Add your OpenAI API key
cp .env.example .env
# Open .env and add: OPENAI_API_KEY=sk-...
3. Run the demo (no server needed)
python demo.py
4. Run the full stack
# Terminal 1 — backend
uvicorn backend.main:app --reload --port 8000

# Terminal 2 — frontend
cd frontend
npm install
npm run dev
# Open http://localhost:5173
Prompt Engineering
Prompt design is a core part of this project. Every LLM call uses carefully engineered prompts that enforce consistent output format, Bloom's Taxonomy alignment for learning objectives, JSON schema for reliable parsing, and RAG grounding to prevent hallucination.
See docs/PROMPT_ENGINEERING.md for full documentation of every prompt, its design rationale, and what changed across iterations.
Example — the learning objectives prompt requires exactly 6 objectives, each starting with a Bloom's Taxonomy action verb, grounded only in the actual lecture content, returned as structured JSON with bloom level metadata.

Tech Stack
LayerTechnologyTranscriptionOpenAI WhisperLLMGPT-4oRAG FrameworkLangChainVector StoreFAISSEmbeddingsOpenAI text-embedding-3-smallBackendFastAPI + UvicornFrontendReact 18 + Vite + TailwindCSSPDF ParsingPyMuPDFAudio Extractionpydub + ffmpeg
