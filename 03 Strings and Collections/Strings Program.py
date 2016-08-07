__author__ = 'BeastV3'
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    # Create list called story words
    story_words = []
    # Loop over every line in story and Create list from line split method and store in line words
    for line in story:
        line_words = line.decode('utf-8').split()
        # For each word in line words list add the it to the story word list
        for word in line_words:
            # add words to end of words
            story_words.append(word)

print(story_words)
