def term_freq(filename: str):
    dic ={}
    file = open(filename, 'r', encoding='utf-8-sig')
    pair_arr = []
    with open(filename, 'r', encoding='utf-8-sig') as x:
        # removes the space character
        list_contents = [line.rstrip('\n') for line in x]
    for x in range(0, len(list_contents) - 1):

        line = list_contents[x].split()
        
        for word in line:
            if word in dic or word.lower() in dic:
                dic[word.lower()] = dic[word.lower()] + 1
            else:
                dic[word.lower()] = 1

    return dic


with open('Frequency.txt', 'w') as f:
    dict = term_freq('unique_QA_Pairs.txt')
    for key in dict:
        newlnStr =  str(key)+ ',' + str(dict[key])
        f.write(newlnStr)
        f.write('\n')


term_freq('unique_QA_Pairs.txt')


import unittest

class Testing(unittest.TestCase):

   def test_func_1(self):
     dict = term_freq('unique_QA_Pairs.txt')
     assert dict["wife"] == 4
   def test_func_2(self):
      dict = term_freq('unique_QA_Pairs.txt')
      assert dict['react'] == 1

if __name__ == "__main__":
    unittest.main()