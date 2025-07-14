from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_data():
    conn = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, capital, area, poblacion FROM provincias")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    provincias = get_data()
    return render_template('map.html', provincias=provincias)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
