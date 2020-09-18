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

        q = 1.0 + self._interest_rate
        qn = pow(q, self._loan_length)
        a = self._loan_amount * qn * (q - 1.0) / float((qn - 1.0))

        return a / 12.0
