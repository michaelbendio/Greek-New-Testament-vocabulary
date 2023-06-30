Greek-New-Testament-vocabulary  
Use morphgnt and the Abbott-Smith GNT dictionary to create a list of vocabulary words  
for a chapter in the Greek New Testament.  
morphgnt is a verse-by-verse, word-by-word morphological analysis of the New Testament   

See https://github.com/translatable-exegetical-tools/Abbott-Smith and  
https://github.com/fhardison/abbot-smith-gloss-list/blob/master/gloss-dict.tab  

Morphgnt Rows: one row per word (for each verse, as many rows as there are words).  
 * book/chapter/verse in the form of 2-character groups: bbccvv
 * part of speech
 * parsing code
 * text (including punctuation)
 * word (with punctuation
 * normalized word
 * lemma

 What remains to be done:  
 Write a module that queries the user for NT book and chapter to create a vocabulary list for.  
		This decouples the front end from the working part and makes a GUI an option.  
 Replace Abbott-Smith.py (slow, ugly parse of every entry until finding the desired lemma)  
 with Abbott-Smith glosses.py which is a python dictionary.  
  
 Next:  
 Currently I scan morphgnt (5900+ lines) from the beginning to find the requested chapter.  
 I've created a file of tells for the beginning of each chapter. See the seek.py module  
 to see how to use it. Replace the code here that does the scanning with seeking the tell.  
 First just print the morphgnt line for the requested chapter and verify it's correct.  
 Then look up the gloss and add it to a vocabulary file. Maintain a 'seen' file so  
 words that have been saved to a previous vocabulary file aren't added to a new one.  
 The vocabulary file is created in the form 'lemma [\t] gloss [space] part of speech [space] parse code'  
 so that it can be imported into Flash Cards Deluxe.  
