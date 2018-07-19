totalElements = input()

if ( 0 < totalElements < 20):
	data = set(map(int,raw_input().split()))
	if len(data) == totalElements:
			cmdNumber = input()
			if ( 0 < cmdNumber < 20):
				count = 0
				while(count < cmdNumber):
					cmd = raw_input().split()
					#print cmd
					actualCommand = cmd[0]
					if (len(cmd)>1):
						elementToRemove = int(cmd[1])
					count += 1
					if (len(data)):
						if (actualCommand == 'pop'):
							data.pop()		
						elif (actualCommand == 'remove'):
							if data.__contains__(elementToRemove):
								data.remove(elementToRemove)
						elif (actualCommand == 'discard'):
							if data.__contains__(elementToRemove):
								data.discard(elementToRemove)

finalResult = 0
for item in data:
	finalResult += item

print finalResult
