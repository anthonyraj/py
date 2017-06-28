
import re

log = 'Sat Sep 12 09:21:08 2015 -0700 I hosta.purestorage.com sha:d92dc test:6 START "test started" | Sat Sep 12 09:21:08 2015 -0700 W hosta.purestorage.com sha:d92dc test:6 FAIL "error message" | Sat Sep 12 09:21:08 2015 -0700 I hosta.purestorage.com sha:d92dc test:7 PASS "success" | Sat Sep 12 09:21:08 2015 -0700 E hosta.purestorage.com sha:d92dc test:8 ERROR "library libXpm.so not found" SEVERITY10 | Sat Sep 12 09:21:08 2015 -0700 E hostb.purestorage.com sha:d92dc test:9 ERROR "SEVERITY100"'

# original answer. It does not print correct value until converted into tuples
def find_host1(log):
    host_data = {}
    data = log.strip().split('|')
    for item in data:
        if item.strip() != '':
            line = item.split(' ')
            for element in line:
                if element.endswith('purestorage.com'):
                    host = element.split('.')
                    if host[0] in host_data: host_data[host[0]] +=1
                    else : host_data[host[0]] = 1
    return max(host_data,key=lambda x:x[1])

def find_host2(logfile):
    f = open(logfile)
    host_data = {}
    for data in f:       
        if data.strip() != '':
            line = data.split(' ')
            for element in line:
                if re.search('purestorage.com$', element):
                    host = element.split('.')
                    if host[0] in host_data: host_data[host[0]] +=1
                    else : host_data[host[0]] = 1
    f.close()
    print(host_data)
    l = [(k,v) for k,v in host_data.items()]
    return max(l,key=lambda x:x[1])

def find_host3(logfile):
    f = open(logfile)
    pattern = 'purestorage.com$'
    host_data = {}
    for data in f:    
        if data.strip() != '': #re.search(pattern, data):
            line = data.split(' ')
            for element in line:
                if re.search(pattern, element):
                    host = element.split('.')
                    if host[0] in host_data: host_data[host[0]] +=1
                    else : host_data[host[0]] = 1
    f.close()
    print(host_data)
    if len(host_data):
        return max(host_data, key=(lambda key: host_data[key]))
    else : return 0

def find_host4(logfile):
    f = open(logfile)
    pattern = '\w+.purestorage.com'
    host_data = {}
    for data in f:    
        if data.strip() != '':
            match = re.search(pattern, data)
            if match:
                element = match.group()
                print(element)
                host = element.split('.')
                if host[0] in host_data: host_data[host[0]] +=1
                else : host_data[host[0]] = 1
    f.close()
    print(host_data)
    if len(host_data):
        return max(host_data, key=(lambda key: host_data[key]))
    else : return 0

    
#m = find_host1(log)
#print("max occurrance of host",m)    
#m = find_host2('tomcat.log')
#print("max occurrance of host",m)
#m = find_host3('tomcat.log')
#print("max occurrance of host",m)
m = find_host4('tomcat.log')
print("max occurrance of host",m)
