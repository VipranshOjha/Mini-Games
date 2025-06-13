# Rubik's Cube Simulator 🧩

A stunning 3D Rubik's Cube simulator with intuitive controls, built using Python, OpenGL, and Pygame.

## 🌟 Features

- **Realistic 3D Cube**: Smooth, colorful 3D rendering of a Rubik's Cube
- **Intuitive Controls**: Drag faces to rotate layers naturally
- **Multiple Implementations**:
  - Advanced 3D implementation with OpenGL
  - Terminal-based version for minimalist environments
  - URSINA engine implementation with advanced graphics
- **Scrambler**: Randomize your cube with a single button press
- **Auto-Solver**: Watch the cube solve itself using advanced algorithms
- **Educational Tool**: Great for learning cube solving techniques

## 🎮 Controls

- **Mouse Drag**: Click and drag on a face to rotate that layer
- **Arrow Keys**: Rotate the entire cube to view from different angles
- **Space**: Scramble the cube with random moves
- **Enter**: Automatically solve the cube
- **R**: Reset to a solved state
- **H**: Toggle help text
- **ESC**: Exit the application

## 💻 Technical Implementation

The project is built with multiple rendering approaches:

1. **OpenGL Implementation**: Direct 3D rendering with precise rotation physics
2. **URSINA Engine**: Modern game engine with enhanced visual effects
3. **Terminal-Based**: ASCII representation for command-line enthusiasts

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pygame
- PyOpenGL
- numpy
- ursina (for URSINA version)

### Installation

```bash
# Clone the repository
git clone https://github.com/VipranshOjha/Rubik-s-Cube.git
cd rubikscube

# Install dependencies
pip install pygame PyOpenGL numpy ursina

# Run the simulator
python main.py
```

## 📚 Learning Resources

This simulator is not just a game but also an educational tool:

- Practice solving algorithms
- Visualize cube rotations
- Understand 3D matrix transformations
- Study the layer-by-layer solving method

## 🛠️ Implementation Details

- **Face Detection**: Precise ray casting for accurate face selection
- **Rotation Animation**: Smooth transitions between cube states
- **State Management**: Tracks the position and orientation of each cubelet
- **Solving Algorithm**: Implements the beginner's method (layer by layer)

---

Enjoy solving! Remember, the Rubik's Cube has over 43 quintillion possible combinations, but only one solution. Happy cubing! 🧩
