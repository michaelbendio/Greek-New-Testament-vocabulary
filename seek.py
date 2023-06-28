# test tell.py
# print start of each chapter in morphgnt
# and verify in morphgnt itself
import pickle

def main():
    with open('tells', 'rb') as t:
        tells = pickle.load(t)

    with open('morphgnt') as m:
        for book in range(26):
            book = inc(book)
            m.seek(tells[book]['01'])
            print(m.readline(), end='')

# increment 'i' and return it as a 2-character string
# ensure the result is 2 characters by prepending a '0' if necessary
def inc(i):
   i += 1
   if i < 10:
      val = '0' + str(i)
   else:
      val = str(i)
   return val

if __name__ == '__main__':
    main()
