def average_finder(l1,l2): #*args bhi use kar sakte hai
    average=[]
    for pair in zip(l1,l2): #*args bhi use kar sakte hai
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3],[4,5,6]))