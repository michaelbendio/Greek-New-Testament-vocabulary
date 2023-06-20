#Columns
#-------
# * book/chapter/verse
# * part of speech

# * parsing code
# * text (including punctuation)
# * word (with punctuation
# * normalized word
# * lemma
 
def main():
	while True:
		section()
		
	with open('morphgnt', 'r', encoding='utf-8') as f:
		for word in f:
			if not word:
				break
			words = word.split()
			print(parsing_code(words[2]), part_of_speech(words[1]))
			print(words[5] + ' ' + words[6])	# normalized word


def section():
	books = {	# the first value of the tuple is the book code, the second is the number of chapters in the book
		'Matthew':('01', '28'), 'Mark':('02', '16'), 'Luke':('03', '24'), 'John':('04', '21'), 
		'Acts':('05', '28'), 'Romans':('06', '16'), '1 Corinthians':('07', '16'), '2 Corinthians':('08', '13'),
		'Galatians':('09', '6'), 'Ephesians':('10', '6'), 'Philippians':('11', '4'), 'Colossians':('12', '4'),
		'1 Thessalonians':('13', '5'), '2 Thessalonians':('14', '3'), '1 Timothy':('15', '6'), 
		'2 Timothy':('16', '4'), 'Titus':('17', '3'), 'Philemon':('18', '1'), 'Hebrews':('19', '13'),
		'James':('20', '5'), '1 Peter':('21', '5'), '2 Peter':('22', '3'), '1 John':('23', '5'),
		'2 John':('24', '1'), '3 John':('25', '1'), 'Jude':('26', '1'), 'Revelation':('27', '22')
	}
	print("Start")
	book = input("book ")
	code = books[book][0]
	last_chapter = books[book][1]
	chapter = input("chapter (1-" + books[book][1] + ") " )
	if len(chapter) == 1:
		chapter = '0' + chapter
	print(book + " (code: " + books[book][0] + ") chapter " + chapter)

	# scan to the book and chapter and get the number of verses
	f = open('morphgnt', 'r', encoding='utf-8')
	while True:
		line = f.readline()
		if line[0:4] == code + chapter:
			break			# at the start of the chapter

	verse = 1
	while True:
		line = f.readline()
		if line[0:4] == code + chapter:	# past the end of the chapter
			verse = line[4:6]
		else:
			break
	print("verse " + verse)
	verse	= input('verse (1 - )' + verse)
	print("line " + line)
	f.close()

#Part of Speech Code
def part_of_speech(token):
	match token:
		case 'A-':
			return 'adjective'
		case 'C-':
			return 'conjunction'
		case 'D-':
			return 'adverb'
		case 'I-':
			return 'interjection'
		case 'N-':
			return 'noun'
		case 'P':
			return 'preposition'
		case 'RA':
			return 'definite article'
		case 'RD':
			return 'demonstrative pronoun'
		case 'RI':
			return 'interrogative/indefinite pronoun'
		case 'RP':
			return 'personal pronoun'
		case 'RR':
			return 'relative pronoun'
		case 'V-':
			return 'verb'
		case 'X-':
			return 'particle'
		case '_':
			return 'part_of_speech: ' + token + ' not recognized.'

# Parsing Code
def parsing_code(s):
	match s[0]:		# person (1=1st, 2=2nd, 3=3rd)
		case '-':
			parse = ''
		case '1':
			parse = '1st person '
		case '2':
			parse = '2nd person '
		case '3':
			parse = '3rd person '
	match s[1]:		# tense (P=present, I=imperfect, F=future, A=aorist, X=perfect, Y=pluperfect)
		case 'P':
			parse += 'present '
		case 'I':
			parse += 'imperfect '
		case 'F':
			parse += 'future '
		case 'A':
			parse += 'aorist '
		case 'X':
			parse += 'perfect '
		case 'Y':
			parse += 'pluperfect '
	match s[2]:		# voice (A=active, M=middle, P=passive)
		case 'A':
			parse += 'active '
		case 'M':
			parse += 'middle '
		case 'P':
			parse += 'passive '	
	match s[3]:		# mood (I=indicative, D=imperative, S=subjunctive, O=optative, N=infinitive, P=participle)
		case 'I':
			parse += 'indicative '
		case 'D':
			parse += 'imperative '
		case 'S':
			parse += 'subjunctive '
		case 'O':
			parse += 'optative '
		case 'N':
			parse += 'infinitive '
		case 'P':
			parse += 'participle '		
	match s[4]:		# case (N=nominative, G=genitive, D=dative, A=accusative)
		case 'N':
			parse += 'nominative '
		case 'G':
			parse += 'genitive '
		case 'D':
			parse += 'dative '
		case 'A':
			parse += 'accusative '
	match s[5]:		# number (S=singular, P=plural)
		case 'S':
			parse += 'singular'
		case 'P':
			parse += 'plural'		
	match s[6]:		# gender (M=masculine, F=feminine, N=neuter)
		case 'M':
			parse += 'masculine '
		case 'F':
			parse += 'feminine '
		case 'N':
			parse += 'neuter '
	match s[7]:		# degree (C=comparative, S=superlative)
		case 'C':
			parse += 'comparative '
		case 'S':
			parse += 'superlative'
	return parse

if __name__ == '__main__':
	main()
