import sys
currfile = sys.argv[1] if len(sys.argv) > 1 else "maze2.txt"
write = sys.argv[2] if len(sys.argv) == 3 else None

#Load the maze as nodes with no parents and -1 distances
def load_maze():
    dist,parents = {},{}
    f = open(currfile,'r')
    maze = f.read().split('\n')
    f.close()
    for linenum,line in enumerate(maze):
        for index,character in enumerate(line):
            if character == "X":
                start = (linenum,index)
                dist[(linenum,index)] = 0
                parents[(linenum,index)] = None
            elif character == " " or character == "O":
                dist[(linenum,index)] = -1
                parents[(linenum,index)] = None
                if character == "O":
                    end = (linenum,index)
    return dist,parents,start,end,maze
#Find the shortest path and update parents and distances using BFS
def find_shortest_path(m,i1,j1,dist,parents):
    from collections import deque
    q = deque([(i1,j1)])
    visited  = set()
    while q:
        i,j = q.popleft()
        left,right = (i,j-1),(i,j+1)
        bottom,top = (i+1,j),(i-1,j)
        if valid(left,maze,visited,dist):
            dist[left] = dist[(i,j)]+1
            parents[left] = (i,j)
            q.append(left)
            visited.add(left)
        if valid(right,maze,visited,dist):
            dist[right] = dist[(i,j)]+1
            parents[right] = (i,j)
            q.append(right)
            visited.add(right)
        if valid(bottom,maze,visited,dist):
            dist[bottom] = dist[(i,j)]+1
            parents[bottom] = (i,j)
            q.append(bottom)
            visited.add(bottom)
        if valid(top,maze,visited,dist):
            dist[top] = dist[(i,j)]+1
            parents[top] = (i,j)
            q.append(top)
            visited.add(top)
#Helper function to check bounds, character, visited, and distance
def valid(point,arr,visited,dist):
    strings = [" ","O"]
    if point[0] >= 0 and point[0] < len(arr):
        if point[1] >= 0 and point[1] < len(arr[0]):
            if arr[point[0]][point[1]] in strings:
                if point not in visited and dist[point] == -1:
                    return True
    return False
#Output path by printing or writing to file
def output_path(parents,maze,start,write = False):
    for line in maze:
        print line
    newmaze = []
    for line in maze:
        newmaze.append(list(line))
    curr = parents[end]
    while curr != start:
        newmaze[curr[0]][curr[1]] = "+"
        curr = parents[curr]
    if write:
        with open(currfile,"a") as f:
            for line in newmaze:
                f.write("".join(line))
                f.write("\n")
    for line in newmaze:
        print "".join(line)

dist,parents,start,end,maze = load_maze()
find_shortest_path(maze,start[0],start[1],dist,parents)
output_path(parents,maze,start)