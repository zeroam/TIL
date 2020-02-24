from singleton import Singleton


@Singleton
class DBConnection(object):
    
    def __init__(self):
        """Initialize your database connection here"""
        pass

    def __str__(self):
        return 'Database connection object'


if __name__ == '__main__':
    c1 = DBConnection.Instance()
    c2 = DBConnection.Instance()

    print('Id of c1 : {}'.format(id(c1)))
    print('Id of c2 : {}'.format(id(c2)))
    print('c1 is c2 ? {}'.format(c1 is c2))
