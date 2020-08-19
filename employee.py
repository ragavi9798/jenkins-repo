class Employee:
    def __init__(self, first, last, pay, raise_amt):
        self.first = first
        self.last = last
        self.pay = pay
        self.raise_amt = raise_amt
    @property
    def email(self):
        self.first = self.first.lower()
        self.last = self.last.lower()
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        if (self.raise_amt < 0 or self.pay < 0):
            raise ValueError('Amount must not be negative')
        self.pay = int(self.pay * self.raise_amt)
        