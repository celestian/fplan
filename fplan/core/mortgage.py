class Mortgage:

    def __init__(self, loan_amount, interest_rate, loan_length):
        '''
        loan_amount     initial loan amount
        interest_rate   annual interest rate (decimal number)
        loan_length     loan legth in years
        '''

        self._loan_amount = loan_amount
        self._interest_rate = interest_rate
        self._loan_length = loan_length

    def anuita(self):

        i_pm = self._interest_rate/12.0
        q = pow(1.0 + i_pm, 12.0 * self._loan_length)
        a = self._loan_amount * i_pm * q / (q - 1.0)

        return a

    def umor(self, k):

        i_pm = self._interest_rate/12.0
        umor = self.anuita() / pow(1.0 + i_pm, 12.0 * self._loan_length - k)

        return umor

    def urok(self, k):

        i_pm = self._interest_rate/12.0
        urok = self.anuita() * (1.0 - (1.0 / pow(1.0 + i_pm, 12.0 * self._loan_length - k)))

        return urok

    def zustatek(self, k):

        umor = 0
        for i in range(0, k):
            umor = umor + self.umor(i)

        return self._loan_amount - umor

    def calendar(self):

        for i in range(0, 12 * self._loan_length + 1):

            print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(i, self.anuita(), self.urok(i), self.umor(i), self.zustatek(i)))
