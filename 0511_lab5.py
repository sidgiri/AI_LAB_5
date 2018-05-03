#AI_LAB5
#Kriston Pal
#0511


from tabulate import tabulate
import operator
import re

# create a empty dictionary for word
word_count = {}
# create a empty dictionary for biagram
biagrams_count = {}
# create a empty list for words
word_list = []
# create empty list for biagrams
bigrams_list = []
# crate a list for later use
words = []


def getWordList():
    content = ""
    # open file in read mode
    f = open("shakespeare.txt", "r")
    if f.mode== 'r':
        content = f.read()
    # add words to word list
    words = re.findall(r'\b[a-z]{1,}\b', content.lower())
    stopwords = {"i",
                 "me",
                 "my",
                 "myself",
                 "we",
                 "our",
                 "ours",
                 "ourselves",
                 "you",
                 "you're",
                 "you've",
                 "you'll",
                 "you'd",
                 "your",
                 "yours",
                 "yourself",
                 "yourselves",
                 "he",
                 "him",
                 "his",
                 "himself",
                 "she",
                 "she's",
                 "her",
                 "hers",
                 "herself",
                 "it",
                 "it's",
                 "its",
                 "itself",
                 "they",
                 "them",
                 "their",
                 "theirs",
                 "themselves",
                 "what",
                 "which",
                 "who",
                 "whom",
                 "this",
                 "that",
                 "that'll",
                 "these",
                 "those",
                 "am",
                 "is",
                 "are",
                 "was",
                 "were",
                 "be",
                 "been",
                 "being",
                 "have",
                 "has",
                 "had",
                 "having",
                 "do",
                 "does",
                 "did",
                 "doing",
                 "a",
                 "an",
                 "the",
                 "and",
                 "but",
                 "if",
                 "or",
                 "because",
                 "as",
                 "until",
                 "while",
                 "of",
                 "at",
                 "by",
                 "for",
                 "with",
                 "about",
                 "against",
                 "between",
                 "into",
                 "through",
                 "during",
                 "before",
                 "after",
                 "above",
                 "below",
                 "to",
                 "from",
                 "up",
                 "down",
                 "in",
                 "out",
                 "on",
                 "off",
                 "over",
                 "under",
                 "again",
                 "further",
                 "then",
                 "once",
                 "here",
                 "there",
                 "when",
                 "where",
                 "why",
                 "how",
                 "all",
                 "any",
                 "both",
                 "each",
                 "few",
                 "more",
                 "most",
                 "other",
                 "some",
                 "such",
                 "no",
                 "nor",
                 "not",
                 "only",
                 "own",
                 "same",
                 "so",
                 "than",
                 "too",
                 "very",
                 "s",
                 "t",
                 "can",
                 "will",
                 "just",
                 "don",
                 "don't",
                 "should",
                 "should've",
                 "now",
                 "d",
                 "ll",
                 "m",
                 "o",
                 "re",
                 "ve",
                 "y",
                 "ain",
                 "aren",
                 "aren't",
                 "couldn",
                 "couldn't",
                 "didn",
                 "didn't",
                 "doesn",
                 "doesn't",
                 "hadn",
                 "hadn't",
                 "hasn",
                 "hasn't",
                 "haven",
                 "haven't",
                 "isn",
                 "isn't",
                 "ma",
                 "mightn",
                 "mightn't",
                 "mustn",
                 "mustn't",
                 "needn",
                 "needn't",
                 "shan",
                 "shan't",
                 "shouldn",
                 "shouldn't",
                 "wasn",
                 "wasn't",
                 "weren",
                 "weren't",
                 "won",
                 "won't",
                 "wouldn",
                 "wouldn't"
                 }

    word_list = [w for w in words if not w in stopwords]

    word_list = []

    for w in words:
        if w not in stopwords:
            word_list.append(w)
    create_dict(word_list)



def predict(a,b,c):
    prob = 0
    after = []
    prediction = ""

    # put all possible words after c in a list
    for i in range(len(word_list)-1):
        if word_list[i] == c:
            after.append(word_list[i+1])


    for d in after:
        if(prob < (probability(a) * condProd(a,b) * condProd(b, c) * condProd(c, d))):
            prediction = d
            prob = (probability(a) * condProd(a, b) * condProd(b, c) * condProd(c, d))
    return prediction


# create a dictionary form word list
def create_dict(word_list):
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


# creating bigrams
def getWordListBigrams():
    for i in range(len(word_list)-1):
        biagram = word_list[i] + " " + word_list[i+1]
        bigrams_list.append(biagram)


# create dictionary for biagrams
def create_dict_biagrams():
    for biagrams in bigrams_list:
        if biagrams in biagrams_count:
            biagrams_count[biagrams] += 1
        else:
            biagrams_count[biagrams] = 1


# calculate the probability for occurance of word 'a'
def probability(a):
    return word_count[a]/len(word_list)


# calculate the probability for finding word a after word b
def condProd(a, b):
    c = a + " " +  b
    return biagrams_count[c]/word_count[a]

# PART 1
getWordList()
# Question 1
top_10 = []
i = 0
# sort the dictionary and add top 10 items in a list
for key, value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):
    i += 1
    item = [i, key, value]
    top_10.append(item)
    if i == 20:
        break

print("PART A \n\nQuestion 1\nA table containing 20 most frequent words. The table contains three columns: rank, word and frequency.\n\n" + tabulate(top_10, headers=['Rank', 'Word', 'Frequency'], tablefmt='rst') + "\n")

