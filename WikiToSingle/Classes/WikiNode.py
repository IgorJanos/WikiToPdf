#------------------------------------------------------------------------------
#
#	WikiToSingle Converter
#
#	Author : Igor Janos
#
#------------------------------------------------------------------------------
import os
import re
import urllib

def escapeNodeName(title):	
	title = urllib.parse.unquote(title)
	return title.replace("-", " ")

def escapeNodeFileName(fn):	
	return escapeNodeName(os.path.splitext(fn)[0])

def indent(d):
	result = ""
	for i in range(d): 
		result = result + "  "
	return result

#------------------------------------------------------------------------------
#
#	Node class
#
#------------------------------------------------------------------------------

class Node:

	def __init__(self, title):
		self.title = escapeNodeName(title)
		self.filename = ""
		self.id = ""
		self.children = []
		self.depth = 0
		self.maxDepth = 0

	def PrepareIds(self, id = ""):
		self.id = id
		i=1
		newId = ""
		for n in self.children:
			# Prepare the node ID
			if (id == ""): newId = "{0}".format(i)
			else: newId = "{0}.{1}".format(id, i)
			n.PrepareIds(newId)
			i += 1
		return None

	def Echo(self, id = ""):
		print("{0}{1} {2}".format(indent(self.depth), id, self.title))

		i=1
		newId = ""
		for n in self.children:
			# Zlozime nove IDcko - cislovanie
			if (id == ""): newId = "{0}".format(i)
			else: newId = "{0}.{1}".format(id, i)
			n.Echo(newId)
			i += 1

		return None	


#------------------------------------------------------------------------------
#	Public functions
#------------------------------------------------------------------------------

def LoadChildrenNodesFromFolder(folder, parentNode):

	# List of found MD files
	files = []

	# Decide on file ordering if there is the '.order' file present
	fileOrder = os.path.join(folder, ".order")
	if (os.path.isfile(fileOrder)):
		with open(fileOrder) as f:
			content = f.readlines()
			content = [x.strip() for x in content] 
			for c in content: 
				cf = c + ".md"
				if (os.path.isfile(os.path.join(folder, cf))): 
					files.append(cf)

	else:
		for f in os.listdir(folder):
			if (os.path.isdir(os.path.join(folder, f)) == False):
				if ('.md' in f): files.append(f)

	# Walk through the found MD files
	for f in files:
		fileName = os.path.splitext(f)[0]

		# Append a new node
		subNode = Node(fileName)
		subNode.filename = os.path.join(folder, f)
		subNode.depth = parentNode.depth + 1
		parentNode.children.append(subNode)

		# Only process if there is such a folder
		subFolder = os.path.join(folder, fileName)
		if (os.path.isdir(subFolder)):
			LoadChildrenNodesFromFolder(subFolder, subNode)

		if (subNode.depth > parentNode.maxDepth):
			parentNode.maxDepth = subNode.depth

	return parentNode


def LoadNodeFromFolder(folder):

	# Result node
	root = Node("Root")
	return LoadChildrenNodesFromFolder(folder, root)