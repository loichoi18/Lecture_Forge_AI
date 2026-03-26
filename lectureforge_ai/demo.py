"""
demo.py — Quick end-to-end demo of LectureForge AI

Runs the full pipeline on the sample transcript without needing
a running server. Good for testing your setup before going full-stack.

Usage:
    python demo.py

Requirements:
    - OPENAI_API_KEY set in .env
    - pip install -r requirements.txt
"""

import json
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
sys.path.append(str(Path(__file__).parent))

from backend.core.module_builder import process_lecture


def main():
    sample = Path("examples/sample_transcript.txt")

    if not sample.exists():
        print("❌ Sample transcript not found. Run from the project root.")
        sys.exit(1)

    print("=" * 60)
    print("  🎓 LectureForge AI — Demo Run")
    print("=" * 60)
    print(f"  Input : {sample}")
    print("  This will call OpenAI API (GPT-4o + embeddings)")
    print("=" * 60)
    print()

    module = process_lecture(sample, title="Introduction to Machine Learning")

    print()
    print("=" * 60)
    print("  ✅ Module generated successfully!")
    print("=" * 60)
    print(f"  Module ID  : {module['module_id']}")
    print(f"  Title      : {module['title']}")
    print(f"  Words      : {module['word_count']:,}")
    print(f"  Time       : {module['processing_time_secs']:.1f}s")
    print()

    print("── Summary ──")
    print(module["summary"])
    print()

    print("── Learning Objectives ──")
    for i, obj in enumerate(module["learning_objectives"], 1):
        level = obj.get("bloom_level", "")
        print(f"  {i}. [{level}] {obj['objective']}")
    print()

    print("── Flashcards (first 3) ──")
    for card in module["flashcards"][:3]:
        print(f"  {card['term']}: {card['definition'][:80]}...")
    print()

    print("── Quiz (first 2 questions) ──")
    for q in module["quiz"][:2]:
        print(f"  Q{q['question_number']}: {q['question']}")
        print(f"  Answer: {q['correct_answer']} — {q['explanation'][:80]}...")
        print()

    output_path = Path("backend/storage/modules") / f"{module['module_id']}.json"
    print(f"  📁 Full module saved to: {output_path}")
    print()
    print("  Now start the backend and frontend to view the dashboard!")
    print("    Backend : uvicorn backend.main:app --reload --port 8000")
    print("    Frontend: cd frontend && npm run dev")


if __name__ == "__main__":
    main()
