import random
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AdvancedGuessGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Arcade Number Guesser")
        self.geometry("450x450")
        
        # Game State Variables
        self.secret_number = 0
        self.attempts = 0
        self.max_range = 100
        self.score_multiplier = 10
        
        self.setup_ui()
        self.start_new_game()

    def setup_ui(self):
        # Title
        self.title_label = ctk.CTkLabel(self, text="🎮 NUMBER GUESSER ARCADE 🎮", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=15)
        
        # Difficulty Selector Label
        self.diff_label = ctk.CTkLabel(self, text="Select Difficulty:", font=("Arial", 12))
        self.diff_label.pack(pady=2)
        
        # Difficulty Segmented Button (Tabs)
        self.diff_switch = ctk.CTkSegmentedButton(
            self, 
            values=["Easy (1-10)", "Medium (1-100)", "Hard (1-1000)"],
            command=self.change_difficulty
        )
        self.diff_switch.set("Medium (1-100)")
        self.diff_switch.pack(pady=5)
        
        # Game Prompt
        self.prompt_label = ctk.CTkLabel(self, text="Guess the number!", font=("Arial", 15))
        self.prompt_label.pack(pady=15)
        
        # Input Box
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your guess", width=150)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess()) # Press Enter to submit
        
        # Submit Button
        self.btn_submit = ctk.CTkButton(self, text="Submit Guess", command=self.check_guess)
        self.btn_submit.pack(pady=5)
        
        # Stats Display (Attempts & Live feedback)
        self.stats_label = ctk.CTkLabel(self, text="Attempts: 0", font=("Arial", 13, "italic"))
        self.stats_label.pack(pady=5)
        
        # Result message
        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=15)
        
        # Play Again Button (Hidden initially)
        self.btn_reset = ctk.CTkButton(self, text="Play Again 🔄", fg_color="green", hover_color="darkgreen", command=self.start_new_game)

    def change_difficulty(self, value):
        if value == "Easy (1-10)":
            self.max_range = 10
            self.score_multiplier = 1
        elif value == "Medium (1-100)":
            self.max_range = 10
            self.score_multiplier = 10
        elif value == "Hard (1-1000)":
            self.max_range = 1000
            self.score_multiplier = 100
        self.start_new_game()

    def start_new_game(self):
        self.secret_number = random.randint(1, self.max_range)
        self.attempts = 0
        
        # Reset UI elements
        self.prompt_label.configure(text=f"Guess a number between 1 and {self.max_range}:")
        self.stats_label.configure(text="Attempts: 0")
        self.result_label.configure(text="")
        self.entry.delete(0, 'end')
        self.entry.configure(state="normal")
        self.btn_submit.configure(state="normal")
        self.diff_switch.configure(state="normal")
        self.btn_reset.pack_forget() # Hide reset button

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.stats_label.configure(text=f"Attempts: {self.attempts}")
            self.entry.delete(0, 'end') # Clear input for next guess
            
            if guess < self.secret_number:
                self.result_label.configure(text="Too low! 📉", text_color="orange")
            elif guess > self.secret_number:
                self.result_label.configure(text="Too high! 📈", text_color="orange")
            else:
                self.handle_win()
                
        except ValueError:
            self.result_label.configure(text="⚠️ Enter a valid number!", text_color="red")

    def handle_win(self):
        # Calculate dynamic score
        base_points = max(10, 100 - ((self.attempts - 1) * 10)) 
        final_score = base_points * self.score_multiplier
        
        # Display Win state
        self.result_label.configure(
            text=f"🎉 CORRECT! 🎉\n\n✨ Final Score: {final_score} pts ✨\n(Multiplier: {self.score_multiplier}x)", 
            text_color="#4CAF50"
        )
        
        # Freeze inputs until they hit restart
        self.entry.configure(state="disabled")
        self.btn_submit.configure(state="disabled")
        self.diff_switch.configure(state="disabled")
        self.btn_reset.pack(pady=10) # Shows play again button

if __name__ == "__main__":
    app = AdvancedGuessGame()
    app.mainloop()

