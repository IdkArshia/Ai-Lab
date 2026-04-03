class agent:
    def __init__(self,utility={'A':{'value':5,'cost':2},'B':{'value':9,'cost':8},'C':{'value':6,'cost':3}}):
        self.utility=utility
    def calculate_utility(self,rock):
        return (self.utility[rock]['value'] *2)-self.utility[rock]['cost']
    def act(self, percept):
        best_ut=0
        best_rock=None
        for rock,data in percept:
            if self.calculate_utility(rock)>best_ut:
                best_rock=rock
                best_ut=self.calculate_utility(rock)
        return best_rock
class environment:
    def __init__(self,rocks):
        self.rocks=rocks
    def get_percept(self):
        return list(self.rocks.items())
def run_agent(env,ag):
    percept=env.get_percept()
    action=ag.act(percept)
    print(f"best rock: {action}")
env=environment({'A':{'value':5,'cost':2},'B':{'value':9,'cost':8},'C':{'value':6,'cost':3}})
ag=agent()
run_agent(env,ag)
