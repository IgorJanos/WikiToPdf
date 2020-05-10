#------------------------------------------------------------------------------
#
#	WikiToSingle Converter
#
#	Author : Igor Janos
#
#------------------------------------------------------------------------------
import os


def headingIndent(n):
	result = ""
	for i in range(n): result = result + "#"
	return result

def offsetHeading(x, n):
	if (x.startswith("#")):
		x = x.replace("#", headingIndent(n+1), 1)
	return x


#------------------------------------------------------------------------------
#
#	Writer class
#
#------------------------------------------------------------------------------

class Writer:

	def __init__(self, filename):
		self.filename = filename
		self.isOpen = False
		self.file = None
		self.maxDepth = 0

	def Begin(self, maxDepth):
		self.file = open(self.filename, "w")
		self.maxDepth = maxDepth
		return None

	def Finish(self):
		self.file.close()
		self.file = None
		return None

	def WriteNode(self, node):
		if (self.file == None): return None

		depthOffset = node.depth
		heading = headingIndent(node.depth)

		print("Processing: ({0}) - {1}".format(node.depth, node.filename))

		# Write the node ID first
		self.file.write("{0} {1} {2} \n".format(heading, node.id, node.title))
		self.file.write(" \n")

		# Write the given node file and offset the headings
		with open(node.filename, 'r', encoding='utf-8', errors='ignore') as filePage:
			content = filePage.readlines()
			content = [offsetHeading(x, depthOffset) for x in content]
			self.file.writelines(content)
			self.file.write(" \n\n")

		# Write the child nodes
		for nChild in node.children:
			self.WriteNode(nChild)

		return None
