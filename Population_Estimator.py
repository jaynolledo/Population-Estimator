def main():
    print('=== POPULATION GROWTH ESTIMATOR ===')
    print('This program estimates population growth of several countries')
    print()
    
    # Asks user to input Number of countries and years
    # The if statements check if the user inputs a non-positive number 
    numCountries = int(input('Number of countries: '))
    if numCountries <= 0:
        print('Error:', numCountries, 'is not a valid input')
        exit(-1)
    numYears = int(input('Number of years: '))
    if numYears <= 0:
        print('Error:', numYears, 'is not a valid input')
        exit(-1)

    print()
    sum = 0
    countHigh = 0
    countLow = 0
    gr = float('-inf')
    max_yr1 = float('-inf')
    max_final = float('-inf')
    
    # I used a for loop to ask the needed information for each country.
    # Under the for loop are if statements that counts no. of countries w/ high/low growth rates and gets the country w highest yr 1 pop 
    for i in range(1, numCountries + 1):
        print('--- Country', str(i), ' ---')
        countryName = input('Country name: ')
        yr1_pop = float(input('Year 1 population of ' + countryName + ' (in millions): '))
        growth_rate = float(input('Population growth rate (% per year): '))
        if growth_rate > 1:
            countHigh = countHigh + 1
        if growth_rate <= 0.1:
            countLow = countLow + 1
        if growth_rate > gr:
            gr = growth_rate
            highest_gr = countryName
        if yr1_pop > max_yr1:
            max_yr1 = yr1_pop
            max_yr1 = round(max_yr1, 3)
            max_yr1Country = countryName
            
     # Under the main for loop is another for loop that allows the program to compute the population of each country per year from year 2 to year numYears
     # Under this for loop is an if statement that allows the program to get the population of the country with largest final population
        yr_pop = yr1_pop
        for i in range (2, numYears + 1):
            yr_pop = yr_pop + (yr_pop * (growth_rate / 100))
            print('Year ' + str(i) + ' population of ' + countryName + ' (in millions):', round(yr_pop, 3))
        if yr_pop > max_final:
            max_final = yr_pop
            max_final = round(max_final, 3)
            max_finalCountry = countryName
            
    # Sums up final populations of all countries and divides it by numCountries to get the average    
        sum = sum + yr_pop
        average = sum / numCountries
        average = round(average, 3)
        print()
            
    print('Summary Report')
    print('    Average year ' + str(numYears) + ' population of all countries:', average)
    print('    Number of countries with high growth rate:', countHigh)
    print('    Number of countries with low growth rate:', countLow)
    print('    Country with highest growth rate:', highest_gr)
    print('    Country with maximum Year 1 population (' + str(max_yr1) + ' million): ' + max_yr1Country)
    print('    Country with maximum Year ' + str(numYears) + ' population (' + str(max_final) + ' million): ' + max_finalCountry)
            
main()
