
import happybase

conn = happybase.Connection("node2.leap.com", 9090)
stu_table = conn.table("test:student")
stu_table.put("000001234", {"c1:name": "sfsf"})
batch = stu_table.batch()
batch.put()
for row in stu_table.scan():
    print("row: ", row)