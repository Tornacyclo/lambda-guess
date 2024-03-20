# lambda-guess
---
## Wavelength Guessing Game

### Introduction
This Python program implements a simple guessing game called "Lambda Guess." The game presents users with images of light spectra and asks them to guess the corresponding wavelength. It utilizes the Tkinter library for creating the graphical user interface (GUI) and the Pillow library for image processing.

### Features
- **Random Image Selection**: The game randomly selects images representing different light spectra for each round.
- **Wavelength Range**: Users are asked to guess the wavelength within a specified range (400 to 700 nanometers).
- **Scoring System**: Users earn points based on the accuracy of their guesses. Points are awarded according to how close their guess is to the actual wavelength.
- **User Feedback**: After each guess, users receive feedback on the correctness of their response and the difference between their guess and the actual wavelength.
- **Game Over**: The game ends after a set number of rounds, and the final score is displayed.
- **Restart Option**: Users have the option to restart the game at any time, resetting the score and starting from the beginning.
- **Menu Options**: The program includes a menu with options to start the game, restart the game, and close the application.

### Components
- **Main Frame**: The main frame contains the canvas for displaying images and a scrollbar for navigation.
- **Content Frame**: Inside the canvas, the content frame holds all the interactive elements of the game.
- **Background Image**: A background image is displayed behind the game elements for aesthetic purposes.
- **User Interface Elements**: These include labels for displaying images, entry fields for user input, buttons for submitting answers and navigating between rounds, and a label for displaying the score.
- **Menu Bar**: The menu bar provides access to game options such as starting, restarting, and closing the game.

### Usage
1. **Starting the Game**: Users can start the game by selecting the "Start Game" option from the menu.
2. **Guessing Wavelengths**: Users input their guesses for the wavelength displayed in the images.
3. **Scoring**: Points are awarded based on the accuracy of the guesses.
4. **Game Over**: After a set number of rounds, the game ends, and the final score is displayed.
5. **Restarting the Game**: Users can restart the game at any time using the "Restart Game" option from the menu.
6. **Closing the Application**: The application can be closed by selecting the "Close" option from the menu or closing the window.

### Dependencies
- Tkinter: Python's standard GUI library for creating the user interface.
- Pillow: A Python Imaging Library (PIL) fork used for image processing tasks.

### How to Run
1. Ensure Python and the required libraries (Tkinter, Pillow) are installed.
2. Execute the provided Python script (`wavelength_game.py`).
3. The game window will appear, allowing users to interact with the game.

### Contribution
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### Datasets
ICVL http://icvl.cs.bgu.ac.il/hyperspectral <br/>
