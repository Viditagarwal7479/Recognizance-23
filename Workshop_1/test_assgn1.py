import unittest
import Assignment1 
import numpy as np

class TestAssignment1(unittest.TestCase):

    def test_square(self):
        self.assertEqual(Assignment1.square(4), 16)

    def test_word_is_palindrome(self):
        self.assertEqual(Assignment1.word_is_palindrome('madam'), True)
        self.assertEqual(Assignment1.word_is_palindrome('abcd'), False)
        self.assertEqual(Assignment1.word_is_palindrome('12321'), True)
        self.assertEqual(Assignment1.word_is_palindrome('abc cba'), True)

    def test_sqrt_of_numbers(self):
        self.assertEqual(Assignment1.sqrt_of_numbers(4), 2)
        self.assertEqual(Assignment1.sqrt_of_numbers(6), 2.45)
        self.assertEqual(Assignment1.sqrt_of_numbers(9.0), 3.0)
        self.assertEqual(Assignment1.sqrt_of_numbers(68), 8.25)
        self.assertRaises(ValueError, Assignment1.sqrt_of_numbers, -1)

    def test_Maximum(self):
        self.assertEqual(Assignment1.Maximum([1,2,3,4,5]), (5,4))
        self.assertEqual(Assignment1.Maximum([0,0,0,0]), (0,0))
    
    def test_even_sort(self):
        self.assertEqual(Assignment1.even_sort([1,2,3,4,5]), [2,4,1,3,5])
        self.assertEqual(Assignment1.even_sort([7,1,5,3]), [1, 3, 5, 7])
        self.assertEqual(Assignment1.even_sort([0,0,0,0]), [0,0,0,0])

    def test_eqn_solver(self):
        self.assertEqual(Assignment1.eqn_solver([1,2], [3,4], [5,6]), (-1.0, 2.0))
        self.assertEqual(Assignment1.eqn_solver([1,1], [1,-1], [2,0]), (1.0, 1.0))

    def test_swap_case(self):
        self.assertEqual(Assignment1.swap_case('Hello'), 'hELLO')
        self.assertEqual(Assignment1.swap_case('Hello World'), 'hELLO wORLD')

    def test_is_prime(self):
        self.assertEqual(Assignment1.is_prime(5), True)
        self.assertEqual(Assignment1.is_prime(4), False)

    def test_is_leap_year(self):
        self.assertEqual(Assignment1.is_leap_year(2000), True)
        self.assertEqual(Assignment1.is_leap_year(2001), False)
        self.assertEqual(Assignment1.is_leap_year(2004), True)
        self.assertEqual(Assignment1.is_leap_year(1700), False)

    def test_is_perfect_square(self):
        self.assertEqual(Assignment1.is_perfect_square(4), True)
        self.assertEqual(Assignment1.is_perfect_square(5), False)

    def test_is_perfect_number(self):
        self.assertEqual(Assignment1.is_perfect_number(6), True)
        self.assertEqual(Assignment1.is_perfect_number(5), False)

    def test_resize_array(self):
        self.assertEqual(Assignment1.resize_array([1,2,3,4,5,6]).tolist(), np.array([[1,2,3],[4,5,6]]).tolist())

    def test_reverse_step_array(self):
        self.assertEqual(Assignment1.reverse_step_array([1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 6, 3])

    def test_reverse_words(self):
        self.assertEqual(Assignment1.reverse_words('Hello World'), 'World Hello')
        self.assertEqual(Assignment1.reverse_words('hehe gotcha'), 'gotcha hehe')

    def test_count_characters(self):
        self.assertEqual(Assignment1.count_characters('Hello World'), {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1})
        self.assertEqual(Assignment1.count_characters("hehe gotcha"), {'h': 3, 'e': 2, 'g': 1, 'o': 1, 't': 1, 'c': 1, 'a': 1})
        self.assertEqual(Assignment1.count_characters("aaa111   bbb"), {'a': 3, '1': 3, 'b': 3})
        self.assertEqual(Assignment1.count_characters("      "), {})

    def test_remove_special_characters(self):
        self.assertEqual(Assignment1.remove_special_characters("Hello, World! 123$ th15 1s 4 t35t str1ng"), "Hello World 123 th15 1s 4 t35t str1ng")
        self.assertEqual(Assignment1.remove_special_characters("he##llo123%  *-  abc 12  ab23"), "hello123    abc 12  ab23")
        self.assertEqual(Assignment1.remove_special_characters("###"), "")
        self.assertEqual(Assignment1.remove_special_characters("### "), " ")

    def test_tuple_of_tuples(self):
        self.assertEqual(Assignment1.sort_tuple_of_tuples((('a', 55), ('z', 1), ('f', 37), ('w', 19))), (('z', 1), ('w', 19), ('f', 37), ('a', 55)))
        self.assertEqual(Assignment1.sort_tuple_of_tuples(((77 , 55), (55 , 1), (68 , 37), (0 , 19))), ((55, 1), (0, 19), (68, 37), (77, 55)))
        self.assertEqual(Assignment1.sort_tuple_of_tuples((), ()), ((), ()))

    def test_alpha_numeric_words(self):
        self.assertEqual(Assignment1.alpha_numeric_words("Hey there33 how11 are you1"), "there33 how11 you1")
        self.assertEqual(Assignment1.alpha_numeric_words("hey"), "")
        self.assertEqual(Assignment1.alpha_numeric_words(""), "")

    def test_count_them_all(self):
        self.assertEqual(Assignment1.count_them_all("IdDk3837#$fsd%%"), {'Characters': 7, 'Numbers': 4, 'Symbols': 4})
        self.assertEqual(Assignment1.count_them_all("jsWW 567tt    kf&^%$66  "), {'Characters': 8, 'Numbers': 5, 'Symbols': 4})
        self.assertEqual(Assignment1.count_them_all("  "), {'Characters': 0, 'Numbers': 0, 'Symbols': 0})

    def test_hash_supremacy(self):
        self.assertEqual(Assignment1.hash_supremacy("&He was a^%$ great @guy"), "#He was a### great #guy")
        self.assertEqual(Assignment1.hash_supremacy("###############"), "###############")
        self.assertEqual(Assignment1.hash_supremacy("  "), "  ")
        self.assertEqual(Assignment1.hash_supremacy("&&&&&&&&"), "########")
        

if __name__ == '__main__':
    unittest.main()