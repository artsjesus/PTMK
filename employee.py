import datetime
from sqlalchemy import Column, Integer, String, Date, Index
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Модель сотрудника
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String, nullable=False)

    # Индексы для ускорения запросов
    __table_args__ = (
        Index('ix_gender', 'gender'),
        Index('ix_full_name', 'full_name'),
    )

    def __init__(self, full_name, birth_date, gender):
        self.full_name = full_name
        self.birth_date = birth_date
        self.gender = gender

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __repr__(self):
        return f"<Employee(id={self.id}, full_name={self.full_name}, birth_date={self.birth_date}, gender={self.gender}, age={self.age()})>"
