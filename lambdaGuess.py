# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:30:10 2024

@author: berth
"""

import tkinter as tk
from tkinter import ttk
import os
import random
from PIL import Image, ImageTk, ImageOps
import glob


class WavelengthGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Lambda Guess")
        self.root.geometry("800x600")

        self.score = 0
        self.count = 0
        self.current_image_number = random.randint(0, len(glob.glob("./images/*_"))-1)
        self.current_wavelength = random.randrange(400, 710, 10)

        # Set up menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.create_menu()
        
        # Game Over Label
        self.game_over_label = ttk.Label(self.root, text="", font=("Arial", 20, "bold"), foreground="red")
        self.game_over_label.pack(padx=10, pady=10)

        # Create a big frame as the main container
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create a canvas for the main frame with a scrollbar
        self.canvas = tk.Canvas(self.main_frame, bg="white")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Create a frame inside the canvas to hold the content
        self.content_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        self.create_widgets()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_menu(self):
        # Add a menu with "Close" and "Start Game" options
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_command(label="Start Game", command=self.start_game)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.root.destroy)
        
        # Add a menu option to restart the game
        file_menu.add_command(label="Restart Game", command=self.restart_game)
        file_menu.add_separator()

    def create_widgets(self):
        # Load and display the background image
        background_path = "./image2.png"
        self.background_image = Image.open(background_path)
        self.background_image = self.background_image.resize((800, 600))
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_canvas = tk.Canvas(self.content_frame, width=800, height=600)
        self.background_canvas.pack()
        self.background_canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        # RGB Image
        self.rgb_label = ttk.Label(self.content_frame)
        self.rgb_label.pack(padx=10, pady=10)

        # Wavelength Image
        self.wavelength_label = ttk.Label(self.content_frame)
        self.wavelength_label.pack(padx=10, pady=10)

        # Entry for User Input
        entry_label = ttk.Label(self.content_frame, text="Enter Wavelength: X∈{400,410,420,…,690,700}")
        entry_label.pack(padx=10, pady=10)

        self.user_entry = ttk.Entry(self.content_frame)
        self.user_entry.pack(pady=(0, 5))  # Adjust the vertical padding

        # Submit Button
        submit_button = ttk.Button(self.content_frame, text="Submit", command=self.check_answer)
        submit_button.pack(pady=(0, 5))  # Adjust the vertical padding
        
        # Score Label
        self.score_label = ttk.Label(self.content_frame, text=f"Score: {self.score}")
        self.score_label.pack(padx=10, pady=10)
        
        # Next Button
        self.next_button = ttk.Button(self.content_frame, text="Next", state=tk.DISABLED, command=self.next_image)
        self.next_button.pack(pady=(0, 10))  # Adjust the vertical padding

    def load_images(self):
        # Load RGB Image
        rgb_path = os.path.join("./images/RGB", f"{self.current_image_number}.jpg")
        self.rgb_image = Image.open(rgb_path)
        self.rgb_image = self.rgb_image.resize((200, 200))  # Resize to a smaller size
        self.rgb_photo = ImageTk.PhotoImage(self.rgb_image)
    
        # Load Wavelength Image
        wavelength_path = os.path.join('./images/' + str(self.current_image_number) + '_',
                                       f"{self.current_image_number}_{self.current_wavelength}.png")
        self.wavelength_image = Image.open(wavelength_path)
        self.wavelength_image = self.wavelength_image.resize((200, 200))  # Resize to a smaller size
    
        # Rotate the wavelength image by 180 degrees
        self.wavelength_image = self.wavelength_image.rotate(180)
    
        # Add a mirror effect
        self.wavelength_image = ImageOps.mirror(self.wavelength_image)
    
        self.wavelength_photo = ImageTk.PhotoImage(self.wavelength_image)

    def update_images(self):
        # Update RGB Image
        self.rgb_label.configure(image=self.rgb_photo)
        self.rgb_label.image = self.rgb_photo

        # Update Wavelength Image
        self.wavelength_label.configure(image=self.wavelength_photo)
        self.wavelength_label.image = self.wavelength_photo

    def check_answer(self):
        user_input = self.user_entry.get()
        try:
            user_wavelength = int(user_input)
            if 400 <= user_wavelength <= 700:
                actual_wavelength = self.current_wavelength
                difference = abs(actual_wavelength - user_wavelength)
                points = max(0, 100 - difference)
                self.score += points

                # Disable user input and show correct response
                self.user_entry.config(state=tk.DISABLED)
                response_label = ttk.Label(self.content_frame, text=f"Correct response: {actual_wavelength}, Difference: {difference}")
                response_label.pack(padx=10, pady=5)

                # Enable the "Next" button
                self.next_button.config(state=tk.NORMAL)

            else:
                self.user_entry.delete(0, tk.END)
                self.user_entry.insert(0, "Enter a valid wavelength (400-700)")

        except ValueError:
            self.user_entry.delete(0, tk.END)
            self.user_entry.insert(0, "Enter a valid number")

    def next_image(self):
        # Reset UI for the next image
        self.user_entry.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
    
        # Clear user input field
        self.user_entry.delete(0, tk.END)
    
        self.count += 1
        if self.count <= 10:
            new_image_number = self.current_image_number
            while new_image_number == self.current_image_number:
                new_image_number = random.randint(0, len(glob.glob("./images/*_"))-1)
    
            new_wavelength = self.current_wavelength
            while new_wavelength == self.current_wavelength:
                new_wavelength = random.randrange(400, 710, 10)
    
            self.current_image_number = new_image_number
            self.current_wavelength = new_wavelength
    
            # Load and update the images for the new wavelength
            self.load_images()
            self.update_images()
    
            # Update the score label
            self.update_score_label()
    
            # Clear the response label
            for widget in self.content_frame.winfo_children():
                if isinstance(widget, ttk.Label) and widget.cget("text").startswith("Correct response"):
                    widget.destroy()
    
        else:
            # Display the "Game Over" banner with the final score
            self.game_over_label.config(text="Game Over! Final Score: {}".format(self.score))
            self.game_over_label.pack(padx=10, pady=10)

    def update_score_label(self):
        self.score_label.configure(text=f"Score: {self.score}")
    
    def restart_game(self):
        # Reset UI and game variables to start the game over
        self.game_over_label.config(text="")
        # self.background_canvas.pack(padx=10, pady=10)  # Show the background image again
        self.score = 0
        self.count = 0
        self.current_image_number = random.randint(0, len(glob.glob("./images/*_"))-1)
        self.current_wavelength = random.randrange(400, 710, 10)
        self.load_images()
        self.update_images()
        self.update_score_label()
        self.user_entry.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.user_entry.delete(0, tk.END)
        
        # Clear the response labels from the previous game
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("text").startswith("Correct response"):
                widget.destroy()

    def start_game(self):
        # Hide the background image
        self.background_canvas.pack_forget()

        # Reset the game variables and start the game
        self.score = 0
        self.count = 0
        self.current_image_number = random.randint(0, len(glob.glob("./images/*_"))-1)
        self.current_wavelength = random.randrange(400, 710, 10)
        self.load_images()
        self.update_images()
        self.update_score_label()


if __name__ == "__main__":
    root = tk.Tk()
    game = WavelengthGame(root)
    root.mainloop()