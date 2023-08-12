import os
import json


def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print(f'{indentation}{value}')


class Entry:
    def __init__(self, title, entries=None, parent=None):
        self.title = title
        if entries is None:
            entries = []
        self.entries = entries
        self.parent = parent

    """
    The class method from_json takes a dict (JSON) and returns an object of the Entry class, 
    with data and nesting from the input JSON.
    """
    @classmethod
    def from_json(cls, value):
        entry = cls(value['title'])
        for sub_entry in value.get('entries', []):
            entry.add_entry(cls.from_json(sub_entry))
        return entry

    """
    - Opens the specified file in read mode
    - Loads the content of the file into a dict
    - Returns an object of the Entry class, created from the loaded dict using the existing from_json method
    """
    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            content = json.load(f)
            return cls.from_json(content)

    """
    The method takes a new entry (an object of the Entry class) and adds it to the entries list of the current record. 
    The parent record of the added entry is also assigned here.
    """
    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    """
    The print_entries method uses the print_with_indent function and outputs the entries, 
    taking into account their nesting.
    """
    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent=indent + 1)

    """
    The method returns an object of the Entry class in the form of a dict with two keys: title and entries.
    """
    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    """
    The method saves the dict returned by the self.json() method to a file in the specified directory
    with a name corresponding to the title of the record in JSON format (i.e., f'{self.title}.json').
    """
    def save(self, path):
        filename = os.path.join(path, self.title)
        content = self.json()
        with open(f'{filename}.json', 'w') as f:
            json.dump(content, f)

    def __str__(self):
        return self.title


class EntryManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.entries = []

    """
    - Iterates through all the files in the self.data_path directory (using os.listdir)
    - If a file has the .json extension (i.e., its filename ends with .json), then:
        - Loads the record from the file using the Entry.load() method
        - Adds the loaded entry to self.entries
    """
    def load(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        else:
            for filename in os.listdir(self.data_path):
                if filename.endswith('json'):
                    entry = Entry.load(os.path.join(self.data_path, filename))
                    self.entries.append(entry)
        return self

    """
    This method is designed to save all the entries from the self.entries list
    to files in the EntryManager class's data_path directory.
    """
    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    """
    Creates a new entry and adds it to the manager.

    Args:
    title (str): The title of the new entry.
    """
    def add_entry(self, title: str):
        entry = Entry(title)
        self.entries.append(entry)
