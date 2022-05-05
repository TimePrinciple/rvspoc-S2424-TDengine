from util.log import *
from util.sql import *
from util.cases import *

class TDTestCase:
    def init(self, conn, logSql):
        tdLog.debug("start to execute %s" % __file__)
        tdSql.init(conn.cursor())

        self.rowNum = 10
        self.ts = 1537146000000

    def run(self):
        tdSql.prepare()

        tdSql.execute('''create table stb(ts timestamp, col1 tinyint, col2 smallint, col3 int, col4 bigint, col5 float, col6 double, 
                    col7 bool, col8 binary(20), col9 nchar(20), col11 tinyint unsigned, col12 smallint unsigned, col13 int unsigned, col14 bigint unsigned) tags(loc nchar(20))''')
        tdSql.execute("create table stb_1 using stb tags('beijing')")

        tdSql.execute('''create table ntb(ts timestamp, col1 tinyint, col2 smallint, col3 int, col4 bigint, col5 float, col6 double, 
                    col7 bool, col8 binary(20), col9 nchar(20), col11 tinyint unsigned, col12 smallint unsigned, col13 int unsigned, col14 bigint unsigned)''')
        
        for i in range(self.rowNum):
            tdSql.execute("insert into stb_1 values(%d, %d, %d, %d, %d, %f, %f, %d, 'taosdata%d', '涛思数据%d', %d, %d, %d, %d)" 
                        % (self.ts + i, i + 1, i + 1, i + 1, i + 1, i + 0.1, i + 0.1, i % 2, i + 1, i + 1, i + 1, i + 1, i + 1, i + 1))
        
        for i in range(self.rowNum):
            tdSql.execute("insert into ntb values(%d, %d, %d, %d, %d, %f, %f, %d, 'taosdata%d', '涛思数据%d', %d, %d, %d, %d)" 
                        % (self.ts + i, i + 1, i + 1, i + 1, i + 1, i + 0.1, i + 0.1, i % 2, i + 1, i + 1, i + 1, i + 1, i + 1, i + 1))
        
        tdSql.query("select count(*) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(*) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(ts) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(ts) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col2) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col2) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col3) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col3) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col4) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col4) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col5) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col5) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col6) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col6) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col7) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col7) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col8) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col8) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col9) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col9) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col11) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col11) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col12) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col12) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col13) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col13) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col14) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col14) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(ts) from db.stb_1")
        tdSql.checkData(0,0,10)        
        tdSql.query("select count(ts) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col2) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col2) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col3) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col3) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col4) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col4) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col5) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col5) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col6) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col6) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col7) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col7) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col8) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col8) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col9) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col9) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col11) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col11) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col12) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col12) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col13) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col13) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col14) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col14) from db.stb_1")
        tdSql.checkData(0,0,10)

        tdSql.execute("insert into stb_1 values(now,null,null,null,null,null,null,null,null,null,null,null,null,null)")
        tdSql.query("select count(col1) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1),count(ts) from stb_1")
        tdSql.checkData(0,0,10)
        tdSql.checkData(0,1,11)

        tdSql.query("select count(col1) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1),count(ts) from db.stb_1")
        tdSql.checkData(0,0,10)
        tdSql.checkData(0,1,11)

        tdSql.query("select count(col1) from stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1),count(ts) from stb")
        tdSql.checkData(0,0,10)
        tdSql.checkData(0,1,11)
        
        tdSql.query("select count(col1) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.query("select count(col1),count(ts) from db.stb")
        tdSql.checkData(0,0,10)
        tdSql.checkData(0,1,11)

        


    def stop(self):
        tdSql.close()
        tdLog.success("%s successfully executed" % __file__)


tdCases.addWindows(__file__, TDTestCase())
tdCases.addLinux(__file__, TDTestCase())