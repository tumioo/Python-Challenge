
# storing file path
file = "paragraph_1.txt"

# declare variables
letter_count = 0

# opening file
with open(file, 'r') as txtfile:
    # reading file
    paragraph = txtfile.read()

    # finding word count
    word_count = paragraph.count(" ") + 1  # +1 to account for the last word

    # finding sentence count
    sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")

    # finding average letter count
    for character in paragraph:
        if character.isalpha():
            letter_count += 1  # counting how many characters are letters
    avg_letter_count = letter_count / word_count

    # finding average sentence length
    avg_sentence = word_count / sentence_count

# tests
# print(word_count)
# print(sentence_count)
print(letter_count)
# print(avg_letter_count)
# print(avg_sentence)

# printing results to terminal
print("Paragraph Analysis")
print("----------------------------------")
print("Approximate Word Count:", word_count)
print("Approximate Sentence Count:", sentence_count)
print("Average Letter Count:", avg_letter_count)
print("Average Sentence Length:", avg_sentence)

# creating the new text file
paragraph_out = open("paragraph_analysis.txt", "w")

# writing the text file
paragraph_out.write("Paragraph Analysis \n")
paragraph_out.write("---------------------------------- \n")
paragraph_out.write("Approximate Word Count: " + str(word_count) + "\n")
paragraph_out.write("Approximate Sentence Count: " + str(sentence_count) + "\n")
paragraph_out.write("Average Letter Count: " + str(avg_letter_count) + "\n")
paragraph_out.write("Average Sentence Length: " + str(avg_sentence))