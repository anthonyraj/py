# Interview Question with Gerald Huff at Tesla
# Manufacturing Operating System (MOS)

class MOS(object):
    process_map = {} #{p0:'process_object'}
    subprocess_map = {} #{s0:'process_name'}
    flowstep_map = {} #{f0:'subprocess_name'}

    def __init__(self):
        print("Creating the MOS Class object")

    def scrub(self,name):
        return name.lower().strip()

    def scrub_list(self,item_list):
        scrubbed_list = [self.scrub(item) for item in item_list]
        return scrubbed_list
    
    def create_process(self,name):
        print("create_process(",name,")")
        if name != '':
            name = self.scrub(name)
            if name not in self.process_map:
                self.process_map[name] = Process(name)
                return 'success creating process '+name
            else: 
                return 'failure process '+name+' exists'
        else:
            return 'failure creating null process name'

    def create_flow_for_process(self,process_name, subprocess_name):
        print("create_flow_for_process(",process_name,",",subprocess_name,")")
        if subprocess_name != '' and process_name !='':
            process_name,subprocess_name = self.scrub_list([process_name,subprocess_name])
            if subprocess_name not in self.subprocess_map:
                self.subprocess_map[subprocess_name] = process_name
                self.process_map[process_name].set_subprocess(subprocess_name)
                return 'success creating flow '+subprocess_name
            else:
                mappedto_process = self.subprocess_map[subprocess_name]
                return 'failure creating flow '+subprocess_name+'. The flow has been mapped to '+mappedto_process
        else:
            return 'failure creating null flow name'
        
    def promote_flow(self,process_name, subprocess_name):
        method = "promote_flow"
        params = "(",process_name,",",subprocess_name,")"
        action = method,params
        print(action)
        if subprocess_name != '' and process_name !='':
            process_name,subprocess_name = self.scrub_list([process_name,subprocess_name])
            if subprocess_name in self.subprocess_map:
                process_name = self.scrub(process_name)
                sp = self.process_map[self.subprocess_map[subprocess_name]].get_subprocess(subprocess_name)
                sp.promote_subprocess_state()
                return 'success promoting flow '+subprocess_name
            else:
                return 'failure ',method,'subprocess_name=',subprocess_name,' does not exist'
        else:
            return 'failure ',method,' contains invalid params (eg.null) ',param

    def delete_flow(self,subprocess_name):
        print("delete_flow(",subprocess_name,")")
        if subprocess_name != '':
            subprocess_name = self.scrub(subprocess_name)
            if subprocess_name in self.subprocess_map:
                p = self.process_map[self.subprocess_map[subprocess_name]]
                p.delete_subprocess(subprocess_name)
                #print("remaining subprocess = ",p.subprocess_map)
                self.subprocess_map.__delitem__(subprocess_name)
                return 'success deleting flow '+subprocess_name
            else :
                return 'failure deleting flow '+subprocess_name
        else:
            return 'failure creating null flow name'       
    def create_flow_step_for_flow(self,subprocess_name,flowstep_name):
        print("create_flow_step_for_flow(",subprocess_name,",",flowstep_name,")")
        if subprocess_name != '' and flowstep_name !='':
            subprocess_name,flowstep_name = self.scrub_list([subprocess_name,flowstep_name])
            if subprocess_name in self.subprocess_map:
                self.flowstep_map[flowstep_name] = subprocess_name
                sp = self.process_map[self.subprocess_map[subprocess_name]].get_subprocess(subprocess_name)
                sp.set_flowstep(flowstep_name)
                return 'success creating flowstep:'+flowstep_name+' for flow:'+subprocess_name
            else:
                return 'failure creating flowstep:'+flowstep_name+' has mapping to flow:'+self.flowstep_map[flowstep_name]
        else :
            return 'failure creating null flowstep name'

    def delete_flow_step_for_flow(self,subprocess_name,flowstep_name):
        print("delete_flow_step_for_flow(",subprocess_name,",",flowstep_name,")")
        if subprocess_name != '' and flowstep_name !='':
            subprocess_name,flowstep_name = self.scrub_list([subprocess_name,flowstep_name])
            if subprocess_name in self.subprocess_map:
                sp = self.process_map[self.subprocess_map[subprocess_name]].get_subprocess(subprocess_name)
                sp.delete_flowstep(flowstep_name)
                self.flowstep_map.__delitem__(flowstep_name)
                return 'success deleting flowstep:'+flowstep_name+' for flow:'+subprocess_name
            else:
                return 'failure creating flowstep:'+flowstep_name+' has mapping to flow:'+self.flowstep_map[flowstep_name]
        else :
            return 'failure deleting null flowstep name'

    def get_process_info(self,process_name):
        print("get_process_info(",process_name,")")
        process_info = {}
        #print(self.process_map)
        if process_name in self.process_map:
            print('found '+process_name)
            p = self.process_map[process_name]
            for sp_name,sp in p.get_subprocess().items():
                print("found "+sp_name)
                #process_info[sp_name] = [fs for fs in sp.get_flowstep()]
                process_info[sp_name] = sp.get_flowstep_order()
        print("process_info=",process_info)
        return process_info

    def get_flow_info(self,subprocess_name):
        print("get_flow_info(",subprocess_name,")")
        flowsteps = []
        #print("self.subprocess_map=",self.subprocess_map)
        if subprocess_name in self.subprocess_map:
            print("found ",subprocess_name)
            sp = self.process_map[self.subprocess_map[subprocess_name]].get_subprocess(subprocess_name)
            #flowsteps = [fs for fs in sp.get_flowstep()]
            flowsteps = sp.get_flowstep_order()
        print("flowsteps=",flowsteps)
        return flowsteps

    def update_flow(self,subprocess_name, flowstep_order):
        print("update_flow(",subprocess_name,",",flowstep_order,")")
        if subprocess_name != '' and len(flowstep_order) != 0:
            subprocess_name = self.scrub(subprocess_name)
            if subprocess_name in self.subprocess_map:
                self.process_map[self.subprocess_map[subprocess_name]].get_subprocess(subprocess_name).set_flowstep_order(flowstep_order)
                return 'success updating flowstep order:'+str(flowstep_order)+' for flow:'+subprocess_name
            else:
                return 'failure: non-existent flow name:'+subprocess_name
        else:
            return 'failure due to null flow name/flowstep order list'

