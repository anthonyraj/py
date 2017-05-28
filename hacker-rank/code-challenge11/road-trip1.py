# road-trip-1
#https://www.hackerrank.com/contests/world-codes#print-11/challenges/road-trip-1

class RoadTrip():
    n=0
    q=0
    w=[]
    gas_avail=[]
    queries=[]
    total_spend=0
    f = lambda x: int(x)
    
    def __init__(self):
        self.read_cities_queries()
        self.read_distance()
        self.read_gas()
        self.read_queries()
        
    def read_cities_queries(self):
        n,q = input().strip().split(' ') # no of cities & queries
        self.n,self.q = [int(n),int(q)]

    def read_distance(self):
        w = input().strip().split(' ')
        f = lambda x: int(x)# need to keep it common
        self.w = [f(x) for x in w]
        #print ("w=",self.w)

    def read_gas(self):
        f = lambda x: int(x)
        for item in range(self.n):
            gas=input().strip().split(' ')
            gas=[f(x) for x in gas]
            self.gas_avail.append(gas)
        #print ("gas_avail=",self.gas_avail)

    def read_queries(self):
        f = lambda x: int(x)
        for item in range(self.q):
            q=input().strip().split(' ')
            q=[f(x) for x in q]
            self.queries.append(q)
        #print ("queries=",self.queries)

    def process_queries(self):
        for q in self.queries:
            start = q[0]
            end = q[1]
            #print ("start=",start,"end=",end)
            #print ("-----------------------")
            self.calc_gas(start,end)

    def calc_gas(self,start,end):
        current_gas = 0
        current_spend = 0
        total_spend = 0

        for current in range(start,end+1):
            current_spend=0
            #print ("city=",current)
            
            if start < current < end: #not the first node
                litres_spent=self.get_litres_spent(current-1) #litres/km spent to current
                #print("litres_spent=",litres_spent)
                current_gas -= litres_spent
                #print ("current_gas=",current_gas)


            if (current<end):
                free_gas = self.get_free_gas(current)
                #print ("free_gas=",free_gas)
                current_gas += free_gas
                #print ("current_gas=",current_gas)
                gas_price = self.get_gas_price(current)
                #print("gas_price=",gas_price) 
                dist = self.get_litres_spent(current)
                #print("dist",dist)
                diff = self.get_spend_factor(current_gas,dist)
                #print("diff",diff)
                    
                # predit the future gas needs here
                if diff<0:
                    current_spend = gas_price * abs(diff)
                    current_gas += abs(diff)
                elif diff>0: 
                    #print("current=",current)
                    price,diff = self.get_optimal_gas(current)
                    if price != -1:
                        current_spend = price * abs(diff)
                        current_gas += abs(diff)
                #print ("current_spend=",current_spend)
                #print ("current_gas=",current_gas)
                total_spend += current_spend 
            #print ("total_spend=",total_spend)
            #print ("-")
        print (total_spend)
        
    #getters
    def get_optimal_gas(self,current):
        dist = 0
        free = 0
        start=current
        end=current+1
        
        gas1 = self.get_gas_price(start)
        gas2 = self.get_gas_price(end)
        #print ("gas1=",gas1,"gas2=",gas2)
        if gas1<gas2: 
            for city in range(start,end+1):
                free += self.get_free_gas(city)
                dist += self.get_litres_spent(city)
            diff = free - dist
            if diff < 0:
                #print (gas1,diff)
                return gas1,diff
        else: return -1,-1

            
    def get_free_gas(self,city):
        return self.gas_avail[city-1][0]

    def get_gas_price(self,city):
        return self.gas_avail[city-1][1]

    def get_litres_spent(self,start): # 1km travelled = 1litre spent
        return self.w[start-1]

    def get_spend_factor(self,current_gas,dist):
        return current_gas-dist

    def mock_output(self): # mock output
        output = [6,3,2,16]
        for q in output:
            print(q)
    
    def run(self,t='mock'):
        if t == 'mock':
            self.mock_output()
        else:
            self.process_queries()
            
        
r = RoadTrip()
r.run('prod')


