import random
class environment:
    def __init__ (self):
        self.state=random.choice(['Dirty' , 'Clean'])
    def get_percept(self):
        return self.state
    def clean_room(self):
        self.state='Clean'
    def update_state(self):
        self.state= random.choice(['Dirty', 'Clean'])
class SimpleReflexAgent:
    def __init__ (self):
        pass
    def act(self,percept):
        if percept == 'Dirty':
            return "Clean the room"
        else:
            return "Room is already clean "
        
def run_agent(agent, env, steps):
    for step in range(steps):
        env.update_state()
        percept= env.get_percept()
        action= agent.act(percept)
        print("step: ",step+1," prcept: ",percept," Action: ",action)
        if percept == 'Dirty':
            env.clean_room()
agent= SimpleReflexAgent()
env=environment()
run_agent(agent,env,5)
