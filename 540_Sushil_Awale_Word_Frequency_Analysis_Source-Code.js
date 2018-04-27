const fs = require('fs');

var wordDictonary = {}; // Create an empty word dictionary
var biagramDictionary = {}; // Create an empty biagram dictionary
var wordList = []; // Create an empty word list
var biagramList = []; // Create an empty biagram list

fs.readFile('shakespeare.txt', function (err, text) { // Read from file
    if (err) return console.error(err); // Throw error if any
    var document = text.toString().toLowerCase(); // Convert read data to lower case and store in document variable
    console.log("File read!");
    createWordDictionary(document);
    createBiagram(document);
    wordList = convertToArray(wordDictonary);
    biagramList = convertToArray(biagramDictionary);
    answers();
});

function createWordDictionary(document) {
        var words = document.match(/\b(\w+)\b/g); // Split the document by checking word boundaries

        words.forEach(function (t) {
                if (t in wordDictonary) {
                    wordDictonary[t] += 1; // If word already exists in dictionary increment frequency
                } else {
                    wordDictonary[t] = 1; // Else initialise with frequency 1
                }

        });
        console.log("Word Dictionary Created!");
}

function createBiagram(document) {
        var words = document.match(/\b(\w+)\b/g); // Split the document by checking word boundaries
        for (var i = 0; i <= words.length; i++)  {
            var bigram = words[i] + " " + words[i + 1]; // Create biagram by concatenation
            if (bigram in biagramDictionary) {
                biagramDictionary[bigram] += 1; // If biagram already exists in dictionary increment frequency
            } else {
                biagramDictionary[bigram] = 1; // Else initialise with frequency 1
            }
        }
        console.log("Bigram Created!");
}

function convertToArray(obj) {
    var sortable = []; // Create an empty array
    for(var key in obj)
        if (obj.hasOwnProperty(key))
            sortable.push([key, obj[key]]); // Add key value pair to 2D array
    return sortable;
}

function top20 (wordList) {

    wordList.sort(function (a, b) {
        return b[1] - a[1]; // Sort array in descending order by second value of an element i.e. frequency
    });

    console.log("\n \n Rank \t Word \t Frequency");
    for (var i = 0; i < 20; i++) {
        console.log(i + 1 + "\t\t\t" + wordList[i][0] + "\t\t\t" + wordList[i][1]);
    }
}

function leastFrequent (wordList) {

    var leastFrequent = {}; // Create empty dictionary

    wordList.sort(function (a, b) {
        return a[1] - b[1]; // Sort array in ascending order by second value of an element i.e. frequency
    });

    var index = 0;

    for (var frequency =  1; frequency <= 10; frequency++) {
        while(wordList[index][1] === frequency) {
            if(leastFrequent[frequency]){
                leastFrequent[frequency].count += 1; // Increase word count
                leastFrequent[frequency].examples.push(wordList[index][0]); // Add word to example list
            } else {
                var examples = []; // Create an empty example list
                examples.push(wordList[index][0]);
                leastFrequent[frequency] = {count: 1, examples: examples}; // Add word to empty example list
            }
            index++;
        }
    }

    console.log("\n \n Frequency \t Word Count \t Example Words");
    for (var key in leastFrequent) {
        console.log(key + "\t\t\t" + leastFrequent[key].count + "\t\t\t\t" + leastFrequent[key].examples[Math.floor((Math.random() * 100) + 1)] + "\t" +
            leastFrequent[key].examples[Math.floor((Math.random() * 100) + 1)] + "\t" +
            leastFrequent[key].examples[Math.floor((Math.random() * 100) + 1)]);
    }
}

// Calculate the probability of the given word
function probability(word) {
    return wordDictonary[word]/wordDictonary.length;
}

// Calculate the probability of secondWord given firstWord
function conditionalProbability(firstWord, secondWord) {
    return biagramDictionary[firstWord + " " + secondWord]/wordDictonary[firstWord];
}

