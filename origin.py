import re

def find_heritability_words(input_file, output_file):
    pattern = r'\b(heritable|inherit|inheritance|inherited)\b'
    with open(input_file, 'r') as in_stream, open(output_file, 'w') as out_stream:
        for line_num, line in enumerate(in_stream, start=1):
            matches = re.findall(pattern, line, flags=re.IGNORECASE)
            for word in matches:
                out_stream.write(f'{line_num}\t{word}\n')

if __name__ == '__main__':
    input_file = 'origin.txt'
    output_file = 'heritability_words.txt'
    find_heritability_words(input_file, output_file)
    print('Words related to heritability have been extracted to heritability_words.txt')
