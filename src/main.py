from queens import get_all_possible_solutions
import sqlalchemy as db
from sqlalchemy import (
    create_engine,
    Table
)

n = 10
solutions = get_all_possible_solutions(n)

engine = create_engine('postgresql://localhost/testdb')
connection = engine.connect()
metadata = db.MetaData()

test_table = Table('test_table', metadata, db.Column('test_id', db.Integer(), db.Sequence('id'), primary_key=True), db.Column('test_string', db.String(25), nullable=False))

test_table.drop(engine)
test_table.create(engine)

query = db.insert(test_table).values(test_string = "Bye World")
connection.execute(query)