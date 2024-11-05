import tkinter as tk

from .base import Alert

class ScreenAlert(Alert):
    
    def on_start(self):
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.configure(background='red')
        
        label = tk.Label(
            root,
            text="STOP BITING YOUR NAILS!",
            font=("Arial", 48),
            fg="white",
            bg="red"
        )
        label.place(relx=0.5, rely=0.5, anchor='center')
        
        root.after(2000, root.destroy)
        root.mainloop()
