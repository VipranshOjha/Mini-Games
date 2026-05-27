# 🎮 2048 Game

A polished and feature-rich clone of the classic **2048 puzzle game**, built using **Python** and **Pygame**.

Slide tiles, combine matching numbers, chase the legendary **2048 tile**, and keep pushing for even higher scores — now with smooth animations, score popups, undo support, persistent high scores, and polished game-state overlays.

---

## ✨ Features

### 🎯 Core Gameplay

* Classic 4x4 2048 gameplay
* Smooth tile movement animations
* Merge mechanics with collision handling
* Random tile spawning (`2` & `4`)

### 🏆 Score System

* Live score tracking
* Persistent best score saving
* High score survives relaunches using `highscore.txt`
* Floating score popup particles on merges

### 🔁 Game Controls

* Arrow Keys support
* WASD support
* Restart anytime with:

  * `R` key
  * "New Game" button
* Undo moves using `Z`

### 🧠 Advanced Features

* 10-step undo history
* Animated undo transitions
* Win overlay when reaching 2048
* Continue playing after winning
* Game-over overlay with instant restart
* Keyboard shortcut footer

### 🎨 UI & Polish

* Minimalist aesthetic inspired by the original 2048
* Responsive score cards
* Hover effects on buttons
* Smooth particle animations
* Clean header/footer layout

---

## 🛠️ Tech Stack

* **Python**
* **Pygame**

---

## 📂 Project Structure

```
2048-Game/
│── main.py
│── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```
git clone https://github.com/VipranshOjha/Mini-Games.git
```

### 2️⃣ Navigate to the Project Folder

```bash id="4n8s1r"
cd Mini-Games/2048-Game
```

### 3️⃣ Install Dependencies

```
pip install pygame
```

### 4️⃣ Run the Game

```
python main.py
```

---

## 🎮 Controls

| Key    | Action       |
| ------ | ------------ |
| ⬅️ / A | Move Left    |
| ➡️ / D | Move Right   |
| ⬆️ / W | Move Up      |
| ⬇️ / S | Move Down    |
| R      | Restart Game |
| Z      | Undo Move    |

---

## 🧠 Gameplay Rules

* Merge tiles with the same value to create larger numbers.
* Every valid move spawns a new tile.
* Plan moves carefully to avoid filling the board.
* Reach **2048** to trigger the win screen.
* Continue beyond 2048 and chase higher scores.

---

## 🔥 Highlights

### 💾 Persistent High Score

Your best score is automatically saved locally and restored every time the game launches.

### ✨ Floating Score Popups

Every merge creates animated score particles that float upward for satisfying visual feedback.

### ↩️ Undo System

Made a bad move? Press `Z` to rewind up to 10 previous states with smooth undo animations.

### 🏆 Win & Game Over Screens

Elegant overlays provide polished transitions between gameplay states without breaking immersion.

---

## 🤝 Contributing

Contributions, ideas, and improvements are always welcome.

Feel free to fork the project and submit a pull request.

---

## 👨‍💻 Author

Made with Python and Pygame by **Vipransh Ojha**
