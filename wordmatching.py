def word_match(words):
    count=0
    list1=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count=count+1
            list1.append(word)
    return list1,count
set_match=["aba","ccdd","1221","123","xyx"]
print(word_match(set_match))