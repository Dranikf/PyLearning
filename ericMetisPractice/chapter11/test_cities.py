from format_cities import format_cities;
import unittest;

class test_cities(unittest.TestCase):
    def  test_city_country(self):
        formatted_citie_country = format_cities('beLaRus','MiNSK');
        self.assertEqual(formatted_citie_country ,'Belarus, Minsk');

    def test_city_country_population(self):
        formatted_citie_country = format_cities('Litva' , 'vilnus' , 1500000);
        self.assertEqual(formatted_citie_country , 'Litva, Vilnus - population 1500000');

unittest.main();
