import cx_Oracle
from flask import Flask, render_template

app = Flask(__name__)

dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', service_name='XE')
conn = cx_Oracle.connect(user='SAI', password='ORACLE', dsn=dsn_tns)

@app.route('/retrieve_data')
def retrieve_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    data = cursor.fetchall()
    cursor.close()

    return render_template('display_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
