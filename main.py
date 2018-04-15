import psycopg2

import configParser
import manageDB
import manageFTP
import manageTXT
def main():
    print ("\n*** I am the main function ***\n")

    #getting the ongoing changes by executing a querry from DB
    #print(manageDB.executeQRY("""SELECT * from change where team_comp_task=false"""))
    rows = manageDB.executeQRY("""SELECT * from change where team_comp_task=false""")

    #extract from build changes servers lists, and put it inside a list with list[0] contains change number
    #manageText.extractServers(rows[0][2])
        #print (rows[0][2])



    for i in range(0, (len(rows))):
        list = [rows[i][0]]
        list.append(manageTXT.extractServers(rows[i][2]))
        #download files from FTP server and organize them into folders with change name
        #manageFTP.downloadServers(list)
        print(list)


if __name__ == "__main__":
    print("Welcome to the automatic Change Dispatcher")
    main()