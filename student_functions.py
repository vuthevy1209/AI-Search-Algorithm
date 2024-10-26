import numpy as np
from queue import Queue, PriorityQueue
from utils import PathBuilder # Khai báo lớp PathBuilder đề thuận tiện cho việc truy vết đường đi và tính toán heuristic


def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
    visited = {} # VD: visited = {3: 1}; đỉnh 3 đã được thăm và đã được thăm từ đỉnh 1
    queue = Queue()
    queue.put(start) 
    visited[start] = None # Đánh dấu đã thăm start và nó không được thăm từ bất kỳ đỉnh nào nên ta gán None
    
    while not queue.empty():
        node = queue.get()
        if node == end : break # Lấy node đầu hàng đợi ra và nếu nó là node end thì ta dừng việc tìm kiếm
        
        # Trong TH chưa là end thì ta mở rộng các node kề với nó
        for adjacentNode, weight in enumerate(matrix[node]): 
            if weight > 0 and adjacentNode not in visited: # Nếu có cạnh nối (weight > 0) và node kề này chưa được thăm
                visited[adjacentNode] = node 
                queue.put(adjacentNode) 
                
    path = PathBuilder.getPath(visited=visited, end=end) # Truy ngược visited để lấy đường đi
        
    return visited, path
                

def DFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    visited = {} # VD: visited = {3: 1}; đỉnh 3 đã được thăm và đã được thăm từ đỉnh 1
    stack = [start] 
    visited[start] = None # Đánh dấu đã thăm start và nó không được thăm từ bất kỳ đỉnh nào nên ta gán None
    
    while stack:
        node = stack.pop()
        if node == end : break # Lấy node đầu ngăn xếp ra và nếu nó là node end thì ta dừng việc tìm kiếm
        
        # Trong TH chưa là end thì ta mở rộng các node kề với nó
        for adjacentNode, weight in enumerate(matrix[node]): 
            if weight > 0 and adjacentNode not in visited: # Nếu có cạnh nối (weight > 0) và node kề này chưa được thăm
                visited[adjacentNode] = node 
                stack.append(adjacentNode) 
                
    path = PathBuilder.getPath(visited=visited, end=end) # Truy ngược visited để lấy đường đi
        
    return visited, path
                
    
        

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: Thuật toán này giống Dijkstra
    
    visited = {} # VD: visited = {3: 1}; đỉnh 3 đã được thăm và đã được thăm từ đỉnh 1
    lowestCostFromStartToNode = {} # VD: lowestCostFromStartToNode = {3: 5}; Chi phí thấp nhấp từ node nguồn tới node 3 là 5
    pQueue = PriorityQueue()

    pQueue.put((0, start))  # Thêm node start với chi phí = 0
    visited[start] = None  # Đánh dấu đã thăm start
    lowestCostFromStartToNode[start] = 0 

    while not pQueue.empty():
        cost, node = pQueue.get()  
        if node == end: break # Lấy node đầu hàng đợi và nếu là end thì dừng tìm kiếm

        for adjacentNode, weight in enumerate(matrix[node]):
            if weight > 0:
                if adjacentNode not in visited:  # Nếu chưa được thăm
                    visited[adjacentNode] = node
                    lowestCostFromStartToNode[adjacentNode] = cost + weight
                    pQueue.put((cost + weight, adjacentNode))
                else:  # Nếu đã thăm, kiểm tra chi phí mới được tạo nếu thăm từ node đang xét => liệu nó có thấp hơn chi phí trước đó không ?
                    oldCost = lowestCostFromStartToNode[adjacentNode]
                    newCost = cost + weight
                    if newCost < oldCost:
                        visited[adjacentNode] = node
                        lowestCostFromStartToNode[adjacentNode] = newCost
                        pQueue.put((newCost, adjacentNode))

    path = PathBuilder.getPath(visited=visited, end=end) # truy ngược đường đi
          
    return visited, path
    
    

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm 
    heuristic : edge weights
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:

    visited = {} # VD: visited = {3: 1}; đỉnh 3 đã được thăm và đã được thăm từ đỉnh 1
    pQueue = PriorityQueue() 
    
    pQueue.put((0, start)) # Thêm node start với chi phí = 0
    visited[start] = None # Đánh dấu đã thăm 

    while not pQueue.empty(): 
        cost, node = pQueue.get()  
        if node == end:  break # Lấy node đầu hàng đợi và nếu là end thì dừng tìm kiếm
        
        # Trong TH chưa là end thì ta mở rộng các node kề với nó
        for adjacentNode, heuristic in enumerate(matrix[node]): 
            if heuristic > 0 and adjacentNode not in visited:
                pQueue.put((heuristic, adjacentNode))
                visited[adjacentNode] = node 

    path = PathBuilder.getPath(visited=visited, end=end) # Truy ngược visited để lấy đường đi
    
    return visited, path
    

    

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
    heuristic: eclid distance based positions parameter
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    
    visited = {} # VD: visited = {3: 1}; đỉnh 3 đã được thăm và đã được thăm từ đỉnh 1
    lowestCostFromStartToNode = {} # VD: lowestCostFromStartToNode = {3: 5}; Chi phí thấp nhấp từ node nguồn tới node 3 là 5
    pQueue = PriorityQueue()  
    
    #Khởi tạo các thông tin ban đầu
    pQueue.put((0, start))  
    visited[start] = None
    lowestCostFromStartToNode[start] = 0;
    
    while not pQueue.empty():
        cost, node = pQueue.get()
        if node == end : break
        
        for adjacentNode, weight in enumerate(matrix[node]):
            if weight > 0:
                gn = cost + weight # Hàm g(n): chi phí từ nguồn tới node n
                hn = PathBuilder.heuristic(node=adjacentNode, end=end, pos=pos) # Hàm h(n): chi phí heuristic từ node n tới đích
                fn = gn + hn
                if adjacentNode not in visited:  # Nếu chưa được thăm
                    visited[adjacentNode] = node
                    lowestCostFromStartToNode[adjacentNode] = fn
                    pQueue.put((fn, adjacentNode))
                else: # Nếu đã thăm rồi thì kiểm tra liệu chi phí mới được tạo ra từ node đang xét có thấp hơn chi phí cũ hay không
                    oldCost = lowestCostFromStartToNode[adjacentNode]
                    newCost = fn;
                    if newCost < oldCost:
                        visited[adjacentNode] = node
                        lowestCostFromStartToNode[adjacentNode] = newCost
                        pQueue.put((newCost, adjacentNode))
                        
    path = PathBuilder.getPath(visited=visited, end=end) # truy ngược tìm đường đi
    
    return visited, path
                



