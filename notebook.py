import datetime
# Store the next available id for all new notes

last_id=0
class Note:
  '''Represent a note in the notebook. Match against a
  string in searches and store tags for each note.'''

  def __init__(self, memo, tags='', creation_date=''):
    '''initialize a note with memo and optional
    space-separated tags. Automatically set the note's
    creation date and a unique id.'''

    self.memo = memo
    self.tags = tags
    if creation_date is None:
      self.creation_date = datetime.date.today()
    else:
      self.creation_date = datetime.datetime.strptime(creation_date,"%Y-%m-%d").date()
    global last_id
    last_id += 1
    self.id = last_id

  def match(self, filter):
    '''Determine if this note matches the filter
    text. Return True if it matches, False otherwise.
    Search is case sensitive and matches both text and
    tags.'''

    return filter in self.memo or filter in self.tags 
  
  def match_year(self, filter):
    temp_date = self.creation_date.strftime("%Y")
    return filter in temp_date
    
class Notebook:
  '''Represent a collection of notes that can be tagged,
  modified, and searched.'''

  def __init__(self):
    '''Initialize a notebook with an empty list.'''

    self.notes = []
    lines = open("notebook.txt").readlines()
    for line in lines:
      list1 = line.split(",")[:4]
      memo = list1[1]
      tags = list1[2]
      creation_date = list1[3]
      self.notes.append(Note(memo, tags, creation_date))

  def new_note(self, memo,creation_date, tags=''):
    '''Create a new note and add it to the list.'''

    self.notes.append(Note(memo, tags, creation_date))

  def modify_memo(self, note_id, memo, creation_date):
    '''Find the note with the given id and change its
    memo to the given value.'''

    for note in self.notes:
      if note.id == note_id:
        note.memo = memo
        break

  def modify_tags(self, note_id, tags):
    '''Find the note with the given id and change its
    tags to the given value.'''

    for note in self.notes:
      if note.id == note_id:
        note.tags = tags
        break

  def search(self, filter):
    '''Find all notes that match the given filter
    string.'''

    return [note for note in self.notes if note.match(filter)]

  def search_year(self, filter):
    return [note for note in self.notes if note.match_year(filter)]

  def save_notes(self):
    file_h = open("notebook.txt","w")
    for note in self.notes:
      temp_id = note.id
      temp_memo = note.memo
      temp_tag = note.tags 
      temp_date = note.creation_date.strftime("%Y-%m-%d")
      temp_string = "{},{},{},{},".format(temp_id,temp_memo,temp_tag,temp_date)
      file_h.write(temp_string)
      file_h.write("\n")
    file_h.close()
