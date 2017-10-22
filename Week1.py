# French verb conjugator
import sys

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
