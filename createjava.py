#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tools.dbcon as dbconn

class createjava:

    @staticmethod
    def createentity(results,tablename):
        str = "public class " + tablename.capitalize() + "{\n\n"
        for row in results:
            column_name = row[0]
            data_type = row[1]
            if data_type == "int":
                str += "    public int " + column_name + ";\n"
                str += "    public void set" + column_name.capitalize() + "(int " + column_name + "){\n"
                str += "        this." + column_name + " = " + column_name + ";\n"
                str += "    }\n"
                str += "    public int get" + column_name.capitalize() + "(int " + column_name + "){\n"
                str += "        return " + column_name + ";\n"
                str += "    }\n\n"
            elif data_type == "bigint":
                str += "    public java.math.BigDecimal " + column_name + ";\n"
                str += "    public void set" + column_name.capitalize() + "(java.math.BigDecimal " + column_name + "){\n"
                str += "        this." + column_name + " = " + column_name + ";\n"
                str += "    }\n"
                str += "    public java.math.BigDecimal get" + column_name.capitalize() + "(java.math.BigDecimal " + column_name + "){\n"
                str += "        return " + column_name + ";\n"
                str += "    }\n\n"
            elif data_type == "varchar" or data_type == "char" or data_type == "text" or data_type == "blob" or data_type == "longtext":
                str += "    public String " + column_name + ";\n"
                str += "    public void set" + column_name.capitalize() + "(String " + column_name + "){\n"
                str += "        this." + column_name + " = " + column_name + ";\n"
                str += "    }\n"
                str += "    public String get" + column_name.capitalize() + "(String " + column_name + "){\n"
                str += "        return " + column_name + ";\n"
                str += "    }\n\n"
            elif data_type == "datetime":
                str += "    public java.sql.Date " + column_name + ";\n"
                str += "    public void set" + column_name.capitalize() + "(java.sql.Date " + column_name + "){\n"
                str += "        this." + column_name + " = " + column_name + ";\n"
                str += "    }\n"
                str += "    public java.sql.Date get" + column_name.capitalize() + "(java.sql.Date " + column_name + "){\n"
                str += "        return " + column_name + ";\n"
                str += "    }\n\n"
        str += "}"
        filename = tablename + ".java"
        file = open(filename,"w")
        file.write(str)
        file.flush()
        file.close()

if __name__ == "__main()__":
    db = dbconn()
    sql = db.getsql("edu","admin")
    results = db.execute(sql)
    cj = createjava()
    cj.createentity(results,"admin")