def Beam(matrix, start, end):
    """
    Perform beam search on a graph represented by an adjacency matrix.
    
    Parameters:
    -----------
    adj_matrix : numpy.ndarray
        The adjacency matrix representing the graph. adj_matrix[i][j] is the weight of the edge from node i to node j, or 0 if there is no edge.
    start_node : int
        The index of the starting node.
    end_node : int
        The index of the goal node.
    beam_width : int
        The maximum number of paths to consider at each step.
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:
    
    # Khởi tạo các dữ liệu cần thiết
    visited = {}  
    beamWidth = 5 # số đường đi tối đa được xem xét ở mỗi bước (chỉ chọn 3 đường tốt nhất để mở rộng)
    pQueue = PriorityQueue()  
    
    pQueue.put((0, [start]))
    visited[start] = None

    while not pQueue.empty():
        for _ in range(min(beamWidth, pQueue.qsize())): 
            cost, path = pQueue.get() 
            endNode = path[-1]  # Lấy node cuối đường đi, VD: A->B->C->D => lấy ra D

            if endNode == end:  # Nếu node lấy ra là end thì dừng tìm kiếm
                return visited, path  

            for adjacentNode, weight in enumerate(matrix[endNode]): 
                if weight > 0 and adjacentNode not in visited:  
                    # Thêm đường đi mới vào queue, VD đang xét D và đỉnh kề là E => A->B->C->D->E; Chi phí sẽ cộng thêm từ D đến E
                    pQueue.put((cost + weight, path + [adjacentNode])) 
                    visited[adjacentNode] = endNode  
                    
    return visited, "Không tồn tại đường đi"