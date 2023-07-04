from t1 import pair_creator 

filename='Overlapping.txt'
def dict_creator(filename: str):

    list_contents=pair_creator(filename)
        
    d={}
    
    for x in list_contents:
        d[x[0]] = x[1]
        
    return d

with open('QA_dictionary.txt', 'w') as f:
    dict = dict_creator(filename)
    for key in dict:
        newlnStr = str(key) + ',' + str(dict[key])
        f.write(newlnStr)
        f.write('\n')

import unittest

class Testing(unittest.TestCase):

   def test_func_1(self):
     dict = dict_creator(filename)
     assert dict["question Who murdered Rhaegar's wife?"] == 'answer House Lannister'
   def test_func_2(self):
      dict = dict_creator(filename)
      assert dict['question Where does the royal party arrive at Winterfell?'] == 'answer House Stark'

if __name__ == "__main__":
    unittest.main()
