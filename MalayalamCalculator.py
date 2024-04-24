import tkinter as tk

def malayalam_to_english(text):
    # Replace Malayalam numerals with English numerals
    return text.replace("൦", "0").replace("൧", "1").replace("൨", "2").replace("൩", "3").replace("൪", "4").replace("൫", "5").replace("൬", "6").replace("൭", "7").replace("൮", "8").replace("൯", "9")

def english_to_malayalam(number):
    # Convert numeric result to Malayalam numerals
    return str(number).translate(str.maketrans("0123456789", "൦൧൨൩൪൫൬൭൮൯"))

def perform_calculation():
    current_text = entry.get()
    try:
        # Convert Malayalam numerals to English numerals before evaluation
        current_text = malayalam_to_english(current_text)
        # Replace multiplication symbol for correct evaluation
        current_text = current_text.replace("x", "*")
        result = eval(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, english_to_malayalam(result))  # Display result in Malayalam numerals
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        perform_calculation()
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        if entry.get() == "Error":
            entry.delete(0, tk.END)
        entry.insert(tk.END, button_text)

# Create the main application window
root = tk.Tk()
root.title("ആൽബിൻ ഗണകയന്")  # Albin Da Calculator (in Malayalam)

# Entry widget to display the calculation and results
entry = tk.Entry(root, font=("Kartika", 25), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for Malayalam numerals and operators
button_texts = [
    ("൭", 1, 0), ("൮", 1, 1), ("൯", 1, 2), ("/", 1, 3),
    ("൪", 2, 0), ("൫", 2, 1), ("൬", 2, 2), ("x", 2, 3),
    ("൧", 3, 0), ("൨", 3, 1), ("൩", 3, 2), ("-", 3, 3),
    ("൦", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons and bind events
for text, row, col in button_texts:
    button = tk.Button(root, text=text, font=("Kartika", 25), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", click)

# Start the main event loop
root.mainloop()
