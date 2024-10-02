import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv('dataset.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text_data'], df['label'], test_size=0.2, random_state=42)

# Preprocess the text data
# You may want to remove stop words, stem or lemmatize words, and convert text to numerical features such as TF-IDF

# Train the Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Test the accuracy of the classifier
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# Evaluate the performance of the classifier
y_pred = clf.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)
