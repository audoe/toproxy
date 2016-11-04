

DBNAME = 'ad'
MYSQL_DATABASES =  {
    'write':  {
       'host':'127.0.0.1',
       'user':'root',
       'port':3306,
       'db':DBNAME,
       'charset':'utf8',
       'passwd':'',
       'connect_timeout':10,
       'use_unicode':False
    },
    'read':  {
       'host':'127.0.0.1',
       'user':'root',
       'port':3306,
       'db':DBNAME,
       'charset':'utf8',
       'passwd':'',
       'connect_timeout':10,
       'use_unicode':False
    }
}


