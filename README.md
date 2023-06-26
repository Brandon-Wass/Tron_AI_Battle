# Tron_AI_Battle

This script is a Python program that creates a game called "Tron AI Battle". In this game, two players move around a game board, leaving trails behind them. The objective is to avoid running into the opponent's trail while trying to trap them with your own trail.

The script begins by importing the necessary libraries: pygame, random, time, and os. The pygame library is used to create the game graphics and handle event processing. The random library is used to randomize the players' starting positions and movements. The time library is used to keep track of the game duration. The os library is used to modify certain drivers for the game.

Next, the script defines several constants that will be used throughout the game. These constants include the screen size, player size, trail width, frames per second, game duration, and background color.

The script then initializes the game by calling pygame.init() and setting up the game display. The display consists of a window with the specified width and height, which is set to "pygame.NOFRAME" to create a window that cannot be minimized or closed. The window is also given a title caption that reads "Tron AI Battle". A clock is also created to keep track of the game's FPS.

Next, the script defines the Player class, which represents a player in the game. Each player has a color, starting position, direction, trail, and speed. The move() function is defined within the class, which updates the player's position and direction based on its current position and movement.

After defining the Player class, the script enters the main game loop. Within this loop, the players' colors, starting positions, and game settings are randomized for each new game. The inner game loop then handles various events, including quitting the game, moving the players, and drawing the game board.

At the end of the game loop, the game display is refreshed and the FPS is paused accordingly. The loop continues until the game is manually exited by the user.

----------------------------

Tron-like program written in python. This code consumes roughly 13% CPU when first launched while running on a Raspberry Pi 4B, but it becomes more CPU intensive as time progresses until it resets after the specified time.