# Quesion 2
print("\n\nQuestion 2\nA table, containing list of bottom frequencies. \n")
bottom_10 = []
i = 0
prevValue =1
wordCount = 0
examples = ""
exampleCount = 0

# function to calculate the list with bottom frequency with examples
for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
    if value != prevValue:
        # create a list to be added to the list
        element = [prevValue, wordCount, examples]
        # re initialize the variables
        prevValue = value
        wordCount=0
        exampleCount = 0
        examples = ""
        # add the element to the list
        bottom_10.append(element)
        i += 1
        continue

    # break loop of we get the 10 entries
    if i == 10:
        break

    # increase word count if the freq is same for the word in the previous iteration also ass it to example list
    if value == prevValue:
        wordCount += 1
        if exampleCount != 4:
            if exampleCount != 0:
                examples = examples + " ," + key
                exampleCount += 1
            else:
                examples = key
                exampleCount += 1


print(tabulate(bottom_10, headers=['Frequency', 'Word Count', 'Examples'], tablefmt='rst') + "\n")

print("\n\nQuestion 3\nA table containing 20 most frequent word-pairs (bigrams). The table contains three columns: rank, word pair and frequency. \n" )
# Question 3
top_20_biagrams =[]
getWordListBigrams()
create_dict_biagrams()
i=0
# sort the list 'biagrams_count' in descending order and add top 20 elements to 'top_20_biagrams'
for key, value in sorted(biagrams_count.items(), key=operator.itemgetter(1), reverse=True):
    i += 1
    item = [i, key, value]
    top_20_biagrams.append(item)
    if i == 20:
        break

print(tabulate(top_20_biagrams, headers=['Rank', 'Word Pair', 'Frequency'], tablefmt='rst') + "\n")

print("\n\nPART B:")
# Part B
# With the frequency counts of the word at our hand we calculate some basic probability estimates.

print("\nQuestion 1:\nCalculate the relative frequency (probability estimate) of the words:\n")

# 1. Calculate the relative frequency (probability estimate) of the words:
# (a) “the"

ProbThe = word_count['the']/len(word_list)
print("The relative frequency of 'the' is " + str(ProbThe))

# (b) “become"

ProbBecome = word_count['become']/len(word_count)
print("The relative frequency of 'become' is " + str(ProbBecome))

# (d) “brave"

ProbBrave = word_count['brave']/len(word_count)
print("The relative frequency of 'brave' is " + str(ProbBrave))

# (e) “treason"

ProbTreason = word_count['treason']/len(word_count)
print("The relative frequency of 'treason' is " + str(ProbTreason))


print("\n\nQuestion 2:\nCalculate the following word conditional probabilities:\n")
# 2. Calculate the following word conditional probabilities:
# (a) P(court | The)

ProbCouGivThe = biagrams_count['the count']/word_count['the']
print("P(court | The) = " + str(ProbCouGivThe))

# (b) P(word | his)

ProbWorGivHis = biagrams_count['his word']/word_count['his']
print("P(word | his) = " + str(ProbCouGivThe))

# (c) P(qualities | rare)

ProbQualGivRare = biagrams_count['rare qualities']/word_count['rare']
print("P(qualities | rare) = " + str(ProbQualGivRare))

# (d) P(men | young)

ProbMenGivYoung = biagrams_count['young men']/word_count['young']
print("P(men | young) = " + str(ProbMenGivYoung))

print("\n\nQuestion 3\nCalculate the probability:\n")
# 3. Calculate the probability:
# (a) P(have, sent)

ProbHavSent = biagrams_count['have sent']/word_count['have']
print("P(have, sent) = " + str(ProbHavSent))

# (b) P(will, look, upon)

PWillLookUpon = probability('will') * condProd('will', 'look') * condProd('look', 'upon')
print("P(will, look, upon) = " + str(PWillLookUpon))

# (c) P(I, am, no, baby)

PIAmNoBaby = probability('i') * condProd('i', 'am') * condProd('am' ,'no') * condProd('no', 'baby')
print("P(I, am, no, baby) = " + str(PIAmNoBaby))

# (d) P(wherefore, art, thou, Romeo)

PWheArtThoRom = probability('wherefore') * condProd('wherefore', 'art') * condProd('art', 'thou') * condProd('thou','romeo')
print("P(wherefore, art, thou, Romeo) = " + str(PWheArtThoRom))


print("\n\nQuestion 4\nCalculate probabilities in Q3 assuming each word is independent of other words\n")
ProbHavSentIn = probability('have') * probability('sent')
print("P(have, sent) = " + str(ProbHavSentIn))


PWillLookUponIn = probability('will') * probability('look') * probability('upon')
print("P(will, look, upon) = " + str(PWillLookUponIn))

PIAmNoBabyIn = probability('i') * probability('am') * probability('no') * probability('baby')
print("P(I, am, no, baby) = " + str(PIAmNoBabyIn))

PWheArtThoRomIn = probability('wherefore') * probability('art') * probability('thou') * probability('romeo')
print("P(wherefore, art, thou, Romeo) = " + str(PWheArtThoRomIn))

print("\n\nQuestion 5\nFind the most probable word to follow this sequence of words: \n")

print("a. I am no \nI am no " + predict("i", "am", "no"))

print("b. wherefore art thou \nwherefore art thou " + predict("wherefore","art","thou"))