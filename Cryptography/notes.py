import music21


def convert_notes_to_melody(note_string):
    melody = music21.stream.Stream()

    notes = note_string.split()

    for note in notes:
        n = music21.note.Note(note)
        melody.append(n)

    return melody


if __name__ == "__main__":
    note_input = input("Enter notes (for example, C4 D4 E4): ")

    melody = convert_notes_to_melody(note_input)

    midi_file = melody.write('midi')
    mf = music21.midi.MidiFile()
    mf.open("output.mid", "wb")
    mf.write(midi_file)
    mf.close()

    # Показать ноты в виде нотной записи
    melody.show()
