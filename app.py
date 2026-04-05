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