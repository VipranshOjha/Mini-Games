# 🧩 Sudoku-Game

An interactive **Sudoku** game built with **Python** and **Pygame**.
Play, solve, or even let the computer solve puzzles in real-time. The game also includes a Sudoku **puzzle generator** so each playthrough feels fresh.

---

## ✨ Features

* 🎮 **Interactive Gameplay** – Click on cells and type numbers to fill the board.
* 🖊 **Sketch Mode** – Temporarily pencil in numbers before committing.
* 🧠 **Built-in Solver** – Press `SPACE` to watch the AI solve the puzzle step-by-step.
* 🔄 **Random Puzzle Generator** – Every game starts with a unique Sudoku board.
* ❌ **Mistake Tracking** – Incorrect entries increase your strike count.
* ⏱ **Timer** – Track how long you take to solve the puzzle.

---

## 📂 Project Structure

```
Sudoku/
│── Generator.py   # Generates random Sudoku puzzles
│── Solver.py      # Solves Sudoku puzzles using backtracking
│── Sudoku.py      # Main game file with GUI, interactions, and gameplay
```

---

## 🕹 Controls

| Key / Action | Function                 |
| ------------ | ------------------------ |
| Mouse Click  | Select a cell            |
| 1–9          | Enter number             |
| DELETE       | Clear selected cell      |
| ENTER        | Confirm temporary number |
| SPACE        | Auto-solve puzzle (AI)   |
| Close Window | Exit game                |

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

Make sure you have **Python 3.x** installed, then install **pygame**:

```bash
pip install pygame
```

### 2️⃣ Run the Game

```bash
python Sudoku.py
```

---

## 🛠 How It Works

* **Puzzle Generation** (`Generator.py`):

  * Fills the diagonal boxes first for faster generation.
  * Uses backtracking to complete the board.
  * Removes random numbers while ensuring the puzzle has a unique solution.

* **Puzzle Solving** (`Solver.py`):

  * Uses a backtracking algorithm to solve puzzles.
  * Checks validity by row, column, and 3×3 grid.

* **Gameplay** (`Sudoku.py`):

  * Handles rendering, user inputs, and game logic.
  * Supports manual play and AI-assisted solving.

---
