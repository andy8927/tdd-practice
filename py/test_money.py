import unittest

class Dollar: 
    def __init__(self, amount):
        self.amount = amount
        
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
        
    def times(self, multiplier): 
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor): 
        return Money(self.amount / divisor, self.currency)
    
class TestMoney(unittest.TestCase): 
    
    def testMultiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10,tenner.amount)
        
    def testMultiplicationInEuros(self): 
        tenEuros = Money(10, "EUR") 
        twentyEuros = tenEuros.times(2) 
        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", twentyEuros.currency)
        
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))
        
    def testDivision(self): 
        originalMoney = Money(4002, "KRW") 
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        
        self.assertEqual(expectedMoneyAfterDivision.amount, actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency, actualMoneyAfterDivision.currency)




if __name__ == '__main__': 
    unittest.main()