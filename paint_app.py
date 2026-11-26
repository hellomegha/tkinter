from logging import root
import tkinter as tk

class PaintApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Paint App")
        self.geometry("600x450")
        self.resizable(False, False)

        self.current_color = "black"
        self.last_x, self.last_y = None, None

        self.create_widgets()

    def create_widgets(self):

        toolbar = tk.Frame(self, pady=5)
        toolbar.pack(side="top", fill="x")

        colors = ["black", "red", "blue", "green", "purple"]
        for color in colors:
            btn = tk.Button(toolbar, bg=color, width=3, command=lambda c=color: self.set_color(c))
            btn.pack(side="left", padx=2)

        tk.Button(toolbar, text="Clear", command=self.clear_canvas).pack(side="right", padx=10)

        self.canvas = tk.Canvas(self, bg="white", width=580, height=380)
        self.canvas.pack(pady=10)

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def set_color(self, color):
        self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.current_color, width=2, capstyle=tk.ROUND)
        self.last_x, self.last_y = x, y

root = tk.Tk()
root.title("Text Editor with Toolbar and Status Bar")
root.geometry("500x400")

toolbar = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar, text="Open").pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Save").pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Clear").pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill="x")

# Text widget
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=5, pady=5)

# Status bar
status_label = tk.Label(root, text="Ready", bd=1, relief="sunken", anchor="w")
status_label.pack(side="bottom", fill="x")

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)


help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()
root.mainloop()