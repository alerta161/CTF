import music21


def convert_notes_to_melody(note_string):
    melody = music21.stream.Stream()

    # Разделение введенных нот по пробелам и обработка каждой ноты
    notes = note_string.split()

    for note in notes:
        n = music21.note.Note(note)
        melody.append(n)

    return melody


if __name__ == "__main__":
    # Получить ввод пользователя
    note_input = input("Введите ноты (например, C4 D4 E4): ")

    # Конвертировать введенные ноты в мелодию
    melody = convert_notes_to_melody(note_input)

    # Воспроизвести мелодию
    midi_file = melody.write('midi')
    mf = music21.midi.MidiFile()
    mf.open("output.mid", "wb")
    mf.write(midi_file)
    mf.close()

    # Показать ноты в виде нотной записи
    melody.show()