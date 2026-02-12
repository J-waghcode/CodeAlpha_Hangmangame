import tkinter as tk
import random

# ---------------- Game Data ----------------
words = ["python", "java", "django", "html", "robot"]
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# ---------------- Functions ----------------
def update_word():
    display = " ".join([l if l in guessed_letters else "_" for l in secret_word])
    word_label.config(text=display)

def check_guess():
    global wrong_guesses
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        status_label.config(text="⚠ Enter single letter only")
        return

    if guess in guessed_letters:
        status_label.config(text="⚠ Already guessed")
        return

    guessed_letters.append(guess)

    if guess in secret_word:
        status_label.config(text="✅ Correct!")
    else:
        wrong_guesses += 1
        status_label.config(text=f"❌ Wrong! Left: {max_wrong-wrong_guesses}")

    update_word()
    check_game()

def check_game():
    if all(l in guessed_letters for l in secret_word):
        status_label.config(text="🎉 You Win!")
        guess_btn.config(state="disabled")

    if wrong_guesses >= max_wrong:
        status_label.config(text=f"💀 Game Over! Word: {secret_word}")
        guess_btn.config(state="disabled")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Modern Hangman Game")
root.geometry("500x420")
root.configure(bg="#141421")

# -------- Card Frame (Border GUI) --------
card = tk.Frame(root, bg="#1e1e2f", bd=4, relief="ridge")
card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=340)

# Title
title = tk.Label(card, text="🎮 Hangman Game",
                 font=("Arial",18,"bold"),
                 bg="#1e1e2f", fg="#00ffcc")
title.pack(pady=15)

# Word display
word_label = tk.Label(card, text="",
                      font=("Consolas",24,"bold"),
                      bg="#1e1e2f", fg="white")
word_label.pack(pady=10)

# Entry
entry = tk.Entry(card,
                 font=("Arial",14),
                 justify="center",
                 bg="#2a2a40",
                 fg="white",
                 insertbackground="white",
                 relief="flat")
entry.pack(pady=10, ipady=5)

# Button
guess_btn = tk.Button(card,
                      text="Guess Letter",
                      command=check_guess,
                      bg="#00ffcc",
                      fg="black",
                      font=("Arial",12,"bold"),
                      padx=10,
                      pady=5,
                      relief="flat")
guess_btn.pack(pady=10)

# Status
status_label = tk.Label(card,
                        text="",
                        font=("Arial",12),
                        bg="#1e1e2f",
                        fg="yellow")
status_label.pack(pady=10)

update_word()
root.mainloop()
