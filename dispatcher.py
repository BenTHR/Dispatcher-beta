import ftplib  # import FTP manipulation library
import configparser
import psycopg2
#import pgdp

a = ['server10.sss', 'server11.sss', 'server12.sss']

# Loading the configuration file
config = configparser.ConfigParser()
config.read("dispecnik.conf")

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
if ('FTPServer' in config):
    db_name = config['DBServer']['db_name']
    db_user = config['DBServer']['db_user']
    db_host = config['DBServer']['db_host']
    db_pwd = config['DBServer']['db_pwd']
    print("Database connection parameters extracted ... OK")
else:
    print('please set up the Database location in the configuration file ... FAIL')

try:
    conn = psycopg2.connect(host=db_user, database=db_name, user=db_user, password=db_pwd)
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+db_name+";")
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
