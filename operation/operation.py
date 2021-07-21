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
        get_db().commit()

        return data

    def db_insert(self, table, columns="", values=""):
        '''

        :param table: table name
        :param columns: columns in table
        :param values: values to be inserted
        :return:
        '''
        cur = get_db().cursor()
        cmd = "INSERT INTO " + table + " " + columns + " VALUES " + values
        print(cmd)
        cur.execute(cmd)
        get_db().commit()

        print("insert successfully")


    def db_update(self, table, columns, values, constraint=""):
        '''
        
        :param table: 
        :param columns:
        :param values:
        :param constraint: 
        :return: 
        '''
        cur = get_db().cursor()
        cmd = "UPDATE " + table + " SET " + columns + " = " + values + constraint
        print(cmd)
        cur.execute(cmd)
        get_db().commit()

        print("update successfully")


    def db_delete(self, table, constraint=""):
        '''

        :param table:
        :param constraint:
        :return:
        '''
        cur = get_db().cursor()
        cmd = "DELETE FROM " + table + constraint
        print(cmd)
        cur.execute(cmd)
        get_db().commit()

        print("delete successfully")