'''
Author: Forked from https://github.com/render-examples/flask-hello-world.git, edits by Nandini Mahesh Bhat
CU ID: nabh6611
GitHub User Name: nabhCO
'''

from flask import Flask
import psycopg2
app = Flask(__name__)

#index route (landing page)
@app.route('/')
def hello_world():
    return 'Hello World from Nandini Bhat in 3308'
    
    

#route for testing database connection
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://hello_world_db_v0i1_user:Jv5R5vjnTCEJ6rxXoBluoI7u8JKDg1zx@dpg-d797f66uk2gs73e8c7ug-a/hello_world_db_v0i1")
    conn.close()
    return "Successfully connected to database"
    
    

#adds table called "Basketball" to database if it does not already exist (you can navigate to /db_drop to drop table before creating)
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


    
#adds data to the Basketball table
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



#selects and displays each of the rows in the Basketball table in the form of an HTML table
@app.route('/db_select')
def db_select():

    conn = psycopg2.connect("postgresql://hello_world_db_v0i1_user:Jv5R5vjnTCEJ6rxXoBluoI7u8JKDg1zx@dpg-d797f66uk2gs73e8c7ug-a/hello_world_db_v0i1")
    cur = conn.cursor()

    cur.execute('''
    SELECT * FROM Basketball;
    ''')

    records = cur.fetchall()

    table_str = "<table>"

    for row in records:
        table_str += "<tr>"
        
        for data in row:
            table_str += "<td> {} </td>".format(data)
            
        table_str += "</tr>"
        
    table_str += "</table>"

    return table_str


        
#drops the Basketball database (can be recreated with db_create)        
@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://hello_world_db_v0i1_user:Jv5R5vjnTCEJ6rxXoBluoI7u8JKDg1zx@dpg-d797f66uk2gs73e8c7ug-a/hello_world_db_v0i1")
    cur = conn.cursor()

    cur.execute('''
    DROP TABLE Basketball;
    ''')

    conn.commit()
    conn.close()
    return "Successfully dropped Basketball table"

    

    
    

