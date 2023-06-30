with open("input.txt", "r") as input_file:
    text = input_file.read()

word_count = len(text.split())

with open("output.txt", "w") as output_file:
    output_file.write(str(word_count))
    print(word_count)
