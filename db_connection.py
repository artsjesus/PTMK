from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self, db_url='postgresql://postgres:password@localhost/namebd'):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_all(self):
        from employee import Base
        Base.metadata.create_all(self.engine)

    def add_employee(self, employee):
        self.session.add(employee)
        self.session.commit()

    def get_all_employees(self):
        from employee import Employee
        return self.session.query(Employee).order_by(Employee.full_name).all()

    def search_employees(self, *filters):
        from employee import Employee
        query = self.session.query(Employee)
        for filter_condition in filters:
            query = query.filter(filter_condition)
        return query.all()

    def bulk_add(self, employees):
        self.session.bulk_save_objects(employees)
        self.session.commit()

    def close(self):
        self.session.close()
