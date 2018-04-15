import ftplib  # import FTP manipulation library
import configparser
import psycopg2
#import pgdp

a = ['server10.sss', 'server11.sss', 'server12.sss']

# Loading the configuration file
config = configparser.ConfigParser()
config.read("dispatcher.conf")

# Gathering FTP connection settings fron the config file  FTPServer' in config:
if ('FTPServer' in config):
    ftp_host = config['FTPServer']['ftp_host']
    ftp_user = config['FTPServer']['ftp_user']
    ftp_password = config['FTPServer']['ftp_password']
    ftp_path = config['FTPServer']['ftp_path']
    print("FTP connection parameters extracted ... OK")
else:
    print('please set up the FTP location in the configuration file ... FAIL')

#### Gathering INPROG changes information ###

# connect to database#
if ('DBPServer' in config):
    db_name = 'change_db' #config['DBServer']['db_name']
    db_user = 'postgres'#config['DBServer']['db_user']
    db_host = 'localhost:5432'#config['DBServer']['db_host']
    db_pwd = 'password'#config['DBServer']['db_pwd']
    print("Database connection parameters extracted ... OK")
else:
    print('please set up the Database location in the configuration file ... FAIL')

try:
    conn = psycopg2.connect(host='localhost:5432', database='change_db', user='postgres', password='password')
    cur = conn.cursor()
    #cur.execute("SELECT * FROM "+db_name+";")
    print("connection to ticketing system database .... OK")

except:
    print("connection to ticketing system database .... FAIL")

# Download the requested files
def download_Files_FTP(ip, user, pwd, path, list):
    ftp = ftplib.FTP(ip)
    ftp.login(user, pwd)
    ftp.cwd(path)
    for i in range(0, len(list)):
        ftp.retrbinary("RETR" + list[i], open(list[i], 'wb').write)
    ftp.quit()
