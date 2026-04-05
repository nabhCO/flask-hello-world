from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Nandini Bhat in 3308'


@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://hello_world_db_v0i1_user:Jv5R5vjnTCEJ6rxXoBluoI7u8JKDg1zx@dpg-d797f66uk2gs73e8c7ug-a/hello_world_db_v0i1")
    conn.close()
    return "Successfully connected to database"


@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://hello_world_db_v0i1_user:Jv5R5vjnTCEJ6rxXoBluoI7u8JKDg1zx@dpg-d797f66uk2gs73e8c7ug-a/hello_world_db_v0i1")
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')

    conn.commit()
    conn.close()
    return "Successfully created Basketball table"
    

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://hello_world_db_v0i1_user:Jv5R5vjnTCEJ6rxXoBluoI7u8JKDg1zx@dpg-d797f66uk2gs73e8c7ug-a/hello_world_db_v0i1")
    cur = conn.cursor()

    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')

    conn.commit()
    conn.close()
    return "Successfully added data to Basketball table"
    
    