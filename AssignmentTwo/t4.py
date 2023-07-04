file = open('Questions.txt', 'r', encoding='utf-8-sig')
pair_arr = []
with open('Questions.txt', 'r', encoding='utf-8-sig') as x:
# removes the space character
    Questions = [line.rstrip('\n') for line in x]
print(Questions)

import unittest

class Testing(unittest.TestCase):

   def test_func_1(self):
     
     assert Questions[0]=="Who is Arya Stark's wife?"
   def test_func_2(self):
      
        assert Questions[1]=="Who escaped the persecution of House Stark?"

if __name__ == "__main__":
    unittest.main()