"""
In this part of the tutorial, I want us to take a moment to peak into the corpora we all downloaded! The NLTK corpus is a massive dump of all kinds of natural language data sets that are definitely worth taking a look at.

Almost all of the files in the NLTK corpus follow the same rules for accessing them by using the NLTK module, but nothing is magical about them. These files are plain text files for the most part, some are XML and some are other formats, but they are all accessible by you manually, or via the module and Python. Let's talk about viewing them manually.

Depending on your installation, your nltk_data directory might be hiding in a multitude of locations. To figure out where it is, head to your Python directory, where the NLTK module is. If you do not know where that is, use the following code:

"""

import nltk
print(nltk.__file__)

"""
if sys.platform.startswith('win'):
    # Common locations on Windows:
    path += [
        str(r'C:\nltk_data'), str(r'D:\nltk_data'), str(r'E:\nltk_data'),
        os.path.join(sys.prefix, str('nltk_data')),
        os.path.join(sys.prefix, str('lib'), str('nltk_data')),
        os.path.join(os.environ.get(str('APPDATA'), str('C:\\')), str('nltk_data'))
    ]
else:
    # Common locations on UNIX & OS X:
    path += [
        str('/usr/share/nltk_data'),
        str('/usr/local/share/nltk_data'),
        str('/usr/lib/nltk_data'),
        str('/usr/local/lib/nltk_data')
    ]
"""

from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])
