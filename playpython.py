def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0
    result = 0
    length = len(array)
    i =0
    while i < length:
        if length != 0:
            sum = sum + array[i]
            print sum
            i+= 2
            result = sum * array[length-1]
        elif i == 0:
            result = 0
    print "result = " + str(result)
    return result 
        
        
    
    
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
