# import Python package NLTK
import nltk
# defone sentence:
# DT: determinant, VBP: Verb, JJ: Afjective
# IN: Preposition, NN: Nount
sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
   ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
# define regular expression
grammar = "NP:{<DT>?<JJ>*<NN>}"
# Parse the grammar
parser_chunking = nltk.RegexpParser(grammar)
# Parse the sentence
parser_chunking.parse(sentence)
# Parse into output
output = parser_chunking.parse(sentence)
output.draw()