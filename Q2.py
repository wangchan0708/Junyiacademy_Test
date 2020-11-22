def number_count(input):
    list=[]
    for i in range(1,input+1):
        if i%15==0:
            list.append(i)
        elif (i%3==0) or (i%5==0):
           continue
        else:
            list.append(i)
    return len(list)
            
