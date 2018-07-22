# -*- coding: utf-8 -*-
"""
<DRIVER>
@author: SRobbins
"""

import time
import sys
import math 

class driver():
    """ <DRIVER> """
    method = str
    initialState = []
    cost = int
    config  =[]    
    solved = False
    N = 0
    
    def __init__(self,initial_state,search_method):
        self.method = search_method
        self.initialState = parseInputState(initial_state) 
        self.cost = 0
        self.N = math.sqrt(len(self.initialState))

        
        ''' Confirm initial state makes a square '''
        if(self.N%1!=0):
            print(len(self.initialState))
            raise Exception("Initial State is Invalid!")
            
        else:
            print("Initializing search method "+self.method)
        self.showAndDefineState()   
        self.run()
        
        
    def showAndDefineState(self):
        col = 1
        rows = 1
        ROW = ""
        positions = ""
        for node in self.initialState:
            ROW += str(node)+" "
            positions += "("+str(col)+","+str(rows)+")"
            self.config.append(Node(node,col,rows))
            col+=1
            if(col==self.N+1):
                rows+=1
                ROW += '\n'
                positions += '\n'
                col = 1
            
        print(ROW)
        print(positions)

    
    def run(self):
        if(self.method=="-dfs"):
            dfs = DFS(self.config)
            while(self.solved==False):
                children,configs  = dfs.dfSearchSpace()
                for child in children:
                    dfs.moveTile(child,Node(0,dfs.zerox,dfs.zeroy))
                    dfs.showConfig()
                    
                dfs.done = True
                self.solved = dfs.done
                print('Cost: '+str(dfs.cost))
                print('--------------------------------')
              
               
        if(self.method=='-bfs'):
            print('--------------------------------')
            print('Starting DFS...')
            bfs = BFS(self.config)
            children, zero = bfs.dfSearchSpace()
            branches = dfs.runBFS(children,zero)
            bs = branches.values()
            for branch in bs:
                dfsc = BFS(branch)
                fringe, zeta = dfsc.dfSearchSpace()                
                dfsc.runBFS(fringe,zeta)
  

class Node:
    children = []
    val = -1
    x =0 
    y = 0
    visited = False
    
    def __init__(self,value,xpos,ypos):
        self.val = value
        self.x = xpos
        self.y = ypos
    
    def addChild(self, childnode):
        self.children.append(childnode)
        
    def showVal(self):
        print(str(self.val))
    
    def getVal(self):
        return self.val
        
    def expandNode(self,board):
        print('Expanding '+str(self.val))
        opt = list()
        index = 0
        # Using same coordinate system as method showAndDefineState()        
        col = 1
        rows = 1
        # Define N, the dimension of square with area NxN 
        N = int(math.sqrt(len(board)))
        for nod3 in board:
            opt.append(nod3)
        for node in board:
            if node.x == (self.x-1 and self.y==node.y):
                self.addChild(node) # Left 
            if node.x<=N and node.x==self.x+1 and node.y==self.y:
                self.addChild(node) # Right 
            if(node.x==self.x and node.y==(self.y - 1)):
                self.addChild(node) #Down
            if(node.x==self.x and node.y==(self.y + 1)):
                self.addChild(node) #Up 
            index += 1
            col+=1
            if col==N:
                rows+=1
                col = 1
        chiln = ""
        for child in self.children:
            chiln += "{"+str(child.val)+' : '+"["+str(child.x)+','+str(child.y)+"] "+"} "
        print(chiln)
        return self.children



