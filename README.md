# 🧟 Information Security RPG Quiz — Monsters of Procrastination

An interactive, educational quiz built in Python with two gameplay modes: a **standard quiz mode** and a full **RPG battle mode**. Questions are loaded dynamically from a `.txt` file, making it easy to update or expand content without touching the code.

Developed as an academic project at **FATEC São Caetano do Sul** for the Information Security program (2025).

---

## 🎮 How It Works

The quiz automatically detects which mode to run based on the contents of `quiz.txt`:

- **RPG Mode** — activated when the file contains questions authored by the original team. The player battles themed enemies ("Monsters of Procrastination") across 5 information security topics. Each correct answer deals damage to the monster; each wrong answer costs the player a life.
- **Standard Mode** — a straightforward quiz where the player selects a topic and answers a set of randomly selected questions.

---

## 🗂️ File Structure

```
├── quiz.txt        # Question bank (pipe-separated format)
└── modo_lis.py     # Main game logic
```

---

## 📄 Question Format (`quiz.txt`)

Each line in `quiz.txt` must follow this format:

```
Question text | Topic | Correct answer (A/B/C/D) | Option A | Option B | Option C | Option D
```

**Example:**
```
What does CIA stand for in cybersecurity? | Security Fundamentals | A | Confidentiality, Integrity, Availability | Control, Integrity, Access | Confidentiality, Information, Authorization | Cybersecurity, Integrity, Availability
```

To customize the quiz for any subject, simply replace the contents of `quiz.txt` with your own questions following this format.

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed
2. Clone this repository:
   ```bash
   git clone https://github.com/sofiaknebl/Quiz-Monstros-da-Procrastina-o.git
   ```
3. Navigate to the project folder and run:
   ```bash
   python modo_lis.py
   ```

---

## ✨ Features

- Dynamic question loading from external `.txt` file — no code changes needed to update content
- Two independent game modes detected automatically
- Random question sampling without repetition within a session
- Per-theme enemy battles with health point tracking (RPG mode)
- Inclusive pronoun selection (she/he/they)
- Full performance summary at the end of each session
- Input validation throughout

---

## 👩‍💻 Authors

Developed by **Isabela Cascais**, **Laura Felício**, and **Sofia Knebl**  
FATEC São Caetano do Sul — Information Security — SEGMA1 — 2025
