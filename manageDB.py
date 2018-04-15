import psycopg2
import configParser

print("Connecting to the database ....", end ='\t')

#get the database parameters from config file
db_params = configParser.getDBConf('dispatcher.conf', 'DBServer')
try:
    connector = psycopg2.connect(host=db_params[0],database=db_params[1], user=db_params[2], password=db_params[3])
    print(".... OK")
except:
        print(".... FAIL")
        exit()

#function that executes an SQL querry on Database and returns results
def executeQRY(querry):
    #connect to the database
    cur = connector.cursor()

    #execute the querry
    cur.execute(querry)
    return(cur.fetchall())

    #clsoing connection with DB
    cur.close()
    connector.close()

