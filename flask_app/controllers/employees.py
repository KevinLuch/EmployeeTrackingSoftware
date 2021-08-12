from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.employee import Employee 

@app.route('/')
def index():
    # connection = connectToMySQL('employee')
    # employees = connection.query_db('SELECT * FROM employees;')
    connection = connectToMySQL('employee')
    departments = connection.query_db('SELECT * FROM departments;')
    return render_template('index.html', employees = Employee.get_all_employees(), departments = departments)

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