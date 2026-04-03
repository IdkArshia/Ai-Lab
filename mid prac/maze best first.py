from queue import PriorityQueue
class node:
    def __init__ (self, position, parent=None):
        self.position=position
        self.parent=parent
        self.g=0
        self.h=0
        self.f=0

    def __lt__ (self,other):
        return self.f<other.f
    
def Mand(current_pos,end_pos):
    return abs(current_pos[0]-end_pos[0])+ abs(current_pos[1]-end_pos[1])

def best_first(maze,start,end):
    rows=len(maze)
    cols=len(maze[0])
    start_node=node(start)
    end_node=node(end)
    frontier=PriorityQueue()
    frontier.put(start_node)

    while not frontier.empty():
        current_node=frontier.get()
        current_pos=current_node.position

        if current_pos==end:
            path=[]
            while current_node:
                path.append(current_node.position)
                current_node=current_node.parent
            return path[::-1]
        for dx,dy in[(0,-1),(0,1),(1,0),(-1,0)]:
            new_pos=(current_pos[0]+dx,current_pos[1]+dy)
            
