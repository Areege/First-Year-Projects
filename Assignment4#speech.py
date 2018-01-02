name=input(str("Please enter the name of the speaker:"))
spin=input(str("Please enter the spin words:"))
speech=input(str("Please enter the speech:"))
    
sentenceCount = 0
wordCount = 0
characterCount = 0

spinList = spin.split(' ')
characterList = list(speech)
wordList = speech.split(' ')
    
for index in range(0,len(wordList)):
    if ('.' in wordList[index]):
        wordList[index] = wordList[index][:-1]
    if ('?' in wordList[index]):
        wordList[index] = wordList[index][:-1]
    if (',' in wordList[index]):
        wordList[index] = wordList[index][:-1]
    if ('-' in wordList[index]):
        wordList[index] = wordList[index-1][:-3]
    if (';' in wordList[index]):
        wordList[index] = wordList[index][:-1]
    if ('"' in wordList[index]):
        wordList[index] = wordList[index][:-1]

for index in range(0, len(characterList)):
    if (characterList[index] == '.'):
        if (characterList[index] != characterList[index-1] or characterList[index+1]):
            sentenceCount += 1
    if (characterList[index] != ' ' or '.'):
        characterCount += 1
            
wordCount = len(wordList)
    
uniqueWords = -1*(wordCount)

for index in range(0, len(wordList)):
    for index1 in range(0, len(wordList)):
        if (wordList[index] == wordList[index1]):
            uniqueWords += 1

if (uniqueWords < 0):
    uniqueWords = 0
if (uniqueWords > 0):
    uniqueWords = wordCount-uniqueWords

percentageOfUnique = int((uniqueWords/wordCount)*100)

found = 0
while (found == 0):
    for index in range(0,len(wordList)):
        counter = 0
        for index1 in range(0,len(wordList)):
            if len(wordList[index]) > len(wordList[index1]):
                counter += 1
                if (counter == len(wordList)-1):
                    longestWord = wordList[index]
                    found = 1

occurrences = 0
for index in range(0,len(spinList)):
    for index1 in range(0, wordCount):
        if (spinList[index] == wordList[index1]):
            occurrences += 1
                
percentageOfOccurrences = int((occurrences/wordCount)*100)

print(sentenceCount,'sentences')
print(wordCount,'words')
print(characterCount,'characters')
print(uniqueWords,'unique words amounting to',percentageOfUnique,'percent.')
print(longestWord,'is the longest word.')
print('The speech contained',occurrences,'spin words, amounting to a ratio of',percentageOfOccurrences,'percent.')
    
    
    
