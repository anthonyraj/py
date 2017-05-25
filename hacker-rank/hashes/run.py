def  StairCase(n):
    for i in range(n):        
        flag = False
        #output = str(i)
        output = ''
        for j in range(n):
            if (j+1 == n-i): 
                flag = True
            if (flag):
                output += '#'
            else:
                output += ' '
        print output

StairCase(6)

