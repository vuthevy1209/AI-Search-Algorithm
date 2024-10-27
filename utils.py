import math

class PathBuilder:
    @staticmethod
    def getPath(visited, end):
        path = []    
        if end in visited:  # Nếu end đã được thăm thì có nghĩa là tồn tại đường đi
            while end is not None:  # Đoạn này là em đang truy ngược lại cái đường đi dựa vào visited
                path.append(end)
                end = visited[end]
            path.reverse()
        else:
            return []  # "Không tồn tại đường đi"
        
        return path
    
    @staticmethod
    def heuristic(node, end, pos):
        return math.sqrt((pos[node][0] - pos[end][0])**2 + (pos[node][1] - pos[end][1])**2)