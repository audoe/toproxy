#coding:utf-8
import os,sys
import datetime,time
import MySQLdb
import traceback
from settings import MYSQL_DATABASES,DBNAME
import datetime,time,uuid
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)


cteate_ad_table_sql = u'''
CREATE TABLE IF NOT EXISTS `ad_info` (
  `id` int(11) AUTO_INCREMENT,
  `title` varchar(255),
  `create_time` DATETIME,
  `ad_type` varchar(255),
  `description` varchar(255),
  `url` varchar(255),
  `imgs` varchar(255),
  `is_game_ad` int(4)

) ENGINE=InnoDB CHARSET=utf8;
'''

def get_conn(alias='write',connect_timeout=10,use_db = True):
    the_conn = None
    try:
        the_conn_c = MYSQL_DATABASES.get(alias, {})
        
        the_conn = MySQLdb.connect(host=the_conn_c['host'], user=the_conn_c['user'], passwd=the_conn_c['passwd'], port=int(the_conn_c.get('port',3306)),charset='utf8',connect_timeout=connect_timeout)
        if use_db:
            the_conn.select_db(the_conn_c['db'])
        the_conn.autocommit(1)
    except Exception, e:
        traceback.print_exc()
        raise Exception, e
    return the_conn

def create_database():
    conn = get_conn('write',use_db=False)
    conn.cursor().execute('CREATE DATABASE IF NOT EXISTS %s; ' % DBNAME)
    conn.close()
    
    
class DBconn(object):
    
    def __init__(self):
        self.conns = {}
    def close(self):
        try:
            for k,conn in self.conns.items():
                try:
                    conn.close()
                except:
                    pass
        except:
            pass
    def __call__(self,alias):
        the_conn = self.conns.get(alias,None)
        if the_conn == None:
            the_conn = get_conn(alias)
            self.conns[alias] = the_conn
        return the_conn
    
    
class DBmodel(object):
    def __init__(self):
        self._conn = DBconn()
        self._table_name = ''
        self._fields = []
        self.id       = 0
        

    def query_one(self,condition_str):
        condition_str = '%s limit 1' % condition_str
        result =  self._query(condition_str).fetchone()
        if result:
            self.setattr(result)
            return self
        return result
    
    def setattr(self,result):
        if result:
            for f_namne in self._fields:
                    value = result.get(f_namne,'')
                    setattr(self,f_namne,value)
                
                
    def query(self,condition_str):
        return self._query(condition_str).fetchall()
    
    
    def lock(self):
        if self._table_name:
            self.conn('write').autocommit(0)
            self.conn('write').cursor().execute('LOCK TABLES %s WRITE;' % self._table_name)

    def unlock(self):
            self.conn('write').cursor().execute('UNLOCK TABLES;')
            self.conn('write').autocommit(1)
    
    def save(self):
        cur = self._conn('write').cursor()
        update_files = []
        values = []
        for f_namne in self._fields:
            if f_namne == 'id':
                continue
            value = getattr(self,f_namne,None)
            if value!=None:
                update_files.append('%s=%%s' % f_namne)
                values.append(value)
            
        if self.id:
            the_sql = '''UPDATE %s Set  %s
                        where id = %d
                        ''' % (self._table_name,','.join(update_files),int(self.id))
        else:
            the_sql = ''' INSERT INTO %s SET
                        %s
                    ''' % (self._table_name,','.join(update_files))
        cur.execute(the_sql,values)
        self._conn('write').commit()
        if not self.id:
            self.id = int(cur.lastrowid)
        return self
        
    
    def _query(self,condition_str='',alias='read'):
        the_sql = 'select * from %s' % self._table_name
        if condition_str:
            the_sql = '%s where %s' % (the_sql,condition_str)
        cur = self._conn(alias).cursor(MySQLdb.cursors.DictCursor)
        cur.execute(the_sql)

        return cur

    def close(self):
        try:
            if self._conn:
                self._conn.close()
        except:
            pass

class AdInfo(DBmodel):
        
    def __init__(self):
        super(AdInfo,self).__init__()
        self._table_name = 'ad_info'
        self._fields = ["id",
                        "title",
                        "description",
                        "ad_type",
                        "create_time",
                        "url",
                        "is_game_ad",
                        "imgs"
                        ]
        for f_name in self._fields:
            setattr(self,f_name,'')
    
        
    def _create_table(self):
        cur = self._conn('write').cursor()
        the_sql  = cteate_ad_table_sql
        cur.execute(the_sql)
        

if __name__ == '__main__':
    p = AdInfo()
    p._create_table()
    print p.id
    p.title='asdasd'
    p.save()
    print p.id
    print p.query("")
    print p.title
