import operator
import re
import string

# dictionary to store word and respective frequency
wordFrequency = {}
# dictionary to store word pair and respective frequency
wordPairFrequency = {}
document_text = open('D:\Sem V\DWIT Lab Work\AI\lab5\\shakespeare.txt', 'r')
# store the text of the opened document
text_string = document_text.read().lower()
# store each word of a string text_string in list
wordList = re.findall(r'\b[a-z]{1,}\b', text_string)

# count frequency of each word in list wordList and store in dictionary wordFrequency
for word in wordList:
    count = wordFrequency.get(word, 0)
    wordFrequency[word] = count + 1
# sort the dictionary in descending order
sorted_wordFrequencyList = sorted(wordFrequency.items(), key=lambda x: x[1], reverse=True)

# list to store all word pairs
wordPairList = []
# make and store all word pairs in wordPairList
for index in range(len(wordList) - 1):
    wordPair = wordList[index] + ":" + wordList[index + 1]
    wordPairList.append(wordPair)
# count frequency of each word pair in list wordPairList and store in dictionary wordPairFrequency
for wordPair in wordPairList:
    count = wordPairFrequency.get(wordPair, 0)
    wordPairFrequency[wordPair] = count + 1
# sort the dictionary in descending order
sorted_wordPairFrequencyList = sorted(wordPairFrequency.items(), key=lambda x: x[1], reverse=True)

# total number of words in wordList (in given document)
totalWords = len(wordList)


# function to calculate probability of a word
def wordProbability(a):
    a = a.lower()
    return wordFrequency[a] / totalWords


# function to calculate conditional probability of B given A
def conditionalProbabilityTwoWords(b, a):
    word_pair = a + ":" + b
    word_pair = word_pair.lower()
    return wordPairFrequency[word_pair] / wordFrequency[a]


# function to calculate probability of occurring B after A
def probabilityTwoWords(a, b):
    return wordProbability(a) * conditionalProbabilityTwoWords(b, a)


# function to calculate probability of occurring C after A B
def probabilityThreeWords(a, b, c):
    return wordProbability(a) * conditionalProbabilityTwoWords(b, a) * conditionalProbabilityTwoWords(c, b)


# function to calculate probability of occurring D after A B C
def probabilityFourWords(a, b, c, d):
    probability = wordProbability(a) * conditionalProbabilityTwoWords(b, a)
    probability *= conditionalProbabilityTwoWords(c, b) * conditionalProbabilityTwoWords(d, c)
    return probability


# function to calculate probability of occurring B after A assuming A and B are independent
def probabilityTwoWordsIndependent(a, b):
    return wordProbability(a) * wordProbability(b)


# function to calculate probability of occurring C after A B assuming A, B, C are independent
def probabilityThreeWordsIndependent(a, b, c):
    return wordProbability(a) * wordProbability(b) * wordProbability(c)


# function to calculate probability of occurring D after A B C assuming A, B, C, D are independent
def probabilityFourWordsIndependent(a, b, c, d):
    return wordProbability(a) * wordProbability(b) * wordProbability(c) * wordProbability(d)


# function to calculate the list of words that come after some word
def listAfter(something):
    something_list = []
    for i in range(len(wordList) - 1):
        if wordList[i] == something:
            something_list.append(wordList[i + 1])
    return something_list


# function to find word with maximum probability to come after A B C among the words that come after C
def mostProbableWordAfter(a, b, c, something_list):
    probability = 0
    word_to_return = ""
    for d in something_list:
        if probability < probabilityFourWords(a, b, c, d):
            probability = probabilityFourWords(a, b, c, d)
            word_to_return = d
    return word_to_return


print("-----------PART A--------------\n")
print("\n*********Solution of Part A Q.No.1*********\n20 Most Frequent Words are\n")
print("Rank\tWord\tFrequencies\n")
for i in range(20):
    print(i + 1, "\t\t", sorted_wordFrequencyList[i][0], "\t", sorted_wordFrequencyList[i][1])

print("\n\n*********Solution of Part A Q.No.2*********\nList of Bottom Frequencies\n")
print("Frequency\tWord Count\tExample Words\n")
for i in range(10):
    word_list = []
    for text_num in sorted_wordFrequencyList:
        if text_num[1] == i + 1:
            word_list.append(text_num[0])
    if len(word_list) > 0:
        new_list = [len(word_list), i + 1, word_list]
    else:
        new_list = [len(word_list), i + 1, ""]
    print(new_list[0], "\t\t", new_list[1], "\t\t", new_list[2])

print("\n\n*********Solution of Part A Q.No.3*********\n20 Most Frequent Word pairs are\n")
print("Rank\tWord Pair\tFrequencies\n")
for i in range(20):
    print(i + 1, "\t\t", sorted_wordPairFrequencyList[i][0], "\t", sorted_wordPairFrequencyList[i][1])

print("\n\n\n-----------PART B------------\n")
print("*********Solution of Part B Q.No.1*********\nRelative Frequencies (Probability Estimate) of Given Words\n")
print("Probability of the, P(the) = ", wordProbability('the'))
print("Probability of become, P(become) = ", wordProbability('become'))
print("Probability of brave, P(brave) = ", wordProbability('brave'))
print("Probability of treason, P(treason) = ", wordProbability('treason'))

print("\n\n*********Solution of Part B Q.No.2*********\nWord Conditional Probabilities:\n")
print("Conditional Probability of P(court|the) = ", conditionalProbabilityTwoWords('court', 'the'))
print("Conditional Probability of P(word|his) = ", conditionalProbabilityTwoWords('word', 'his'))
print("Conditional Probability of P(qualities|rare) = ", conditionalProbabilityTwoWords('qualities', 'rare'))
print("Conditional Probability of P(men|young) = ", conditionalProbabilityTwoWords('men', 'young'))

print("\n\n*********Solution of Part B Q.No.3*********\nProbability of multiple words:\n")
print("Probability of P(have,sent) = ", probabilityTwoWords('have', 'sent'))
print("Probability of P(will,look,upon) = ", probabilityThreeWords('will', 'look', 'upon'))
print("Probability of P(I,am,no,baby) = ", probabilityFourWords('i', 'am', 'no', 'baby'))
print("Probability of P(wherefore,art,thou,Romeo) = ", probabilityFourWords('wherefore', 'art', 'thou', 'romeo'))

print("\n\n*********Solution of Part B Q.No.4*********\nProbability of multiple words assuming independent:\n")
print("Probability of P(have,sent) = ", probabilityTwoWordsIndependent('have', 'sent'))
print("Probability of P(will,look,upon) = ", probabilityThreeWordsIndependent('will', 'look', 'upon'))
print("Probability of P(I,am,no,baby) = ", probabilityFourWordsIndependent('i', 'am', 'no', 'baby'))
print("Probability of P(wherefore,art,thou,Romeo) = ",
      probabilityFourWordsIndependent('wherefore', 'art', 'thou', 'romeo'))

print("\n\n************Solution of Part B Q.No.5**********\nMost probable words to follow : ")
print("The most probable word to follow, I am no,  is " + mostProbableWordAfter('i', 'am', 'no', listAfter('no')))
print("The most probable word to follow, wherefore art thou, is " + mostProbableWordAfter('wherefore', 'art', 'thou',
                                                                                          listAfter('thou')))
