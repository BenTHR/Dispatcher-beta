import configparser


###getting Database connection parameters using the getDBConf function###
# We this function using two parametrs: 0.configuration file path, 1. Section name of the config file
# and it will return a list of parameters ordered as follow
# 0.Host name:port		1.Data Base name	     2.User name	3.Password
def getDBConf (filename, section):
    # connect to the DB server
    print("Gathering database configuration ....", end='\t')

    config = configparser.ConfigParser()
    config.read(filename)

    try:
        if (section in config):
            db_host = config[section]['db_host']
            db_name = config[section]['db_name']
            db_user = config[section]['db_user']
            db_pwd = config[section]['db_pwd']
        else:
            print(".... not such section in config file ... FAIL")
            exit(1)

        print(" .... OK")
    except:
        print("gathering database configuration .... FAIL")

    a=[db_host,db_name,db_user,db_pwd]
    return a

def getFTPConf (filename, section):
    # connect to the FTP server
    print("Gathering FTP configuration ....", end='\t')

    config = configparser.ConfigParser()
    config.read(filename)

    try:
        if (section in config):
            db_host = config[section]['db_host']
            db_name = config[section]['db_name']
            db_user = config[section]['db_user']
            db_pwd = config[section]['db_pwd']
        else:
            print(".... not such section in config file ... FAIL")
            exit(1)

        print(" .... OK")
    except:
        print("gathering database configuration .... FAIL")

    a=[db_host,db_name,db_user,db_pwd]
    return a