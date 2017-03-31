import numpy as np

sentences = [
    ['are you full'],
    ['believe', 'me'],
    ['bye', 'bye', 'mom'],
	['can', 'i', 'go', 'to', 'restroom'],
	['can', 'i', 'help', 'you'],
	['can', 'you', 'speak', 'slowly'],
	['check', 'it', 'out'],
	['clap', 'your', 'hands'],
	['close', 'the', 'door'],
	['close', 'your', 'eyes'],
	['comb', 'your', 'hair'],
	['come', 'down'],
	['come', 'here'],
    ['come' 'on'],
	['come', 'in', 'please'],
]

classVector = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
temp = set()

[temp.add(word) for sentence in sentences for word in sentence]
words = list(temp)

classLabels = set(classVector)
probs = {}

for classLabel in classLabels:
    probs[classLabel] = float(classVector.count(classLabel)) / float(len(classVector))

z = np.zeros([1, 10])
prob_class = np.zeros([len(classVector), len(words)]);
prob_word = np.zeros([1, len(words)])

for i in range(len(sentences)):
    for word in sentences[i]:       
        prob_class[i, words.index(word)] += 1

print(prob_class)
