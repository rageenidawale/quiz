# 🧠 Quizzler – Test Your Knowledge! 🎓

This Python-based **quiz application** presents multiple-choice questions fetched from an external dataset and keeps track of the user's score.

---

## ✨ Features
- Loads **trivia questions** dynamically.
- Tracks **user's progress and score**.
- Uses **OOP principles** (separate classes for questions, quiz logic, and UI).
- **Interactive UI** using Tkinter.

---

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies

Ensure you have Python installed, then install **Tkinter** if needed:

```bash
pip install tk
```

---

### 2️⃣ Project Structure

```
📂 Quiz_App
│── 📜 main.py           # Entry point of the application
│── 📜 question_model.py # Question class definition
│── 📜 quiz_brain.py     # Quiz logic and game flow
│── 📜 data.py           # Stores the question bank
│── 📜 ui.py             # Tkinter-based GUI
```

---

### 3️⃣ Run the Application

Execute the script:

```bash
python main.py
```

The app will open a **GUI window**, displaying quiz questions with **True/False** buttons.

---

## 📜 How It Works

1. **Loads questions** from `data.py` (or an API, if integrated).
2. Displays questions using **Tkinter** UI.
3. User selects **True** or **False**.
4. App provides **instant feedback** and updates the **score**.
5. **At the end**, displays the **final score**.
