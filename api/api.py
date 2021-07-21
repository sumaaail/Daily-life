from operation.operation import Operation


def demo_select(cmd):
    table = 'students'
    columns = ['NAME', 'ADDRESS']
    constraint = ' where ' + 'ID = 2'
    op = Operation()
    data = op.db_select(table, columns, constraint)
    return data


# UserLogin and registration


# input the uname for uid
def select_id_by_uname(cmd):
    table = 'user'
    column = ['uid']
    constraint = ' WHERE uname = "{}"'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    print(type(data))
    return data


# input the table name for selection
def select_all(cmd):
    table = cmd
    columns = '*'
    op = Operation()
    data = op.db_select(table, columns)
    print(type(data))
    return data


# input the uname for check
def select_uname(cmd):
    table = 'user'
    column = ['uname']
    op = Operation()
    data = op.db_select(table, column)
    print(type(data), data)
    return data


# input the uname to login
def select_pwd_by_uname(cmd):
    table = 'user'
    column = ['pwd']
    constraint = ' WHERE uname = "{}"'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    print(type(data), data)
    return data


# input the values for registration
def user_register(cmd):
    table = 'user'
    columns = str(('uname', 'pwd', 'phone'))
    values = str(tuple(cmd))
    op = Operation()
    op.db_insert(table, columns, values)
    return 1


# input the uname for delete account
def delete_account_by_uname(cmd):
    table = 'user'
    constraint = ' WHERE uname = "{}"'.format(cmd)
    op = Operation()
    op.db_delete(table,constraint)
    return 1
################################################################################################

# favourite table

# input the values for save favourites
def insert_fav(cmd):
    table = 'fav'
    columns = ['uid', 'fav']
    values = cmd
    op = Operation()
    op.db_insert(table, columns, values)
    return 1


# input the uid to fetch the fav
def select_fav_by_uid(cmd):
    table = 'fav'
    column = ['fav']
    constraint = ' WHERE uid = {}'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    return data


#########################################################################################################

