from collections import deque

def write_output(line):
    new_line = f'{line}\n'
    with open('output.txt', 'a+') as writer:

        writer.write(new_line)

        writer.close()

def add_information(line, sentence):
    letters = 0
    punctuation_marks = 0

    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char != ' ':
            punctuation_marks += 1

    end_result = f'Line {line}: {sentence} ({letters})({punctuation_marks})'
    write_output(end_result)


with open('text.txt', 'r') as reader:

    sentences = deque(reader.read().split('\n'))
    line = 1
    while sentences:

        add_information(line, sentences.popleft())
        line += 1

    reader.close()