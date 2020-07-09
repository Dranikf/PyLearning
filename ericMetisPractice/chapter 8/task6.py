def city_country(sity , country):
    sity = sity.lower().title();
    country = country.lower().title();
    return sity + ', ' + country;

print(city_country('minsk' , 'belaRUs'));
print(city_country('moSkow' , 'rUSSIA'));
print(city_country('loNdon' , 'Great britan'));

