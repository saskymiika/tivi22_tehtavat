
from tkinter import Tk, ttk

class GUI:
    """This class uses tkinter library to create graphical user interfaces."""
    def __init__(self, name: str):
        self.root = Tk()
        self.root.title(name.title())
        self.run = self.root.mainloop
        self.end = self.root.destroy
        self.frames = []
        self.styles = {}

    def defaults(self, styles: dict):
        """usage: 'classname': {values...}"""
        self.styles = styles

    def set_app_icon(self, icon_path: str):
        self.root.iconbitmap(icon_path)

    def add_frame(self, classname=None):
        frame = ttk.Frame(self.root)

        if classname != None:
            self.assign_styles(classname, frame)

        self.frames.append(frame)
        return frame

    def remove_frames(self):
        """Removes all frames within the application window."""
        while len(self.frames) > 0:
            self.frames[0].destroy()
            self.frames.pop(0)

    def remove_frame_at(self, index: int):
        """Removes a frame at specific index in self.frames list."""
        self.frames[index].destroy()
        self.frames.pop(index)

    def label(self, frame: ttk.Frame, text: str, classname=None):
        label = ttk.Label(frame, text=text)
        if classname != None:
            self.assign_styles(classname, label)
        return label

    def button(self, frame: ttk.Frame, text: str, callback=lambda: None, classname=None):
        button = ttk.Button(frame, text=text, command=callback)
        if classname != None:
            self.assign_styles(classname, button)
        return button

    def assign_styles(self, classname: str, item):
        if self.styles[classname] != None:
            item.config(**self.styles[classname])

    def entry(self, frame: ttk.Frame, type=None, classname=None):
        entry = ttk.Entry(frame)
        if classname != None:
            self.assign_styles(classname, entry)
        if type != None and type.lower() == "password":
            entry.config(show="*")
        return entry

