from nltk.tokenize import sent_tokenize, word_tokenize

#   Tokenizing: words tokenizers and sentence tokenizers
#       Lexicon and corporas
#           corporas: body of the text.
#               Ex: medical journals, presidentials speeches, English language
#           lexicon: words and their means.
#               Ex.investor-speak and regular english speak
#               investor-speak 'bull' = someone who is positive about the market.
#               english speak 'bull' = scary animal you dont want running @ you

exemple_text = "Hello Mr. Marlon, how are you doing today? The weather is great an Python is awesome. The sky is pinkish-blue. You should not eat cardboard."
# exemple_text = "Olá Dr. Marlon, como você está? O clima está muito bom e Python é fantástico. O céu está como brigadeiro. Você não deveria comer cartões."

print(sent_tokenize(exemple_text))

print(word_tokenize(exemple_text))

