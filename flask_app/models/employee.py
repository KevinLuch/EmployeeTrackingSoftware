from flask_app.config.mysqlconnection import connectToMySQL

class Employee():

    def __init__(self, data):
        self.id = data['id']
        self.department_id = data['department_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.salary = data['salary']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @classmethod 
    def get_all_employees(cls):
        employees = connectToMySQL('employee').query_db("SELECT * FROM employees;")

        results = []
        for employee in employees:
            results.append(cls(employee))

        return results 

    @classmethod
    def create_employee(cls, data):

        connection = connectToMySQL('employee')
        query = "INSERT INTO employees (department_id, first_name, last_name, salary, created_at, updated_at) VALUES (%(department_id)s, %(first_name)s, %(last_name)s, %(salary)s, NOW(), NOW());"
        new_employee_id = connection.query_db(query, data)

        return new_employee_id

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM employees WHERE id = %(id)s;"
        
        return connectToMySQL('employee').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM employees WHERE id = %(id)s;"
        # Data coming back is a list
        results = connectToMySQL('employee').query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_employee(cls, data):
        query = "UPDATE employees SET first_name = %(first_name)s, last_name = %(last_name)s, salary=%(salary)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('employee').query_db(query, data)
