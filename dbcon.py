#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


class dbconn():

    def __init__(self):
        # 打开数据库连接
        m = {}
        f = open("config.property","r")
        for line in f.readlines():
            str = line.replace('\n', '').split(":")
            m[str[0]] = str[1]
        db = pymysql.connect(m.get("host"),m.get("user"),m.get("password"),m.get("dbname"))
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询

    @staticmethod
    def getsql(dbname,tablename):
        sql = "select column_name, data_type from information_schema.columns where table_schema ='" + dbname + "' and table_name = '" + tablename + "';"
        return sql


    def execute(self,sql):
        cu = self.cursor
        cu.execute(sql)
        # 获取所有记录列表
        results = cu.fetchall()
        return results


    def close(self):
        self.cursor.close()
