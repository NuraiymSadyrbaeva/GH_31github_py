import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Your English skills will improve with practice."
words = word_tokenize(text)
filtered_words = [word for word in words if word.isalpha() and word.lower() not in stopwords.words("english")]

# Count word frequency
word_frequency = nltk.FreqDist(filtered_words)

# Print word frequency
print(word_frequency.most_common(5))  # Print the 5 most common words
