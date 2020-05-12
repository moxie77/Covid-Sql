from db_func import *


cases_file = open("C:/Users/IT/Desktop/pure/covid19/time_series_covid19_confirmed_global.csv")
deaths_file = open("C:/Users/IT/Desktop/pure/covid19/time_series_covid19_deaths_global.csv")



countries_of_choice = ["Italy",'Jamaica','Japan','Jordan']
heading = cases_file.readlines(1)
heading_deaths = deaths_file.readlines(1)

for case_line, death_line in zip(cases_file.readlines(), deaths_file.readlines()):
    
    case_line = case_line.split(",")
    death_line = death_line.split(",")

    country_name = case_line[1]

    if country_name in countries_of_choice:
        country_exists = check_country(country_name)

        if country_exists:

            for data in list(zip(case_line, heading[0].split(","), death_line))[4:]:
                #print(data)
                country_id = country_exists[0]['id']
                date = format_time(data[1])
                cases = data[0]
                deaths = data[2]
                write_case_with_deaths(country_id, date, cases, deaths)

        else:
            write_country(country_name, case_line[2], case_line[3])

