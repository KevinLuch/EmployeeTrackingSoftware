from flask import Flask, render_template, request, session, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'yeezy yeezy yeezy'

@app.route('/')
def index():
    connection = connectToMySQL('employee')
    employees = connection.query_db('SELECT * FROM employees;')
    connection = connectToMySQL('employee')
    departments = connection.query_db('SELECT * FROM departments;')
    return render_template('index.html', employees = employees, departments = departments)

@app.route('/employees/create', methods=['POST'])
def create_employee():
    connection = connectToMySQL('employee')

    query = "INSERT INTO employees (department_id, first_name, last_name, salary, created_at, updated_at) VALUES (%(department_id)s, %(first_name)s, %(last_name)s, %(salary)s, NOW(), NOW());"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'salary': request.form['salary'],
        'department_id': request.form['department_id'],
    }

    connection.query_db(query, data)

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)