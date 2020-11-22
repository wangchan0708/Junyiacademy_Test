def f(string):
    new_string=[]
    for i in string.split(' '):
        new_word=i[::-1]
        new_string.append(new_word)
    
    return ' '.join(new_string)
