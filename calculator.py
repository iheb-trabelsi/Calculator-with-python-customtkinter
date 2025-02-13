import customtkinter as ctk
import math

# Initialize the app
ctk.set_appearance_mode("Light")  # Options: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.memory = 0  # Memory storage

        # Display Field
        self.entry_var = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.entry_var, font=("Arial", 24), width=350, height=50)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button Layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C', '√', '^', 'log'),
            ('sin', 'cos', 'tan', 'M+')
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = ctk.CTkButton(self, text=text, font=("Arial", 20), width=80, height=60,
                                     command=lambda t=text: self.on_button_click(t))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
    
    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.entry_var.set(self.entry_var.get() + button_text)
        elif button_text in '+-*/':
            self.entry_var.set(self.entry_var.get() + ' ' + button_text + ' ')
        elif button_text == 'C':
            self.entry_var.set('')
        elif button_text == '=':
            try:
                self.entry_var.set(eval(self.entry_var.get()))
            except Exception:
                self.entry_var.set("Error")
        elif button_text == '√':
            try:
                self.entry_var.set(str(math.sqrt(float(self.entry_var.get()))))
            except Exception:
                self.entry_var.set("Error")
        elif button_text == '^':
            self.entry_var.set(self.entry_var.get() + ' ** ')
        elif button_text == 'log':
            try:
                self.entry_var.set(str(math.log10(float(self.entry_var.get()))))
            except Exception:
                self.entry_var.set("Error")
        elif button_text in ('sin', 'cos', 'tan'):
            try:
                value = float(self.entry_var.get())
                if button_text == 'sin':
                    self.entry_var.set(str(math.sin(math.radians(value))))
                elif button_text == 'cos':
                    self.entry_var.set(str(math.cos(math.radians(value))))
                elif button_text == 'tan':
                    self.entry_var.set(str(math.tan(math.radians(value))))
            except Exception:
                self.entry_var.set("Error")
        elif button_text == 'M+':
            try:
                self.memory = float(self.entry_var.get())
                self.entry_var.set('')
            except Exception:
                self.entry_var.set("Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
