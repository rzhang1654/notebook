#!/bin/env python
import datetime
import sys
from notebook import Notebook, Note
class Menu(object):
  '''Display a menu and respond to choices when run.'''
  def __init__(self):
    self.notebook = Notebook()
    self.choices = {
      "1": self.show_notes,
      "2": self.search_notes,
      "3": self.search_years,
      "4": self.add_note,
      "5": self.modify_note,
      "6": self.quit
    }

  def display_menu(self):
    print("""
Notebook Menu
1. Show all Notes
2. Search Memos and Tags
3. Search by Year
4. Add Note
5. Modify Note
6. Quit
""")

  def run(self):
    '''Display the menu and respond to choices.'''
    while True:
      self.display_menu()
      choice = input("Enter an option: ")
      action = self.choices.get(choice)
      if action:
        action()
      else:
        print("{0} is not a valid choice".format(choice))


  def show_notes(self, notes=None):
    if type(notes) != list:
      notes = self.notebook.notes
    for note in notes:
      print("ID:{0},TAGS:{1},MEMO:{2},DATE:{3}".format(note.id, note.tags, note.memo, note.creation_date))
    

  def search_notes(self):
    filter = input("Search for: ")
    notes = self.notebook.search(filter)
    self.show_notes(notes)

  def search_years(self):
    filter = input("Search For: ")
    notes = self.notebook.search_year(filter)
    self.show_notes(notes)

  def add_note(self):
    memo = input("Enter a memo: ")
    creation_date1 = datetime.date.today()
    creation_date = creation_date1.strftime("%Y,%m,%d")
    self.notebook.new_note(memo, creation_date)
    print("Your note has been added.")

  def save_notebook(self):
    self.notebook.save_notes()

  def modify_note(self):
    id = input("Enter a note id: ")
    memo = input("Enter a memo: ")
    tags = input("Enter tags: ")
    if memo:
      self.notebook.modify_memo(int(id), memo)
    if tags:
      self.notebook.modify_tags(int(id), tags)
  
  def quit(self):
    self.save_notebook()
    print("Your Notes Have Been Saved.")
    print("Thank you for using your notebook today.")
    sys.exit(0)

if __name__ == "__main__":
  Menu().run()


