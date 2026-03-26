# How LectureForge AI Works — Plain English Guide

> No technical background required to read this.

---

## The Problem

Imagine a startup community that runs 50 expert workshops a year. Each session
is recorded. But turning a 90-minute recording into a structured online course
takes a content team days of work per session — transcription, writing objectives,
building quizzes, creating glossaries, formatting for the LMS.

**LectureForge AI does all of that in under 60 seconds.**

---

## Step by Step

### 1. You upload a file
Drop in any lecture file — a video recording, an audio file, a PDF of slides,
or a plain text transcript. The system figures out the format automatically.

### 2. Transcription (if needed)
For video and audio files, the system uses **OpenAI Whisper** — the same technology
that powers automatic subtitles — to convert speech into text. It handles accents,
technical terminology, and background noise well.

For PDFs and text files, the text is extracted directly. No transcription needed.

### 3. Smart chunking
A 90-minute lecture might produce 15,000 words. That's too much to give to an AI
model all at once — it has a limited "attention window".

So the system breaks the transcript into overlapping 800-character chunks, like
cutting a long document into manageable pages that slightly overlap at the edges
so nothing falls through the gap.

### 4. Embedding (the memory system)
Each chunk is converted into a list of 1,536 numbers called a **vector embedding**.
Think of it like a GPS coordinate — but instead of a location in physical space,
it's a location in meaning-space. Similar concepts end up with similar coordinates.

These embeddings are stored in a **FAISS vector database** (a very fast similarity
search engine developed by Meta).

### 5. Retrieval (finding the right context)
When generating each part of the learning module, the system asks a targeted question:
- For the summary: *"What are the main topics and key points?"*
- For flashcards: *"What key terms and definitions were explained?"*
- For the quiz: *"What important facts should learners be tested on?"*

It retrieves the 5–8 most relevant chunks for each question — like a research
assistant pulling the right paragraphs from a textbook.

### 6. Generation (the AI writes the content)
The retrieved chunks are fed to **GPT-4o** along with carefully engineered prompts.
The prompts tell the model exactly what to produce:

- The summary prompt requires exactly 150 words in flowing prose
- The objectives prompt requires Bloom's Taxonomy-aligned action verbs
- The quiz prompt requires plausible wrong answers with explanations

This prompt engineering is what ensures consistent, high-quality, LMS-ready output
every time — not random AI-generated text.

### 7. Assembly and export
All six sections (summary, objectives, outline, flashcards, quiz, glossary) are
assembled into a single structured JSON file and saved. The React dashboard
presents them in a tabbed interface where educators can review, interact with
the quiz, and export the module.

---

## Why This Matters for Education

Traditional course creation is a bottleneck. Expert knowledge gets locked inside
recordings that no one has time to properly structure. LectureForge AI removes
that bottleneck — any recorded session can become a full structured module,
making expert-led programs far more scalable.

This is the direction EdTech is heading: AI not as a replacement for educators,
but as a **force multiplier** for the content they already create.

---

*Built by Ba Dung Luong — Bachelor of Artificial Intelligence, UTS*
