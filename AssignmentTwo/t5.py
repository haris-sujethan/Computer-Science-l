file = open('Answers.txt', 'r', encoding='utf-8-sig')
pair_arr = []
with open('Answers.txt', 'r', encoding='utf-8-sig') as x:
# removes the space character
    Answers = [line.rstrip('\n') for line in x]
print(Answers)

import unittest

class Testing(unittest.TestCase):

   def test_func_1(self):
     
     assert Answers[0]=="Lady Catelyn Stark"
   def test_func_2(self):
      
        assert Answers[1]=="House Lannister"

if __name__ == "__main__":
    unittest.main()