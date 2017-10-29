# French verb conjugator
import sys
import pytest

def conjugate(inf):
	conj=[]
	beg=inf[0:-2]
	conj.append(('je',beg+'e'));
	conj.append(('tu',beg+'es'));
	conj.append(('il/elle/on',beg+'e'));
	return conj

def test_aimer():
    assert(conjugate("aimer")==
    	[('je','aime'), ('tu','aimes'), ('il/elle/on','aime')]);

def test2():
	assert(conjugate("conducer")==
    	[('je','conduce'), ('tu','conduces'), ('il/elle/on','conduce')]);

def test3():
	assert(conjugate("caner")==
    	[('je','cane'), ('tu','canes'), ('il/elle/on','cane')]);

if __name__ == "__main__":
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
