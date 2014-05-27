# coding: utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

db = sqlite3.connect('./azure.db')
cur = db.cursor()
try:
    cur.execute('drop table searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

class AzureCmdletsPipeline(object):
    def process_item(self, item, spider):
        f = open('download/%s.htm' % item['title'], 'w')
        f.write("""<html> <head> <link rel='stylesheet' type='text/css' href='azure.css' /> </head> <body id='top' class="page-"> <div id='page'>""")
        f.write(item['content'].encode('utf8'))
        f.write('</div></body></html>')
        f.close()
        cur.execute('insert or ignore into searchIndex(name, type, path) values (?, ?, ?)', (item['title'], 'func', '%s.htm' % item['title']))
        db.commit()
        #import pdb; pdb.set_trace()
