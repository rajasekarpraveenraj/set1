#to print list of leap years in a list from the given year
def find_leap_years(given_year):
    list_of_leap_years=[]
    while(len(list_of_leap_years)<15):
        if given_year%4==0:
            if given_year%100==0:
                if given_year%400==0:
                    list_of_leap_years.append(given_year)
                    given_year=given_year+1
                else:
                    given_year=given_year+1
            else:
                list_of_leap_years.append(given_year)
                given_year=given_year+1
        else:
            given_year=given_year+1
    return list_of_leap_years
list_of_leap_years=find_leap_years(2004)
print(list_of_leap_years)        
            
