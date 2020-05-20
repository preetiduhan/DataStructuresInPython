def anagrams(words):
    anagrams={}
    for word in words:
        sortedword=''.join(sorted(word))
        if sortedword in anagrams:
            anagrams[sortedword].append(word)
        else:
            anagrams[sortedword]=[word]
    print(list(anagrams.values()))

words=["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams(words)
        
        
