import cx_Oracle
from flask import Flask, request

app = Flask(__name__)

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='SAI', password='ORACELE', dsn=dsn_tns)

@app.route('/submit_data', methods=['POST'])
def submit_data():
    name = request.form['name']
    email = request.form['email']
    age = int(request.form['age'])
    dob = request.form['dob']

    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_data (name, email, age, dob) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))", (name, email, age, dob))
    conn.commit()
    cursor.close()

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
