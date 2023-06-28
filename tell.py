# record the tell for the start of each chapter store it in 'tells' and
# finally write tells to a file
import pickle

def main():
   book_tells = {}
   chapter_tells = {}
   with open('morphgnt', 'r', encoding='utf-8') as f:
      book = '01'
      chapter = '01'
      chapter_tells[chapter] = f.tell()
      while True:
         previous_tell = f.tell()
         line = f.readline()
         if (line[0:2]) != book:
            chapter_tells[chapter] = previous_tell
            book_tells[book] = chapter_tells
            if book == '27':
                break
            book = inc(book)
#            print('book', book)
            chapter_tells = {}
            chapter = '00'
         if line[2:4] != chapter:	# the tell here is the end of the first line in the next chapter
            chapter = inc(chapter)
#            print('chapter',chapter)
            chapter_tells[chapter] = previous_tell
            while True:
               line = f.readline()
               if line[0:4] == book + chapter:
                  break
            p = open('tells', 'wb')
            pickle.dump(book_tells, p)
            p.close()

# increment the string 's' as if it were an integer
# ensure the result is 2 characters by prepending a '0' if necessary
def inc(s):
   i = int(s)
   i += 1
   if i < 10:
      val = '0' + str(i)
   else:
      val = str(i)
   return val

if __name__ == '__main__':
	main()
