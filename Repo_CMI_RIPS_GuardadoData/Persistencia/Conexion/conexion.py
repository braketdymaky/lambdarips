import pymysql
import sys
import os


class BaseDatos:
    __REGION = os.environ['region']
    __rds_host = os.environ['host']
    __user = os.environ['user']
    __password = os.environ['password']
    __db_name = os.environ['db_name']

    connection = pymysql.connect(__rds_host, user=__user, passwd=__password, db=__db_name, connect_timeout=15)
