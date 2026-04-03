import random
class environment:
    def __init__ (self):
        self.grid= ['Clean','Dirty','Clean','Clean','Dirty','Dirty','Clean','Clean','Clean']
    def get_percept(self,position):
        return self.grid[position]
    def clean_room(self,position):
        self.grid[position]='Clean'
    def display_grid(self, position):
        for pos in range(9):
            if pos != position:
                 print(self.grid[pos])
            else:
                print(" ")
class SimpleReflexAgent:
    def __init__ (self,position=0):
        self.position=position
    def act(self,percept,grid):
        if percept == 'Dirty':
            grid [self.position]='Clean'
            return "Clean the room"
        else:
            return "Room is already clean "
    def move(self):
        if self.position < 8:
            self.position=self.position+1
        return self.position


        
def run_agent(agent, env, steps):
    for step in range(steps):
        percept= env.get_percept(agent.position)
        action= agent.act(percept,env.grid)
        print("step: ",step+1," prcept: ",percept," Action: ",action)
        env.display_grid(agent.position)
        agent.move()
agent= SimpleReflexAgent()
env=environment()
run_agent(agent,env,9)