class Process(object):
    
    def __init__(self,name):
        self.process_name = ''
        self.process_state = ''
        self.subprocess_map = {}
        self.subprocess_count = 0
        self.set_process(name)
        
    def set_process(self,name):
        self.process_name = name
        
    def get_process(self):
        return self.process_name

    def set_subprocess_count(self,value):
        self.subprocess_count = value

    def get_subprocess_count(self):
        return self.subprocess_count

    def increment_subprocess_count(self):
        value = self.get_subprocess_count()
        value +=1
        self.set_subprocess_count(value)

    def decrement_subprocess_count(self):
        value = self.get_subprocess_count()
        value -=1
        self.set_subprocess_count(value)
    
    def set_subprocess(self,name):
        if name not in self.subprocess_map:
            self.subprocess_map[name] = SubProcess(name)
            self.increment_subprocess_count()
            return 1
        else :
            return 0

    def get_subprocess(self,name=''):
        if name=='':
            return self.subprocess_map
        else :
            return self.subprocess_map[name]

    def delete_subprocess(self,name):
        if name !='':
            stateelf.subprocess_map.__delitem__(name)
            self.decrement_subprocess_count()    

class SubProcess(object):
    # does not make sense to have a flow in archive state before production. It should be in archive after production
    state_order = ['develop','archive','production']
    
    def __init__(self,name):
        self.subprocess_name = ''
        self.subprocess_state = ''
        self.flowstep_map = {}
        self.flowstep_order = []
        self.flowstep_count = 0
        self.state_id = -1
        self.set_subprocess(name)
        self.promote_subprocess_state() # initial state set to develop
        
    def set_subprocess(self,name):
        self.subprocess_name = name.lower().strip()
        
    def get_subprocess(self):
        return self.subprocess_name

    def set_subprocess_state(self,state):
        self.subprocess_state = state

    def get_subprocess_state(self):
        return self.subprocess_state

    def promote_subprocess_state(self):
        self.state_id += 1
        if self.state_id < len(self.state_order):            
            self.set_subprocess_state(self.state_order[self.state_id])
        else: self.state_id = len(self.state_order)-1

    def set_flowstep(self,name):
        self.flowstep_map[name] = FlowStep(name)
        self.push_flowstep_order(name)

    def get_flowstep(self,name=''):
        if name != '':
            return self.flowstep_map[name]
        else:
            return self.flowstep_map

    def delete_flowstep(self,name):
        if name != '':
            self.flowstep_map.__delitem__(name)
            self.delete_from_flowstep_order(name)

    def set_flowstep_order(self,order):
        self.flowstep_order = order

    def get_flowstep_order(self):
        return self.flowstep_order

    def push_flowstep_order(self,name):
        self.flowstep_order.append(name)

    def delete_from_flowstep_order(self,name):
        self.flowstep_order.remove(name)
    
class FlowStep(object):
    state_order = ['initialized','running','wait','completed','error']
    
    def __init__(self,name):
        self.flowstep_name = ''
        self.flowstep_state = ''
        self.state_id = -1
        self.set_flowstep_name(name)

    def set_flowstep_name(self,name):
        self.flowstep_name = name

    def get_flowstep_name(self):
        return self.flowstep_name

    def set_flowstep_state(self,state):
        self.flowstep_state=state

    def get_flowstep_state(self):
        return self.flowstep_state

    def promote_flowstep_state(self):
        self.state_id += 1
        if self.state_id < len(self.state_order):            
            self.set_flowstep_state(self.state_order[self.state_id])
        else: self.state_id = len(self.state_order)-1

def run():
    mos = MOS()
    mos.create_process('p1')
    mos.get_process_info('p1')
    mos.create_flow_for_process('p1','s1')
    mos.promote_flow('p1','s1')
    mos.get_flow_info('s1')
    mos.get_process_info('p1')
    mos.create_flow_for_process('p1','s2')
    mos.get_flow_info('s1')
    mos.get_process_info('p1')
    mos.delete_flow('s2')
    mos.get_flow_info('s1')
    mos.create_flow_step_for_flow('s1','f1')
    mos.create_flow_step_for_flow('s1','f2')
    mos.create_flow_step_for_flow('s1','f3')
    mos.get_flow_info('s1')
    mos.get_process_info('p1')
    mos.delete_flow_step_for_flow('s1','f3')
    mos.get_flow_info('s1')
    mos.get_process_info('p1')
    mos.update_flow('s1',['f2','f1'])
    mos.get_flow_info('s1')
    mos.get_process_info('p1')
    
#run()
