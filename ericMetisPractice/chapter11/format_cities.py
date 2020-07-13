def format_cities(country , citie, population = None):
    if population != None:
        result = (country.lower() + ', ' + citie.lower()).title() + ' - population ' + str(population);
    else:
        result = (country.lower() + ', ' + citie.lower()).title();
    
    return result;
