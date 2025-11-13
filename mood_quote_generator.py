import requests
from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Fetch quotes
# -------------------------------
def get_quotes():
    try:
        response = requests.get("https://zenquotes.io/api/quotes")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load quotes: {e}")
        return []

# -------------------------------
# Mood detection
# -------------------------------
def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

# -------------------------------
# Quote matching
# -------------------------------
def categorize_quote(quote):
    blob = TextBlob(quote)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def find_matching_quote(mood, quotes):
    for q in quotes:
        if categorize_quote(q["q"]) == mood:
            return q
    return quotes[0] if quotes else None

# -------------------------------
# GUI Logic
# -------------------------------
def generate_quote():
    user_input = mood_entry.get()
    if not user_input.strip():
        messagebox.showwarning("Wait", "Please describe your mood first 💬")
        return

    mood = analyze_mood(user_input)
    quotes = get_quotes()
    match = find_matching_quote(mood, quotes)

    # Updated richer mood colours
    if mood == "positive":
        bg_color, fg_color, emoji = "#2E8B57", "#F0FFF0", "😄"     # SeaGreen
    elif mood == "negative":
        bg_color, fg_color, emoji = "#8B0000", "#FFF5F5", "😔"     # DarkRed
    else:
        bg_color, fg_color, emoji = "#3A3A3A", "#EAEAEA", "😐"     # Slate Grey

    root.config(bg=bg_color)
    title_label.config(bg=bg_color, fg=fg_color)
    mood_label.config(text=f"Detected mood: {emoji} {mood.capitalize()}", bg=bg_color, fg=fg_color)
    input_frame.config(bg=bg_color)
    mood_entry.config(bg="#222", fg="#EEE", insertbackground="#EEE")
    ask_label.config(bg=bg_color, fg=fg_color)
    quote_box.config(text=f"“{match['q']}”\n\n— {match['a']}", bg="#111", fg="#EEE")

# -------------------------------
# GUI Design
# -------------------------------
root = tk.Tk()
root.title("💡 Mood-Based Quote Generator")
root.geometry("650x420")
root.configure(bg="#3A3A3A")

title_label = tk.Label(root, text="💡 Mood-Based Quote Generator", font=("Helvetica", 18, "bold"), bg="#3A3A3A", fg="#EAEAEA")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#3A3A3A")
input_frame.pack(pady=10)

ask_label = tk.Label(input_frame, text="How are you feeling today?", font=("Helvetica", 12), bg="#3A3A3A", fg="#EAEAEA")
ask_label.pack(side=tk.LEFT, padx=5)

mood_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12), bg="#222", fg="#EEE", bd=2, relief="flat", insertbackground="#EEE")
mood_entry.pack(side=tk.LEFT, padx=5)

def on_hover(e):
    generate_button.config(bg="#FFA726")
def on_leave(e):
    generate_button.config(bg="#FB8C00")

generate_button = tk.Button(root, text="Inspire Me 🌟", font=("Helvetica", 12, "bold"), bg="#FB8C00", fg="#111", relief="raised", padx=15, pady=5, command=generate_quote)
generate_button.pack(pady=10)
generate_button.bind("<Enter>", on_hover)
generate_button.bind("<Leave>", on_leave)

mood_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), bg="#3A3A3A", fg="#EAEAEA")
mood_label.pack(pady=5)

quote_box = tk.Label(root, text="", wraplength=500, justify="center", font=("Georgia", 13, "italic"), bg="#111", fg="#EEE", padx=15, pady=15, relief="flat")
quote_box.pack(pady=15)

root.mainloop()
