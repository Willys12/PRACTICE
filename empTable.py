#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData


engine = create_engine('sqlite:///example.db')

metadata = MetaData()

emp_salary = Table('emp_salary', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String), Column('email', String))

metadata.create_all(engine)
