class agent:
    def __init__(self):
        self.goal='drop parcel at red house'
    def formulate_goal(self,percept):
        if percept=='Red House':
            self.goal='drop parcel at red house'
        else:
           self.goal='no action needed'
    def act(self,percept):
        self.formulate_goal(percept)
        if self.goal=='drop parcel at red house':
            return 'goal complete, terminate'
        else:
            return 'goal not reached, continue'
class environment:
    def __init__(self):
        pass
    def get_percept(self, house):
        return house
def run_agent(env, ag, path):
    for house in path:
        percept=env.get_percept(house)
        action=ag.act(percept)
        print(f'percept: {percept} action: {action}')
        if action=='goal complete, terminate':
            break
env=environment()
ag=agent()
run_agent(env,ag,['Blue House','Green House','Red House','Yellow House','White House'])