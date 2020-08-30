
class Node:
    def __init__(self, state=None ):
        self.state = state
        self.idx = 0
        self.parent  = None
        self.children = []


    def copy_puzzle(self, copyTo, copyFrom):
        copyTo = [0] * len(copyFrom)
        # copyTo = np.zeros(len(copyFrom))
        for i in range(0, len(copyFrom)):
          copyTo[i] = copyFrom[i]
        return copyTo



    def no_space(self,str):
        return str.replace(" ", "")



    def IsSame(self, lst, child):
        if len(lst) != 0:
            for l in range(0,len(lst)):
                if lst[l].same2(child) == True:
                    return True
                else:
                    return False

        return False

    def same2(self, other):
        possibility = []
        possibility = self.copy_puzzle(possibility,other.state)
        samePuzzle = True;
        for i in range(0, len(self.state)):
            if self.state[i] != possibility[i]:
                return False

        return samePuzzle


    def MoveUp(self, idx):
        possibility = []
        if idx - 3 >= 0:
            possibility = self.copy_puzzle(possibility, self.state)
            temp = possibility[idx - 3]
            possibility[idx - 3] = possibility[idx]
            possibility[idx] = temp

            Up_Child = Node(possibility)

            self.children.append(Up_Child)

            Up_Child.parent = self



    def MoveDown(self, idx):
        possibility = []
        if idx +3 < len(self.state):
            possibility = self.copy_puzzle(possibility, self.state)
            temp = possibility[idx + 3]
            possibility[idx + 3] = possibility[idx]
            possibility[idx] = temp

            Down_Child = Node(possibility)

            self.children.append(Down_Child)

            Down_Child.parent = self



    def MoveRight(self, idx):
        possibility = []
        if idx % 3 < 2:
            possibility = self.copy_puzzle(possibility, self.state)
            temp = possibility[idx + 1]
            possibility[idx+1] = possibility[idx]
            possibility[idx] = temp

            Right_Child = Node(possibility)

            self.children.append(Right_Child)

            Right_Child.parent = self




    def MoveLeft(self, idx):
        possibility = []
        if idx% 3 > 0:
            possibility = self.copy_puzzle( possibility, self.state)
            temp = possibility[idx - 1]
            possibility[idx-1] = possibility[idx]
            possibility[idx] = temp

            Left_Child = Node(possibility)

            self.children.append(Left_Child)

            Left_Child.parent = self





    def Diff_Moves(self):
        for i in range(0, len(self.state)):
            if self.state[i] == 0:
                x = i

        self.MoveRight(x)
        self.MoveLeft(x)
        self.MoveUp(x)

        self.MoveDown(x)




    def set_puzzle(self):
        puzzle_input = []
        x = input("Enter the first 3 digits (Must be between 0 and 8 inclusive): ")
        y = input("Enter the next 3 digits (Must be between 0 and 8 inclusive): ")
        z = input("Enter the last 3 digits (Must be between 0 and 8 inclusive): ")

        x = self.no_space(x)
        y = self.no_space(y)
        z = self.no_space(z)

        for i in x:
            puzzle_input.append(int(i))
        for i in y:
            puzzle_input.append(int(i))
        for i in z:
            puzzle_input.append(int(i))

        for num in puzzle_input:
            if puzzle_input.count(num) > 1:
                print("IMPOSSIBLE")
            else:
                self.state = puzzle_input




    def Goal_reach(self):
        goal = [1,2,3,4,5,6,7,8,0]
        isGoal = True
        for i in range(0,len(self.state)):
            if self.state[i] == goal[i]:
                isGoal = True
            else:
                return False

        return isGoal


def bfs(root):
    path = [root]
    bfs_queue = [root]
    sames_lst = []
    pop_list = []
    final_list = []
    counter = 0
    lvlcount = 0
    while len(bfs_queue) != 0:
        current_node = bfs_queue[0]
        if current_node.Goal_reach():
            return counter
        lvlcount +=1
        current_node.Diff_Moves()
        # print(bfs_queue)

        for i in range(0, len(current_node.children)):
            if current_node.children[i].Goal_reach():
                path.append(current_node.children[i])
                child = path.pop()
                while child.parent:
                    parent = child.parent
                    child = parent
                    counter += 1
                return counter


        for j in range(0, len(bfs_queue)):
            for k in range(0, len(current_node.children)):
                if bfs_queue[j].same2(current_node.children[k]):
                    sames_lst.append(current_node.children[k])


        dif_children = [item for item in current_node.children if item not in sames_lst]
        bfs_queue += dif_children
        del sames_lst[:]
        pop_list.append(bfs_queue.pop(0))
        for i in range(0,len(pop_list)):
            for j in range(0,len(dif_children)):
                if pop_list[i].same2(dif_children[j]):
                    final_list.append(dif_children[j])

        finchild = [item for item in dif_children if item not in final_list]
        bfs_queue += finchild

        # if lvlcount > 31:
        #     return "IMPOSSIBLE"

        # print(lvlcount)




nn = Node()
nn.set_puzzle()
print(bfs(nn))

