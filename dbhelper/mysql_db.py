# -*- coding: utf-8 -*-
import logging
import MySQLdb
from functools import wraps


class DBHelper(object):
    host = ""
    port = ""
    username = ""
    password = ""
    dbname = ""
    conn = None

    def __init__(self, host, port, user, pwd, db,**kwargs):
        self.logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.username = user
        self.password = pwd
        self.db = db
        self.conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            passwd=pwd,
            db=db,
            charset='utf8',**kwargs)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn is not None:
            self.conn.close()

    # decorator
    def mysqldb(sqlfunc):
        def wrapper(self, sql, params=None):
            c = self.conn.cursor()
            results = sqlfunc(self, sql, params, c)
            c.close()
            return results

        return wrapper

    #return decorator
    @mysqldb
    def execsql(self, sql, params=None, cursor=None):
        try:
            cursor.execute(sql, params)
            self.conn.commit()
        except MySQLdb.Error as e:
            self.logger.error('Failed to open file', exc_info=True)
            self.conn.rollback()

    @mysqldb
    def queryall(self, sql, params=None, cursor=None):
        if cursor is None:
            self.logger.warn("[cursor none]")
            return
        cursor.execute(sql, params)
        results = cursor.fetchall()
        return results

    @mysqldb
    def execmany(self, sql, params=None, cursor=None):
        try:
            cursor.executemany(sql, params)
            self.conn.commit()
        except MySQLdb.Error as e:
            self.logger.error('Failed to open file', exc_info=True)
            self.conn.rollback()


    # decorate
class EasyDBHelper(DBHelper):
    def __init__(self, connmap):
        super(EasyDBHelper,
              self).__init__(connmap["host"], connmap["port"], connmap["user"],
                             connmap["pwd"], connmap["db"])
