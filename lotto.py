import tkinter as tk
import random





def on_button_click():
    zahlen= list(range(1,50))
    random.shuffle(zahlen)
   
    label.config(text=zahlen[:6])

# Hauptfenster erstellen
root = tk.Tk()
root.title("Lottozahlen")
# >>>>> root.geometry("400x300") 

# Label erstellen
label = tk.Label(root, text="Lotto start")
label.pack(pady=10)

# Button erstellen
button = tk.Button(root, text="Klick!", command=on_button_click)
button.pack(pady=20,padx=20)

# Hauptschleife starten
root.mainloop()
