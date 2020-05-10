#------------------------------------------------------------------------------
#
#	WikiToSingle Converter
#
#	Author : Igor Janos
#
#------------------------------------------------------------------------------

import sys
import Classes.WikiNode as WN
import Classes.WikiWriter as WW


def doProcess(sourceFolder, outputFilename):

	# Load the WIKI folder structure
	root = WN.LoadNodeFromFolder(sourceFolder)
	root.PrepareIds()

	writer = WW.Writer(outputFilename)
	writer.Begin(root.maxDepth)
		
	# Export with this writer
	for n in root.children:
		writer.WriteNode(n)

	writer.Finish()
	return None


#------------------------------------------------------------------------------
#	EntryPoint: Parse commandline arguments
#------------------------------------------------------------------------------
def doMain():

	# Defaults
	sourceFolder = ''
	outputFilename = 'result.md'

	# Parsing command linov
	print('WikiToSingle.py -s <SOURCEFOLDER> -o <OUTPUTFILENAME>')

	argc = len(sys.argv)
	if (argc < 5):
		print('Error - unexpected number of arguments')
		return -1

	i=1
	while (i<argc):
		if (sys.argv[i] == '-s'):
			i += 1
			sourceFolder = sys.argv[i]
			i += 1
		elif (sys.argv[i] == '-o'):
			i += 1
			outputFilename = sys.argv[i]
			i += 1
		else:
			print('Error - unknown argument: ', sys.argv[i])

	# Try and process the Wiki
	return doProcess(sourceFolder, outputFilename)


if __name__ == "__main__":
	doMain()

