class Notes:
    """Класс для управления заметками"""

    def __init__(self):
        self.notes = []

    def add_notes(self, note):
        self.notes.append(note)

    def list_items(self):
        print('Список заметок')
        for note in self.notes:
            print(f'- {note}')

    def __str__(self):
        result = ''
        for contact in self.contacts:
            result += f'{contact.name}, {contact.phone}, {contact.email}\n'
        return result

    def __len__(self):
        return len(self.notes)