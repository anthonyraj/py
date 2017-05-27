import sys, os.path

def valid_file(filename):
    f1 = filename
    i=1
    while (os.path.isfile(f1)):
        f1 = filename+'('+str(i)+')'
        i += 1
    return f1

def crt_file(filename):
    f1 = valid_file(filename)    
    f = open(f1,'w')
    f.close()
    return f1
        
def del_file(filename):
    if (os.path.isfile(filename)):
        os.remove(filename) 
                    
def rnm_file(f1,f2):
    new_file = f2
    flag = False
    if (os.path.isfile(f1)):
        del_file(f1)
        if(os.path.isfile(f2)):
            f2 = valid_file(f2)
        f2_final = crt_file(f2)
        if(f2_final == f2):
            print ('r '+f1+' -> '+f2)
    
        
def process_command(cmd):
    cmds = cmd.split(' ')
    if cmds[0] == 'crt':
        f1 = crt_file(cmds[1])
        print ('+ '+f1)
        
    if cmds[0] == 'del':
        del_file(cmds[1])
        print ('- '+cmds[1])
        
    if cmds[0] == 'rnm':
        rnm_file(cmds[1],cmds[2])
         
commands = []

#q = int(input().strip())
# Process each command

#for a0 in range(q):
    # Read the first string denoting the command type
#    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command

    #commands.append(command)

commands=['crt phonebook'
,'crt phonebook'
,'crt phonebook'
,'crt todo'
,'crt phonebook'
,'del phonebook'
,'del phonebook(2)'
,'crt phonebook'
,'crt phonebook'
,'crt phonebook'
,'rnm phonebook(2) todo'
#,'crt tony'
#,'rnm tony jenny'
#,'crt jenny'          
          ]

commands1=['rnm phonebook todo'
          ,'rnm phonebook todo'
          ,'rnm phonebook todo'
          ]

for command in commands:
    process_command(command)
