from functools import reduce, wraps
from .factory import factory



def export(_dbhelper, filename=None):
    """
        @dbhelper
        @filename if filename == None , will return query results else return filename
    """
    dbhelper = _dbhelper
    if isinstance(_dbhelper, str):
        dbhelper = factory.get_mysql(_dbhelper)

    def wrapperfunc(sqlfunc):
        @wraps(sqlfunc)
        def dofunc(*args, **kwargs):
            sqls = sqlfunc(*args, **kwargs)
            if isinstance(sqls, str):
                sqls = [sqls]
            if isinstance(sqls, list):
                return __query(dbhelper, sqls, filename)
            raise ValueError("proxy func is not return sql or sql list")

        return dofunc

    return wrapperfunc


def __query(dbhelper, sqls, filename=None):
    results = reduce(lambda a, b: a + b,
                     [dbhelper.queryall(sql) for sql in sqls])
    if not filename:
        return results
    with open(filename, "w") as f:
        f.writelines("\n".join([str(res) for res in results]))
        return filename


def shardsql(inputrange= 100):
    if isinstance(inputrange, int):
        inputrange = range(inputrange)
    if isinstance(inputrange, list) or isinstance(inputrange, range):
        _range = inputrange 
    else:
        raise ValueError("shardsql params error")
    def wrapperfunc(sqlfunc):
        def func(*args, **kwargs):
                return [
                    sqlfunc(*args, **kwargs).format("{:0>2}".format(_tag))
                    for _tag in(_range)
                ]

        return func

    return wrapperfunc
