from operation.operation import Operation
from flask import jsonify

def demo_select(cmd):
    table = 'students'
    columns = ['NAME', 'ADDRESS']
    constraint = ' where ' + 'ID = 2'
    op = Operation()
    data = op.db_select(table,columns,constraint)
    return jsonify(data)

def select_all(cmd):
    table = cmd
    columns = '*'
    op = Operation()
    data = op.db_select(table,columns)
    print(type(data))
    return jsonify(data)

def select_column(cmd):
    pass

def insert_log(cmd):
    pass