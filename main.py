# tutorial followed for sql: https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91

from queens import get_all_possible_solutions
import sqlalchemy as db
from sqlalchemy import (
    create_engine,
    Table
)

n = 8
solutions = get_all_possible_solutions(n)

engine = create_engine('postgresql+psycopg2://user:123456@db/queens')
connection = engine.connect()
metadata = db.MetaData()

solutions_table = Table('solutions_table', metadata, db.Column('id', db.Integer(), db.Sequence('id'), primary_key=True), db.Column('simple_solution_string', db.String(15), nullable=False))

solutions_table.drop(engine, checkfirst=True)
solutions_table.create(engine)

for solution in solutions:
    # uncomment this line to see the raw output
    # print(solution.to_string())
    query = db.insert(solutions_table).values(simple_solution_string = solution.to_simple_string())
    connection.execute(query)

# comment in here if you want to see the raw output
query = db.select([solutions_table])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()

for row in ResultSet:
    print(row)