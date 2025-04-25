from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import json
import os

class NoteLayout(BoxLayout):
    pass

class NoteApp(App):
    def build(self):
        return NoteLayout()

    def save_note(self):
        note_text = self.root.ids.note_input.text.strip()
        if note_text:
            notes = self.load_notes()
            notes.append({"content": note_text})
            with open("notes.json", "w") as f:
                json.dump(notes, f)
            self.root.ids.note_input.text = ""

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json") as f:
                return json.load(f)
        return []

if __name__ == "__main__":
    NoteApp().run()
