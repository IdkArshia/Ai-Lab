class environment:
    def __init__(self,key="no"):
        self.key=key
    def get_percept(self,room):
        return {'key':self.key,'room':room}
    def update_key(self):
        self.key='yes'
class agent:
    def __init__(self):
        pass
    def act(self,percept):
        if percept['key']=='no' and percept['room']=='D':
            return "can't enter room D, key not available"
        elif percept['room']=='B':
            return "entering room "+percept['room'] +" key aquired"
        else:
            return "entering room "+percept['room']
def run_agent(env, ag, path):
    for room in path:
        percept=env.get_percept(room)
        action=ag.act(percept)
        if percept['room']=='B':
            env.update_key()
        print(action)
env=environment()
ag=agent()
run_agent(env,ag,['A','C','D','B','D'])
        
