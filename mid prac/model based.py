class environment:
    def __init__ (self, state='Dirty'):
        self.state=state
    def get_percept(self):
        return self.state
    def clean_room(self):
        self.state='Clean'

class ModelBasedAgent:
    def __init__(self):
        self.model={}
    def update_model(self, percept):
        self.model['current']=percept
        print(self.model)
    def predict_act(self):
        if self.model['current']=='Dirty':
            return "Clean the room"
        else:
            return "room is already clean"
    def act(self,percept):
        self.update_model(percept)
        return self.predict_act()

def run_agent(env, ag, steps):
    for step in range(steps):
        percept=env.get_percept()
        action=ag.act(percept)
        print(f"Step {step+1}: percept: {percept} action: {action}")

agent=ModelBasedAgent()
env=environment()
run_agent(env,agent,5)


    