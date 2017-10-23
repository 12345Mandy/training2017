# French verb conjugator
import sys

def ends_in_er(word):
        """
        Return True if the string word ends in 'er', otherwise return False.
        This does not work if there is whitespace at the end of the string.
        Maybe we could consider taking care of that in this function just to
        be robust.
        """
        return (word[-2:] == 'er')

def test_functions():
        if not ends_in_er('beer'):
                print("FAIL")
        if ends_in_er('carrot'):
                print("FAIL")
        #  Following test could catch something that we change
        if ends_in_er('amanecer\n'):
                print("FAIL.  Currently not stripping whitespace")


# run the self-test for our functions
test_functions()

# prompt user
print ("Enter verb in infinitive form")


# Read the response
for verb in sys.stdin:
	# be clever and work around the newline
	ending=verb[-3:-1]
	print (ending)
	if ending=='er':
		beg=verb[0:-3]
		print ("j\' " + beg + "e")
		print ("tu " + beg + "es")
		print ("il/elle/on " + beg + "e")
		print ("nous " + beg + "ons")
		print ("vous " + beg + "ez")
		print ("ils/elles " + beg + "ent")
	# prompt user
	print ("Enter verb in infinitive form")


