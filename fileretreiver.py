import sys,getopt

from filedecoder import FileDecoder

def helper():
	print " Usage: python retreiver.py -i <inputfile> -o <outputfile>"


if __name__=="__main__":
	inputfile = ""
	outputfile = ""
	try:
		optlist, args = getopt.getopt(sys.argv[1:], "hi:o:",["help","inputfile=","outputfile="])
	except getopt.GetoptError as ge:
		helper()
	for o,a in optlist:
		if o  in ("-h","help"):
			helper()
		elif o in ("-i","--inputfile"):
			inputfile = a
		elif o in ("-o","--outputfile"): 
			outputfile = a
	fildecoder = FileDecoder(inputfile, outputfile)
	fildecoder.rundecoder()