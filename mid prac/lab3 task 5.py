import random
class agent:
    def __init__(self,actions):
        self.Q={}
        self.actions=actions
        self.alpha=0.1
        self.gamma=0.9
        self.epsilon=0.2
    def get_Q(self, state,action):
        return self.Q.get((state,action),0)
    def choose_action(self,state):
        if random.uniform(0,1)<self.epsilon:
            return random.choice(self.actions)
        else:
            return max(self.actions,key=lambda a:self.get_Q(state,a))
    def learn(self, state, action, reward, next_state):
        old_Q=self.get_Q(state,action)
        future_Q=max([self.get_Q(next_state,a) for a in self.actions])
        new_Q=old_Q+ self.alpha*(reward+self.gamma*future_Q-old_Q)
        self.Q[(state,action)]=new_Q
class environment:
    def __init__(self):
        self.track = ['Start', 'Empty', 'Cheese', 'Trap']
        self.rewards = {
            'Start': 0,
            'Empty': -1,
            'Cheese': 10,
            'Trap': -10
        }
    
    def get_state(self, position):
        return self.track[position]

    def get_reward(self, state):
        return self.rewards[state]
def run_agent(env,ag,steps=5):
    current_pos=0
    for step in range(steps):
        percept=env.get_state(current_pos)
        action=ag.choose_action(percept)
        next_pos=action
        next_state=env.get_state(next_pos)
        reward=env.get_reward(next_state)
        ag.learn(percept,action,reward,next_state)
        print(f"Step {step+1}: {percept} → {next_state}, Reward: {reward}")

        current_pos = next_pos


# Run
env=environment()
ag=agent([1,2,3])
run_agent(env,ag)
