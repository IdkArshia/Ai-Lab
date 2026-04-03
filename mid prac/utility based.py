class environment:
    def __init__(self, movies):
        self.movies=movies
    def get_percept(self):
        return list(self.movies.items())
    
class UtAgent:
    def __init__(self,mood_factor=0.7):
        self.mood_factor=mood_factor
    def utility(self, review):
        return review* self.mood_factor
    def act(self, percept):
        best_mov=None
        best_ut=0
        for mov,rev in percept:
            mov_ut=self.utility(rev)
            if best_ut<mov_ut:
                best_ut=mov_ut
                best_mov=mov
        return best_mov
    
def run_agent(agent, environment):
    percept=environment.get_percept()
    action=agent.act(percept)
    print(f"available movies: {environment.movies}")
    print(f"best movie: {action}")

movies={
    "abc":3,
    "fgh":5,
    "tgh":1,
    "fghj":9
}
env=environment(movies)
agent=UtAgent()
run_agent(agent,env)