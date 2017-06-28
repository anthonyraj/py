log = 'Sat Sep 12 09:21:08 2015 -0700 I hosta.purestorage.com sha:d92dc test:6 START "test started" | Sat Sep 12 09:21:08 2015 -0700 W hosta.purestorage.com sha:d92dc test:6 FAIL "error message" | Sat Sep 12 09:21:08 2015 -0700 I hosta.purestorage.com sha:d92dc test:7 PASS "success" | Sat Sep 12 09:21:08 2015 -0700 E hosta.purestorage.com sha:d92dc test:8 ERROR "library libXpm.so not found" SEVERITY10 | Sat Sep 12 09:21:08 2015 -0700 E hostb.purestorage.com sha:d92dc test:9 ERROR "SEVERITY100"'

def find_host(log):
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
    
m = find_host(log)
print("max occurrance of host",m)
