# Parse an Abbott-Smith XML-tagged dictionary
# https://github.com/translatable-exegetical-tools/Abbott-Smith, specifically abbott-smith.tei.xml
# First delete everything before the first <entry> and after the last one

# find a line that starts with <entry... >
# this will contain the lemma
# strip off everything except the lemma
def entry(f):
	while True:
		line = f.readline()
		if not line:
			break
		if line.find('<entry n=') >= 0:
#			if line.find('G2033') >= 0:
#				breakpoint()
			start = line.find('"')+1
			end = line.find('|')		# e.g., <entry n="ἀγαπάω|G25">
			if end < 0:
				end = line.find('">')	# e.g., <entry n="Ἀβειληνή">
			return line[start:end]
			break

# find the first gloss in the entry
# note that this does not parse out the complete lexical entry--just the first gloss
# this could be improved
def gloss(f):
	while True:
		line = f.readline()
		if line.find('</entry>') >= 0:
			return ''
		gloss = line.find('<gloss>')
		if gloss >= 0:
			line = line[gloss+7:]	# i.e., starting after <gloss>
			end = line.find('</gloss>')
			return strip_foreign_tag(line[:end])
	for line in f:
		if line.find('</entry>') >= 0:
			return ''

# sometimes there will be a <foreign...> greek word </foreign>
# the greek word is the gloss, e.g. δαιμον
def strip_foreign_tag(line):
	tag = line.find('<foreign')
	if tag >= 0:
		angle = line.find('>')								# if there's an < there will be a >'
		end_tag = line.find('</foreign')			# if there's a <foreign, there will be a </foreign'
		line = line[0:tag]+line[angle+1:end_tag]
	return line

def lookup(word):
	with open('Abbott-Smith raw entries.txt', 'r', encoding='utf-8') as f:
		while True:
			e = entry(f)
			if not e:
				break
			if word == e:
				return gloss(f)
