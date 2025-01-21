class Letter:
    """A letter receives an all-caps reply when sent successfully.
    >>> hi = Letter('Hello, World!')
    >>> hi.send()
    Hello, World! has been sent.
    HELLO, WORLD!
    >>> hi.send()
    Hello, World! was already sent.
    >>> Letter('Hey').send().send()
    Hey has been sent.
    HEY has been sent.
    HEY
    """

    def __init__(self, contents):
        self.contents = contents
        self.sent = False

    def send(self):
        if self.sent:
            print(self, "was already sent.")
        else:
            print(self, "has been sent.")
            self.sent = True
            return Letter(self.contents.upper())

    def __repr__(self):
        # Note: since no __str__ method is defined, the repr and str strings are the same.
        return self.contents


class Numbered(Letter):
    """A numbered letter has a different repr method that shows its number.
    >>> hey = Numbered('Hello, World!')
    >>> hey.send()
    #0 has been sent.
    HELLO, WORLD!
    >>> Numbered('Hi!').send()
    #1 has been sent.
    HI!
    >>> hey
    #0
    """

    number = 0

    def __init__(self, contents):
        super().__init__(contents)
        self.number = Numbered.number
        Numbered.number += 1

    def __repr__(self):
        return "#" + str(self.number)
