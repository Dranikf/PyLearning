import unittest;
from name_function import get_formatted_name;

class NamesTestCase(unittest.TestCase):
    """ тесты для 'name_function.py' """
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin');
        self.assertEqual(formatted_name , 'Janis Joplin');

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('fedor' , 'kobak' , 'alekseevich');
        self.assertEqual(formatted_name, 'Fedor Alekseevich Kobak');


unittest.main();
