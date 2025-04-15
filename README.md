#Overview
Alien Invasion is a classic arcade-style space shooter game built with Pygame. Players control a spaceship at the bottom of the screen, defending Earth against descending alien invaders. The game features increasing difficulty, score tracking, multiple lives, and visual indicators for game state.

#Features
🚀 Spaceship control with smooth horizontal movement
👾 Fleets of aliens that move and descend
🔫 Bullet shooting mechanics with fire rate limits
💯 Scoring system with high score tracking
⚡ Progressive difficulty increase
❤️ Multiple lives system with visual indicators
� Level progression
🎮 Play button for game restart
🖥️ Responsive screen sizing

#Installation
Ensure you have Python 3.x installed
Install Pygame:
pip install pygame

#Game Controls
Left Arrow Key: Move ship left
Right Arrow Key: Move ship right
Space Bar: Fire bullets
Q Key: Quit game
Mouse Click: Press Play button when game is over

#File Structure
AlienInvasion/
├── alien.py           # Alien class implementation
├── alienInvasion.py   # Main game class
├── bullet.py          # Bullet class
├── button.py          # Play button implementation
├── game_stats.py      # Game statistics tracking
├── scoreboard.py      # Score display system
├── setting.py         # Game configuration settings
└── ship.py            # Player ship implementation

#Game Mechanics
The player starts with 3 lives (ships)
Each alien hit awards points (starting at 50)
The game speeds up after clearing each wave
Points per alien increase with each level
Game ends when aliens reach the bottom or all lives are lost

#Requirements
Python 3.x
Pygame library

#Customization
You can modify various game parameters in setting.py, including:
Screen dimensions
Ship, bullet, and alien speeds
Number of allowed bullets
Number of lives
Speed increase scaling
Scoring values

#Assets
The game uses two bitmap images:
ship.bmp - Player spaceship (scaled to 50x50)
alien.bmp - Alien invaders (scaled to 40x40)
Place these in an Images directory at C:/Users/accaz/AlienInvasion/Game/Images/ or modify the paths in ship.py and alien.py.

#Troubleshooting
If you encounter issues:
Verify Pygame is installed correctly
Check image file paths if you get loading errors
Ensure all game files are in the same directory
The game requires a display - it won't work in headless environments

#Future Enhancements
Potential improvements could include:
Different alien types with unique behaviors
Power-up systems
Sound effects and music
Boss battles
Mobile device support
