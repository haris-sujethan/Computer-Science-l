from t6 import term_freq

new_dict = term_freq('unique_QA_Pairs.txt')

with open('Decreasing_Frequency.txt', 'w') as f:
    dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
    for key in dict:
        newlnStr = str(key) + ',' + str(dict[key])
        f.write(newlnStr)
        f.write('\n')
        
        
        
import unittest

class Testing(unittest.TestCase):

   def test_func_1(self):
    
     assert dict["wife"] == 4
   def test_func_2(self):

      assert dict['react'] == 1

if __name__ == "__main__":
    unittest.main()
    
    