class BFS:
    done = False
    STATE = []
    def __init__(self,board):
        self.STATE = board
        self.cost = 0
        
    def BfSearchSpace(self):
        '''
        The Depth First Search begins by expanding the first frontier element, 
        and continues expanding it's children until it finds no more. From this 
        child, the search extends to the siblings at this low level. When all 
        siblings have been explored, the searh resumes this same process from the 
        next element in the frontier set. This algorithm iterates until eventually
        covering solution space. 
        '''
        col=1
        row=1
        zeta = Node(0,-1,-1)
        for e in self.STATE:
            #e.x = col
            #e.y = row
            if(int(e.val)==0):
                fnodes = e.expandNode(self.STATE)
                zeta = e
            col+=1
            if(col==int(math.sqrt(len(self.STATE)))+1):
                col=1
                row+=1
        return fnodes, zeta
        
    def runBFS(self, fnodes, zeta):    
        #Explore all children of each fnodes ones by ones 
        print('Frontiers: ')
        frontiers = {}
        index = 0
        while(len(fnodes)>0):
            self.STATE = self.swapTiles(fnodes.pop(),zeta)
            self.showConfig()
            frontiers[index] = self.STATE
            index += 1
        index = 0
        print('Expanding Frontiers')
        self.STATE = frontiers.values
        fringes = {}
        i = 0
        for frontier in frontiers:
            print('Board Configuration '+str(i)+':')
            self.STATE = frontier
            branch = self.recursiveChildPopper(frontiers[index])
            while(len(branch)>0):
                self.STATE = self.swapTiles(branch.pop(),zeta)
                self.showConfig()
                fringes[i] = self.STATE
                
                i += 1
            #self.showConfig()
            self.clearChildren()            
            index += 1
        return fringes 

    
            
    def checkSolved(self):
        solution = []
        index = 0
        for node in self.STATE:            
            if(int(node.val)==index):
                solution.append(True)
            index += 1
        if(len(solution)==len(self.STATE)):
            return True
        else:
            return False
    
    def recursiveChildPopper(self,state):
        '''
        CHILD_POPPER
        '''
        col = 1
        row = 1
        self.STATE = state
        self.showConfig()
        for n in self.STATE:        
            if(int(n.val)==0):
                children = n.expandNode(state)
                print('Node0 @ ('+str(n.x)+','+str(n.y)+')')
        print('--------------------------------')
        return children
    
    def swapTiles(self,tileA,zero):  
        newstate = []
        col = 1
        rows = 1
        index = 0
        for node in self.STATE:
            if(node.val!=tileA.val and node.val!=zero.val):
                newstate.append(node)
                node.x = col
                node.y = rows
            if(int(node.val)==0):
                newstate.append(tileA)
                node.x = tileA.x
                node.y = tileA.y
            if(node.val==tileA.val):
                newstate.append(zero)
                tileA.x = zero.x
                tileA.y = zero.y
            col+=1
            if(col==int(math.sqrt(len(self.STATE)))+1):
                col = 1
                rows+=1
            index +=1 
        return newstate
    
    def showConfig(self):
        '''
        Display the current board configuration 
        '''
        col = 1
        rows = 1
        ROW = ""
        pos = ""
        for node in self.STATE:
            ROW += str(node.val)+" "
            pos += "("+str(col)+","+str(rows)+")"
            node.x = col
            node.y = rows
            col+=1
            if(col==int(math.sqrt(len(self.STATE)))+1):
                rows+=1
                ROW+= '\t'+pos+'\n'
                pos = ""
                col = 1
            
            
        print(ROW)
        
    def clearChildren(self):
        for child in self.STATE:
            for node in child.children:
                child.children.pop()

class DFS:
    '''
    Define the set of possible solutions following a breadth first search
    algorith of exploring potential moves for the NxN Puzzle. 
       
    For a breadth first search this means expanding the tree by rows of 
    children. For example if A->(B,C) where B->(D,E) and C->(F,G), a bredth
    first search would start by checking both it's children B and C, then
    checking the children of B (D and E) and the children of C (F and G). 
    ''' 
    done = False
    items = list()
    configuration = []    
    zerox = -1
    zeroy = -1
    Q = list()
    commands = ['up','down','left','right']
    
    def __init__(self,board):
        self.cost = 0
        self.configuration = board
        
    def dfSearchSpace(self):
        '''
        Define the set of possible solutions, following a depth first search
        algorithm of exploring moves, to the solve the NxN Puzzle. 
        
        The depth first search space is defined by exploring the children of a
        decision tree recursively (in this case) until the next node has no child.
        Only then does the search move on the next option in the top fronier.
        '''   
        children = []
        configs = [] 
        col = 1
        rows = 1
        zeta = Node(0,0,0)
        for node in self.configuration:
            if(int(node.val)==0):
                self.zerox = col
                self.zeroy = rows
                zeta = Node(self.zerox,self.zeroy,node.val)
                children = node.expandNode(self.configuration) 
        while(len(children)>0):
            index = 0
            for child in children:
                self.configuration[index] =  self.moveTile(child,zeta)
                index += 1
            col +=1  
            if(col==int(math.sqrt(len(self.configuration)))):
                rows+=1
                col = 1   
                
        return children, configs 
        
  
    
    def clearChildren(self):
        for child in self.configuration:
            for node in child.children:
                child.children.pop()
            
        
            
    def runConfigs(self,states):
        for state in states:
            self = DFS(state)
            self.cost +=1 
            children, configs = self.dfSearchSpace()
            
        
    def moveTile(self,tileA,tileB):
        if tileB.visited == False:
            return self.configuration
        self.cost += 1 
        newconfig = []
        for node in self.configuration:
            if(node.val==tileB.val and node.val==tileB.val):
                newconfig.append(tileA)
                self.zerox =tileA.x
                self.zeroy = tileA.y
            elif(node.val==tileA.val):
                newconfig.append(tileB)
                self.zerox =tileA.x
                self.zeroy = tileA.y
                tileB.visited = False
            else:
                newconfig.append(node)
                
        return newconfig 
     
    def showConfig(self):
        '''
        Display the current board configuration 
        '''
        col = 1
        rows = 1
        ROW = ""
        pos = ""
        for node in self.configuration:
            ROW += str(node.val)+" "
            pos += "("+str(col)+","+str(rows)+")"
            col+=1
            if(col==int(math.sqrt(len(self.configuration)))+1):
                rows+=1
                ROW+= '\t'+pos+'\n'
                pos = ""
                col = 1
            node.x = col
            node.y = rows
            self.Q.append(node)
        print(ROW)

#######################__END_OF_CLASS_METHODS_#################################


def parseInputState(initialstate):
      state = []
      nodes = initialstate.split(",")
      for node in nodes:
          node = node.replace("[","")
          node = node.replace("]","")
          state.append(node)
      return state

#################################_MAIN_########################################
def main():
    search = sys.argv[1]
    state_init = sys.argv[2]
    d = driver(state_init,search)
    
    
if __name__ =='__main__':
    main()
