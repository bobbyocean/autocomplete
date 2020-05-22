from collections      import Counter
from itertools        import chain
from sortedcontainers import SortedDict

class AutoComplete:

    def __init__(self,text=None):
        '''
        This is a basic autocomplete algorithm that simply gets a count of the words that
        are trained on. The words are stored in a SortedDict for efficiency.

        Examples:

        x = AutoComplete()
        x.train('some text to train on')
        print(x)
        x.autocomplete('tex')
        x.train('some other text that is really interesting to the user')
        x.autocomplete('so')
        x.autocomplete_dict('so')

        y = AutoComplete('Different text that is used over here.')
        y += x
        print(y)
        y.autocomplete('us')

        z = x + y
        print(z)
        z.autocomplete('t')
        z.autocomplete('t',True)
        z.autocomplete_dict('T')
        z.autocomplete_dict('t').most_common(2)
        print(', '.join(f'"{a}" ({b})' for a,b in z.autocomplete_dict('t').most_common(3)))
        '''
        self.words = SortedDict()
        self.train(text)

    def __repr__(self):
        return (f'AutoComplete instance is currently trained on {len(self.words)} '
                f'unique words ({sum(self.words.values())} total).')

    def __add__(self,other):
        if isinstance(other,AutoComplete):
            new = AutoComplete()
            for word in chain(self.words, other.words):
                if word not in new.words:
                    new.words[word] = self.words.get(word, 0) + other.words.get(word, 0)
            return new
        else:
            raise TypeError(f'AutoComplete can only add with another AutoComplete instance.')

    def __iadd__(self,other):
        if isinstance(other,AutoComplete):
            for word in other.words:
                self.words[word] = self.words.get(word, 0) + other.words.get(word, 0)
            return self
        else:
            raise TypeError(f'AutoComplete can only add with another AutoComplete instance.')

    def _filter_word(self,word):
        '''Specify how to filter a word so that it '''
        word = word.lower()
        # Strip all printable ascii that is not alpha numeric.
        word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c')
        return word

    def _get_words(self,text):
        '''This function specifies how to split up the text into the words to train on.
        Normally, one would simply .split() over the text. Returns a generator for
        efficiency.'''
        return map(self._filter_word,text.split())

    def train(self,text):
        '''Given a string of text, train on the words in the text; that is, update self.words.'''
        words = self._get_words(text) if text else []
        for word in words:
            self.words[word] = self.words.get(word,0) + 1

    def autocomplete_dict(self,start_string):
        '''Find the section of words in self.words that starts with start_string. Return a Counter().'''
        sub_string = start_string.lower()
        if not self.words:
            return Counter()
        answer = dict()
        start  = self.words.bisect_left(sub_string)
        w,c    = self.words.peekitem(start)
        while w.startswith(sub_string) and w!=sub_string:
            answer[start_string+w[len(start_string):]] = c
            start += 1
            if len(self.words)<=start:
                break
            w,c = self.words.peekitem(start)
        return Counter(answer)

    def autocomplete(self,sub_string,confidence=False):
        '''Shortcut function to return the most common word from self.autocomplete_dict().'''
        answer = self.autocomplete_dict(sub_string)
        if not answer:
            return 'Not enough data for any suggestions.'
        answer = answer.most_common(1)[0]
        return f'{answer[0]} ({answer[1]})' if confidence else answer[0]




