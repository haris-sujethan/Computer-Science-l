#Question Two

from t1 import pair_creator

qa_arr = pair_creator('QA_Pairs.txt')


def unique_overlapping_separator(qa_arr:list):
    """Splits the overlapping questions and answers

    """
    unique_pairs = list(qa_arr)
    overlapping = []
    
    x = 0
    while x <= len(unique_pairs):
        y = int(x) + 1
        while y < len(unique_pairs):

            if unique_pairs[x][0].lower() == unique_pairs[y][0].lower() and unique_pairs[x][1].lower() == \
                    unique_pairs[y][1].lower():

                overlapping.append(unique_pairs[y])

                indices = [i for i, x in enumerate(unique_pairs) if x == unique_pairs[y]]
                unique_pairs.pop(indices[-1])

            elif unique_pairs[x][0].lower() == unique_pairs[y][0].lower():

                overlapping.append(unique_pairs[y])
                indices = [i for i, x in enumerate(unique_pairs) if x == unique_pairs[y]]
                unique_pairs.pop(indices[-1])

            elif unique_pairs[x][1].lower() == unique_pairs[y][1].lower():
                overlapping.append(unique_pairs[y])
                indices = [i for i, x in enumerate(unique_pairs) if x == unique_pairs[y]]
                unique_pairs.pop(indices[-1])
            y += 1
        x += 1

    return(unique_pairs, overlapping)



answers = unique_overlapping_separator(qa_arr)

with open('unique_QA_Pairs.txt', 'w') as f:
    for line in answers[0]:
        f.write(line[0])
        f.write('\n')
        f.write(line[1])
        f.write('\n')

with open('Overlapping.txt', 'w') as f:
    for line in answers[1]:
        f.write(line[0])
        f.write('\n')
        f.write(line[1])
        f.write('\n')



import unittest

class Testing(unittest.TestCase):

    def test_length(self):
        test_arr = pair_creator('QA_Pairs.txt')
        test_tuple = unique_overlapping_separator(test_arr)
        assert len(test_arr) == len(test_tuple[0]) + len(test_tuple[1])

    def test_uppercase(self):
        upperList = [("AAA", "BBB"), ("ccc", "ddd"), ("eee", "BBB"), ("ggg", "hhh"), ("aaa", "bbb")]
        test_tuple = unique_overlapping_separator(upperList)


        assert test_tuple[0] == [('AAA', 'BBB'), ('ccc', 'ddd'), ('ggg', 'hhh')]
        assert test_tuple[1] == [('eee', 'BBB'), ('aaa', 'bbb')]


if __name__ == "__main__":
    unittest.main()



       

  