// Predict the next word after first, second and third word
function predict(first, second, third) {
    var prob = 0;
    var after = [];
    var prediction = "";

    // Put all words after third in a list
    for (var i = 1; i < wordList.length; i++) {
        if (wordList[i][0] === third) {
            after.push(wordList[i + 1][0]);
        }
    }

    for (var fourth in after) {
        if (prob < (probability(first) * conditionalProbability(first, second) *
            conditionalProbability(second, third) * conditionalProbability(third, fourth))) {
                prediction = fourth;
            prob = (probability(first) * conditionalProbability(first, second) *
                    conditionalProbability(second, third) * conditionalProbability(third, fourth))
        }
    }
    return prediction;
}

function answers () {

    /*
    Part A

        1. A table containing 20 most frequent words. The table contains three columns: rank, word and
            frequency.
        2. A table, containing list of bottom frequencies. The table contains three columns: frequency,
            word count and example words. You are supposed to print word counts for frequencies 10 to 1.
            The rows in this table show how many words have frequency 10,9,8...1 with example of some of
            the words.
        3. A table containing 20 most frequent word-pairs (bigrams). The table contains three columns:
            rank, word pair and frequency.
    */

    top20(wordList); // Answer 1
    top20(biagramList); // Answer 2
    leastFrequent(wordList); // Answer 3

    /*
    Part B:
        With the frequency counts of the word at our hand we calculate some basic probability estimates.
        1. Calculate the relative frequency (probability estimate) of the words:
        (a) “the" (b) “become" (d) “brave" (e) “treason"
        [Note: P(the) = count(the) / N . Here, count(the) is the frequency of “the" and “N" is the total word
        count.]
        2. Calculate the following word conditional probabilities:
        (a) P(court | The) (b) P(word | his) (c) P(qualities | rare) (d) P(men | young)
        [Read P(B | A) as “the probability with which word B follows word A". Note: P(B | A) = count(A;B)
        | count(A) ]
        3. Calculate the probability:
        (a) P(have, sent) (b) P(will, look, upon) (c) P(I, am, no, baby) (d) P(wherefore, art, thou, Romeo)
        Hint à use the chain rule (multiplication rule):
     */

    console.log("The relative frequency of 'the': " + wordDictonary["the"]/wordDictonary.length); // Answer 1.a
    console.log("The relative frequency of 'become': " + wordDictonary["become"]/wordDictonary.length); // Answer 1.b
    console.log("The relative frequency of 'brave': " + wordDictonary["brave"]/wordDictonary.length); // Answer 1.d
    console.log("The relative frequency of 'treason': " + wordDictonary["treason"]/wordDictonary.length); // Answer 1.e

    console.log("P(court | The): " + biagramDictionary["the court"]/wordDictonary["the"]); // Answer 2.a
    console.log("P(word | his): " + biagramDictionary["his word"]/wordDictonary["his"]); // Answer 2.b
    console.log("P(qualities | rare): " + biagramDictionary["rare qualities"]/wordDictonary["rare"]); // Answer 2.c
    console.log("P(men | young): " + biagramDictionary["young men"]/wordDictonary["young"]); // Answer 2.d

    console.log("P(have, sent): " + biagramDictionary["have sent"]/wordDictonary["have"]); // Answer 3.a
    console.log("P(will, look, upon): " + probability('will') * conditionalProbability('will', 'look') *
        conditionalProbability('look', 'upon')); // Answer 3.b
    console.log("P(I, am, no, baby): " + probability('i') * conditionalProbability('i', 'am') *
        conditionalProbability('am' ,'no') * conditionalProbability('no', 'baby')); // Answer 3.c
    console.log("P(wherefore, art, thou, Romeo): " + probability('wherefore') * conditionalProbability('wherefore', 'art') *
        conditionalProbability('art' ,'thou') * conditionalProbability('thou', 'romeo')); // Answer 3.d

    console.log("P(have, sent): " + probability('have') * probability('sent')); // Answer 4.a
    console.log("P(will, look, upon): " + probability('will') * probability('look') * probability('upon')); // Answer 4.b
    console.log("P(I, am, no, baby): " + probability('i') * probability('am') * probability('no') * probability('baby')); // Answer 4.c
    console.log("P(wherefore, art, thou, Romeo): " + probability('wherefore') * probability('art') * probability('thou') * probability('romeo')); // Answer 4.d

    console.log(" I am no " + predict("i", "am", "no"));
    console.log(" Wherefore art thou " + predict("wherefore", "art", "thou"));
}
