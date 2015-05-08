
OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
	return operation(x,y)
def conv(x):
	if x == 1:
		x = True
	else:
		x = False
def conjunction(x,y):
	if x == y and x == 0:
		#print "T"
		return 1
	elif x == y and x == 1:
		#print "F x and y are 1"
		return 0
	else:
		#print "F"
		return 0
def disjunction(x,y):
	if x == y and x == 0:
		#print "F x and y are 0"
		return 0
	else:
		#print "ture!"
		return 1
def implication(x,y):
	if x == 1:
		x = 0
	else:
		x = 1
	return disjunction(x,y)
def exclusive(x,y):
	if disjunction(x,y) == 1:
		if conjunction(x,y) == 1:
			return 0
		else:
			return 1
	else:
		return 0




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, conjunction) == 0, "and"
    assert boolean(1, 0, disjunction) == 1, "or"
    assert boolean(1, 1, implication) == 1, "material"
    assert boolean(0, 1, exclusive) == 1, "xor"
    #assert boolean(0, 1, equivalence) == 0, "same?"
    #conjunction(1,0)
    #conjunction(0,0)
    #conjunction(0,1)
    #conjunction(1,1)
    #disjunction(1,0)
    #disjunction(0,0)
    #disjunction(0,1)
    #disjunction(1,1)
