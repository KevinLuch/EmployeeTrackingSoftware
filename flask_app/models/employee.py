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


    @classmethod 
    def get_all_employees(cls):
        employees = connectToMySQL('employee').query_db("SELECT * FROM employees;")

        results = []
        for employee in employees:
            results.append(cls(employee))

        return results 