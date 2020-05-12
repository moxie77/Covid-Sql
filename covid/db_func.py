import pymysql.cursors

#  Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='covid19',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# def create_tables():
#     with connection.cursor() as Cursor:
        
#         create_countries_table = "create table IF NOT EXISTS countries (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(100), lng float, lat float)"

#         Cursor.execute(create_countries_table)

#         create_cases_table = "CREATE table IF NOT EXISTS cases (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL , country_id INT(10), FOREIGN KEY (country_id) REFERENCES countries(id), cases INT(100), `date` DATE)"

#         Cursor.execute(create_cases_table)
        
#         connection.commit()

def create_tables():
    with connection.cursor() as Cursor:
        
        create_countries_table = "create table IF NOT EXISTS countries (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(100), lng float, lat float)"

        Cursor.execute(create_countries_table)

        create_cases_table = "CREATE table IF NOT EXISTS cases_with_deaths (id int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL , country_id INT(10), FOREIGN KEY (country_id) REFERENCES countries(id), cases INT(100), deaths INT(100), `date` DATE)"

        Cursor.execute(create_cases_table)
        
        connection.commit()


def write_country(name, lng, lat):

    with connection.cursor() as Cursor:
        
        add_country = f"INSERT INTO countries (name, lat, lng) values('{name}','{lat}','{lng}')"

        Cursor.execute(add_country)
        
        connection.commit()

def write_case(country_id,date,cases):
    with connection.cursor() as Cursor:
        add_case = f"INSERT INTO cases(country_id, date, cases) values('{country_id}','{date}','{cases}')"

        Cursor.execute(add_case)
        connection.commit()

def write_case_with_deaths(country_id, date, cases, deaths):

    with connection.cursor() as Cursor:
        
        add_case = f"INSERT INTO cases_with_deaths (country_id, date, cases, deaths) values('{country_id}','{date}','{cases}', '{deaths}')"

        Cursor.execute(add_case)
        
        connection.commit()

def check_country(name):
    with connection.cursor() as Cursor:
        
        get_country = f"SELECT * FROM countries where name = '{name}'"

        Cursor.execute(get_country)
        
        return Cursor.fetchall()   

        
def format_time(date):
    
    "1/22/20" # before split
    month, day, year = date.split("/") #["1","22", "20"] #after split
   
    fixed_date = "-".join([year.replace('\n','')+'20', month, day]) #20+20 ==== 2020
    "2020-1-22"
    return fixed_date

# write_country("Nigeria", 1.89, 1.0923)
write_case(1, "2020-01-02", 23)
#create_tables()