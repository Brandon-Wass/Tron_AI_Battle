#!/usr/bin/python3

import pygame
import random
import time
import os

# Driver modifiers
#os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

# Save the screen surface to a seperate file, un-comment to enable saving output to another file
#pygame.image.save(screen, "./background_image/output.mp4")

# Define constants
WIDTH = 1200
HEIGHT = 692
SIZE = 3  # Player size
TRAIL_WIDTH = 1  # Trail width
FPS = 60
BG_COLOR = (0, 0, 0)
GAME_DURATION = 60 * 60  # Game duration in seconds

# Initialize the game
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, 8) # 0=regular display window // pygame.NOFRAME=window that cannot be minimized or closed
pygame.display.set_caption("Tron AI Battle")
clock = pygame.time.Clock()

# Define the Player class
class Player:
    def __init__(self, color, start_pos):
        self.color = color
        self.x, self.y = start_pos
        self.direction = random.choice(["up", "down", "left", "right"])
        self.trail = []
        self.speed = SIZE

    def move(self, players):
        directions = ["up", "down", "left", "right"]
        valid_directions = []

        # Determine the player's valid directions based on the boundaries and walls
        if self.direction == "up":
            if self.y > 0:
                valid_directions = ["up", "left", "right"]
            else:
                valid_directions = ["left", "right"]
        elif self.direction == "down":
            if self.y < HEIGHT - SIZE:
                valid_directions = ["down", "left", "right"]
            else:
                valid_directions = ["left", "right"]
        elif self.direction == "left":
            if self.x > 0:
                valid_directions = ["up", "down", "left"]
            else:
                valid_directions = ["up", "down"]
        elif self.direction == "right":
            if self.x < WIDTH - SIZE:
                valid_directions = ["up", "down", "right"]
            else:
                valid_directions = ["up", "down"]

        # Choose the next direction randomly from the valid directions
        if valid_directions:
            self.direction = random.choice(valid_directions)

        # Move the player and add their previous position to their trail
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
        self.trail.append((self.x, self.y))

    def draw(self):
        # Draw the player
        pygame.draw.rect(screen, self.color, (self.x, self.y, SIZE, SIZE))

        # Draw the player's trail
        for i in range(len(self.trail)-1):
            start_pos = self.trail[i]
            end_pos = self.trail[i+1]
            pygame.draw.line(screen, self.color, start_pos, end_pos, TRAIL_WIDTH)

# Main game loop
start_time = time.time()
while True:
    # Reset the game
    player_one_color = (255,0,75)
    player_one_start_pos = (random.randint(0, WIDTH-SIZE), random.randint(0, HEIGHT-SIZE))
    player_two_color = (255,0,150)
    player_two_start_pos = (random.randint(0, WIDTH-SIZE), random.randint(0, HEIGHT-SIZE))
    player_one = Player(player_one_color, player_one_start_pos)
    player_two = Player(player_two_color, player_two_start_pos)

    # Game loop for a single game
    game_start_time = time.time()
    while time.time() - game_start_time < GAME_DURATION:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move the players
        player_one.move([player_two])
        player_two.move([player_one])

        # Draw the players and update the display
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, (255, 0, 255), (0, 0, WIDTH, HEIGHT), 2)
        player_one.draw()
        player_two.draw()
        pygame.display.flip()

        # Pause for the specified FPS
        clock.tick(FPS)
        pygame.display.update()
