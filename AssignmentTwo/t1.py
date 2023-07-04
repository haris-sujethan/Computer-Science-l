# Question One

def pair_creator(filename: str):
    """Takes in a file name,
    and creates pairs of Q and As
    """
    file = open(filename, 'r', encoding='utf-8-sig')
    pair_arr = []
    with open(filename, 'r', encoding='utf-8-sig') as x:
        # removes the space character
        list_contents = [line.rstrip('\n') for line in x]
        # removes random character in start of line



    for x in range(0, len(list_contents) - 1):
        line = list_contents[x].split()
        line2 = list_contents[x + 1].split()

        line_txt = list_contents[x]
        line2_txt = list_contents[x + 1]
        if line[0] == "answer":
            if line2[0] == "question":
                pair_arr.append((line2_txt, line_txt))

    file.close()
    return pair_arr




import unittest

class Testing(unittest.TestCase):

   def test_func_1(self):
     assert len(pair_creator('QA_Pairs.txt'))==5725

   def test_func_2(self):
      assert pair_creator('QA_Pairs.txt')[0] == ("question Who is Arya Stark's wife?", 'answer Lady Catelyn Stark')

if __name__ == "__main__":
    unittest.main()


    
        
        



