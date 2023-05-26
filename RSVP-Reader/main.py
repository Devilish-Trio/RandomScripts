import time
import tkinter as tk
import tkinter.filedialog
import ebooklib
import re
import os
import json
from ebooklib import epub
from bs4 import BeautifulSoup


class EPUBReader:
    def __init__(self, text):
        self.text = text

        self.root = tk.Tk()
        self.root.title("EPUB Reader")

        self.text_widget = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 14))
        self.text_widget.insert(tk.END, self.text)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        self.root.mainloop()


class RsvpRead:
    def __init__(self, text, file_path, wpm=300, start_from_beginning=False):
        self.text = text
        self.file_path = file_path
        self.words = self.text.split()
        self.wpm = wpm
        self.word_delay = 60 / self.wpm
        self.paused = False
        self.current_word_index = 0 if start_from_beginning else self.load_last_word_index()

        self.root = tk.Tk()
        self.root.title("RSVP Read")

        self.canvas = tk.Canvas(self.root, width=600, height=200)
        self.canvas.pack()

        self.progress_label = tk.Label(self.root, text="", anchor="e", justify="right")
        self.progress_label.pack(side="bottom", fill="both", expand=True)

        self.start()

    def update_wpm(self, delta):
        self.wpm += delta
        self.word_delay = 60 / self.wpm
        self.update_progress_label()

    def update_progress_label(self):
        progress_percentage = (self.current_word_index + 1) / len(self.words) * 100
        self.progress_label.config(
            text=f"Word: {self.current_word_index + 1}/{len(self.words)} ({progress_percentage:.2f}%) | WPM: {self.wpm}")

    def display_word(self, word):
        middle_index = len(word) // 2
        center_x = 300
        center_y = 100
        char_width = 28

        start_x = center_x - char_width * middle_index

        for i, char in enumerate(word):
            color = "orange" if i == middle_index else "black"
            x = start_x + i * char_width
            self.canvas.create_text(x, center_y, text=char, fill=color, font=("Helvetica", 24))

    def start(self):
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("<Up>", lambda event: self.update_wpm(10))
        self.root.bind("<Down>", lambda event: self.update_wpm(-10))

        for i in range(self.current_word_index, len(self.words)):
            while self.paused:
                self.root.update()
                time.sleep(0.1)

                if not self.root:
                    return

            if not self.root:
                return

            self.canvas.delete("all")
            self.display_word(self.words[i])
            self.current_word_index = i
            self.save_last_word_index()

            self.update_progress_label()

            self.root.update()
            time.sleep(self.word_delay)

        self.root.mainloop()

    def toggle_pause(self, event):
        self.paused = not self.paused

    def load_last_word_index(self):
        save_file = f"{os.path.splitext(self.file_path)[0]}.json"
        if os.path.exists(save_file):
            with open(save_file, "r") as f:
                return json.load(f)["last_word_index"]
        return 0

    def save_last_word_index(self):
        save_file = f"{os.path.splitext(self.file_path)[0]}.json"
        with open(save_file, "w") as f:
            json.dump({"last_word_index": self.current_word_index}, f)



def get_epub_text(file_path):
    book = epub.read_epub(file_path)
    full_text = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")

            # Remove formatting tags
            for tag in soup(["i", "b", "u", "strong", "em"]):
                tag.unwrap()

            # Remove reference links
            text = re.sub(r'\[\d+\]', '', soup.get_text())

            full_text += text + "\n"

    return full_text

def main(file_path):
    epub_text = get_epub_text(file_path)

    print("Select an option:")
    print("1. RSVP")
    print("2. Normal Reading")

    option = input("Enter 1 or 2: ")

    if option == "1":
        wpm = 400
        start_from_beginning = input("Start from the beginning? (y/n): ").lower() == "y"
        app = RsvpRead(epub_text, file_path, wpm, start_from_beginning)
    elif option == "2":
        app = EPUBReader(epub_text)
    else:
        print("Invalid option.")
        return

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])

    if file_path:
        main(file_path)
    else:
        print("No file selected.")
