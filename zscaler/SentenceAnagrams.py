def countSentences(words, sentences):
    anagramsDict = {}
    anagramswords = []
    anagramsDictCnt = []
    for word in words:
        for word2 in words:
            if word != word2 and sorted(word) == sorted(word2):
                    anagramsDict[word] = word2
                    anagramswords.append(word)

    anagramcntArray = []

    for sentence in sentences:
        words = sentence.split(" ")
        print(words)
        anagramCnt = 0
        for word in words:
            if word in anagramswords:
                anagramCnt += 1
        anagramcntArray.append(anagramCnt)

    # print(anagramcntArray)

if __name__ == '__main__':

    sentenceArray = ["cat the bats", "in the act", "act tabs in"]

    wordset = ["the", "bats", "tabs", "in", "cat", "act"]

    countSentences(wordset, sentenceArray)