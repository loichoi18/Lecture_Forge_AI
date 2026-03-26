# API Reference

Base URL: `http://localhost:8000`
Interactive docs: `http://localhost:8000/docs`

---

## Health

### `GET /`
Returns service status.

**Response**
```json
{ "status": "ok", "service": "LectureForge AI", "docs": "/docs" }
```

---

## Pipeline

### `POST /api/upload`
Upload a lecture file. Returns a `file_id` to use in the next step.

**Request:** `multipart/form-data` with field `file`

**Accepted formats:** `.mp4` `.mov` `.mp3` `.wav` `.m4a` `.pdf` `.txt` `.docx`

**Response**
```json
{
  "file_id":    "a3f2c1d8",
  "filename":   "intro_to_ml.mp3",
  "size_bytes": 45231890,
  "format":     ".mp3",
  "message":    "File uploaded. Call /api/process to generate the module."
}
```

---

### `POST /api/process/{file_id}`
Run the full AI pipeline on an uploaded file. Returns the complete learning module.

**Query params:**
- `title` (optional) — Custom module title

**⚠️ This call takes 30–90 seconds** depending on file length. Do not set a short timeout.

**Response**
```json
{
  "module_id":   "a3f2c1d8",
  "title":       "Introduction to Machine Learning",
  "source_file": "intro_to_ml.mp3",
  "created_at":  "2025-01-15T10:23:41",
  "word_count":  4821,
  "processing_time_secs": 47.3,

  "summary": "A 150-word overview of the lecture...",

  "learning_objectives": [
    { "objective": "Explain the three types of machine learning", "bloom_level": "Understand", "verb": "Explain" }
  ],

  "lesson_outline": [
    {
      "section_number": 1,
      "title": "What is Machine Learning?",
      "duration_estimate": "10 minutes",
      "points": ["Definition and scope", "Relationship to AI", "Real-world applications"]
    }
  ],

  "flashcards": [
    { "term": "Overfitting", "definition": "When a model performs well on training data but poorly on new data." }
  ],

  "quiz": [
    {
      "question_number": 1,
      "question": "Which type of machine learning uses labelled training data?",
      "options": { "A": "Unsupervised learning", "B": "Supervised learning", "C": "Reinforcement learning", "D": "Transfer learning" },
      "correct_answer": "B",
      "explanation": "Supervised learning trains on labelled data where both inputs and correct outputs are provided."
    }
  ],

  "glossary": [
    { "term": "Feature engineering", "definition": "The process of selecting and transforming input variables to improve model performance." }
  ],

  "transcript": "Full transcript text..."
}
```

---

## Modules

### `GET /api/modules`
List all previously generated modules (metadata only, no full content).

**Response**
```json
[
  {
    "module_id":   "a3f2c1d8",
    "title":       "Introduction to Machine Learning",
    "source_file": "intro_to_ml.mp3",
    "created_at":  "2025-01-15T10:23:41",
    "word_count":  4821
  }
]
```

---

### `GET /api/modules/{module_id}`
Get a complete previously generated module by ID.

**Response:** Same structure as `/api/process` response.

**Error (404)**
```json
{ "detail": "Module not found: a3f2c1d8" }
```
