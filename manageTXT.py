import re

def extractServers (s):
    lst = re.findall('\SERV\d\d\d+',s)
    return(lst)