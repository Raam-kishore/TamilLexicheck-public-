import pandas as pd
import pickle

# Dumping data into the pickle file
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Read the contents of the file
file_contents = pd.read_csv('tamilwords.txt', encoding='utf-8')
file_contents.dropna()
file_contents.drop_duplicates()
tamil_words=open('words.pickle','rb+')
tamil_word=pickle.load(tamil_words)
print(tamil_word)
def find_closest_word(n):
    input_name=n
    threshold = 4
    closest_word = None
    min_distance = 4
    for word in tamil_word:
        distance = levenshtein_distance(word, input_name)

        if distance < min_distance:
            min_distance = distance
            closest_word = word
    print("Incorrect word :",input_name)
    print(f"Closest word and correct word name: {closest_word}")
    print("Edit distance between this word ",levenshtein_distance(input_name,closest_word))

input_word="ஆகாய"
if __name__=='__main__':
    find_closest_word(input_word)
