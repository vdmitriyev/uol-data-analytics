#!/usr/bin/env python3

__author__      = "Viktor Dmitriyev"
__version__     = "1.0"
__created__     = "05.04.2018"
__updated__     = "05.04.2018"
__description__ = "A simple python test utility that tests connection to the SAP HANA from Python."

"""
    Dependencies:
        - https://github.com/SAP/PyHDB
"""

"""

How to figure out the right port (SQL PORT) of a tenant (more here - https://github.com/SAPDocuments/How-Tos/issues/36):
 - SELECT SERVICE_NAME, PORT, SQL_PORT, (PORT + 2) HTTP_PORT FROM SYS.M_SERVICES WHERE ((SERVICE_NAME='indexserver' and COORDINATOR_TYPE= 'MASTER') or (SERVICE_NAME='xsengine'));

"""

import pyhdb
import argparse

def test_connection():

    import settings as settings

    connection = pyhdb.connect(
        host=settings.HOST,
        port=settings.PORT,
        user=settings.USER,
        password=settings.PASSWORD
    )


    SH_SCHEMA = settings.DB_SCHEMA
    SH_TABLE_NAME = settings.DB_TABLE_TEST
    cursor = connection.cursor()
    sql = 'SELECT * FROM "{0}"."{1}"'.format(SH_SCHEMA, SH_TABLE_NAME)
    print ('[i] execution following SQL: {0}'.format(sql))

    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    cursor.close()

def main():
    test_connection()

if __name__ == '__main__':

    # fetching input parameters
    parser = argparse.ArgumentParser(description='{0}\nVersion - {1}. Last updated - {1}\n'
                                    .format(__description__, __version__, __updated__))

    # urls-file
    # parser.add_argument(
    #     '--about',
    #     dest='about',
    #     help='input')

    # # parse input parameters
    # args = parser.parse_args()

    #main(args.user, args.password, args.server, args.port)
    main()
