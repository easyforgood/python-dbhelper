import dbhelper  as db

dbhelper = db.factory.get_mysql("backup")

res = dbhelper.queryall("select order_code from test limit 0,1")

print(res[0][0])


dbhelper.execsql("update %s set order_code=1 ", ("test"))



