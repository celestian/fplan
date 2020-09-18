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
