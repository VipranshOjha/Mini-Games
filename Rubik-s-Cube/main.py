import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import time

# Import your RubiksCube3D class
from RubiksCube4 import RubiksCube3D
from Solver import CubeSolver 

class CubeScrambler:
    def __init__(self, cube_instance):
        self.cube = cube_instance
        self.moves = ['x', 'y', 'z']
        self.indices = [-1, 1]  # Outer layers
        self.directions = [-1, 1]

    def generate_random_move(self):
        """Generate a random move (axis, layer, direction)"""
        axis = random.choice(self.moves)
        index = random.choice(self.indices)
        direction = random.choice(self.directions)
        return axis, index, direction

    def scramble(self, num_moves=20):
        """Scramble the cube with random moves"""
        print("Scrambling cube...")
        scramble_sequence = []

        for _ in range(num_moves):
            axis, index, direction = self.generate_random_move()
            self.cube.start_rotation(axis, index, direction)
            scramble_sequence.append((axis, index, direction))

            while self.cube.animating:
                self.cube.update_animation()
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                self.cube.draw_cube()
                pygame.display.flip()
                pygame.time.wait(16)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

            pygame.time.wait(100)

        print("Scramble complete!")
        return scramble_sequence


class RubiksCubeGame:
    def __init__(self):
        self.cube = RubiksCube3D()
        self.scrambler = CubeScrambler(self.cube)
        self.solver = CubeSolver(self.cube) 
        self.running = True
        self.show_help = False

    def handle_extended_events(self, event):
        """Handle extra key events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Scramble cube
                self.scrambler.scramble()
            elif event.key == pygame.K_RETURN:
                # Solve the cube
                print("Solving cube...")
                self.solver.solve()
                print("Solution applied!")
            elif event.key == pygame.K_r:
                # Reset cube
                self.cube = RubiksCube3D()
                self.scrambler = CubeScrambler(self.cube)
                self.solver = CubeSolver(self.cube)
            elif event.key == pygame.K_h:
                self.show_help = not self.show_help
            elif event.key == pygame.K_ESCAPE:
                self.running = False

    def render_help_text(self):
        """Display help text"""
        if self.show_help:
            print("\nControls:")
            print("  Left-click and drag: Rotate the cube")
            print("  Space: Scramble the cube")
            print("  Enter: Solve the cube")
            print("  R: Reset the cube")
            print("  H: Toggle help")
            print("  Esc: Exit")

    def run(self):
        """Main game loop"""
        while self.running:
            self.cube.update_animation()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                    self.cube.handle_event(event)
                else:
                    self.handle_extended_events(event)

            self.cube.draw_cube()

            if self.show_help:
                self.render_help_text()

            pygame.display.flip()
            pygame.time.wait(16)

        pygame.quit()


if __name__ == "__main__":
    game = RubiksCubeGame()
    game.run()
