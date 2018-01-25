from pymongo import MongoClient



def get_mongodb(**kwargs):
    url = kwargs.get("url", None)
    dbname = kwargs.get("db", None)
    user = kwargs.get("user", None)
    passwd = kwargs.get("passwd", None)
    authdb = kwargs.get("authdb", 'admin')
    if not all([url, dbname, user, passwd, authdb]):
        raise ValueError("params is wrong.")

    client = MongoClient(url)
    db = client[dbname]
    db.authenticate(user, passwd, source=authdb)
    return db
