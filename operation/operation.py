from db_config import *



class Operation():
    def __init__(self):
        self.__fields__ = []

    def db_select(self, table, columns=[], constraint=""):
        '''

        :param table: table name
        :param columns: columns to be selected
        :param constraint: constraint of the select
        :return:
        '''
        data = []
        cur = get_db().cursor()
        cmd = "SELECT " + ','.join(columns) + " FROM " + table + constraint
        print(cmd)
        for row in cur.execute(cmd):
            data.append(row)
        return data

    def db_insert(self, table, columns, values):
        '''

        :param table: table name
        :param columns: columns in table
        :param values: values to be inserted
        :return:
        '''
        pass

    def db_update(self, table, columns, values, constraint):
        '''
        
        :param table: 
        :param columns: 
        :param values: 
        :param constraint: 
        :return: 
        '''
        pass

    def db_delete(self, table, constraint):
        '''

        :param table:
        :param constraint:
        :return:
        '''
        pass
