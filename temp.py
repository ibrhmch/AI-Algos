from queue import PriorityQueue

gridmain = [[0,1,3],[4,2,5],[7,8,6]]
gridgoal = [[0,1,2],[3,4,5],[6,7,8]]
print('Start State')
for i in gridmain:
    print(i)

print('\nGoal State')
for i in gridgoal:
    print(i)

def swapper(cur, loc, gridmain = None):
    (cr, cc), (nr, nc) = cur, loc
    gridmain[cr][cc], gridmain[nr][nc] = gridmain[nr][nc], gridmain[cr][cc]
    return gridmain

def heuristic(gridmain = None, gridgoal = None):
    count = 0
    for i in range(len(gridmain)):
        for j in range(len(gridmain)):
            if gridmain[i][j] != gridgoal[i][j]:
                count+=1
    return count

def ucs(loc, gridmain = None, gridgoal = None):
    cur_r, cur_c = loc
    pq = PriorityQueue()
    pq.put((0, (gridmain, cur_r, cur_c)))
    vl = []
    count=0
    while gridmain != gridgoal:
        cost, (gridmain, nr, nc) = pq.get()
        while gridmain in vl:
            cost, (gridmain, nr, nc) = pq.get()
        count+=1
        vl.append(gridmain)
        cur_r, cur_c = nr, nc
        if cur_r != 0:
            tempgrid = swapper((cur_r, cur_c), (cur_r-1,cur_c),[x[:] for x in gridmain])
            cost = heuristic(tempgrid, gridgoal)
            pq.put((cost, (tempgrid, cur_r-1, cur_c)))
        if cur_r != 2:
            tempgrid = swapper((cur_r, cur_c), (cur_r+1,cur_c),[x[:] for x in gridmain])
            cost = heuristic(tempgrid, gridgoal)
            pq.put((cost, (tempgrid, cur_r+1, cur_c)))
        if cur_c != 0:
            tempgrid = swapper((cur_r, cur_c), (cur_r,cur_c-1),[x[:] for x in gridmain])
            cost = heuristic(tempgrid, gridgoal)
            pq.put((cost, (tempgrid, cur_r, cur_c-1)))
        if cur_c != 2:
            tempgrid = swapper((cur_r, cur_c), (cur_r,cur_c+1),[x[:] for x in gridmain])
            cost = heuristic(tempgrid, gridgoal)
            pq.put((cost, (tempgrid, cur_r, cur_c+1)))

    print(f'\nTotal states traversed : {count}')
    for i in gridmain:
        print(i)
        
if __name__ == '__main__':
    ucs((0,0), [x[:] for x in gridmain], gridgoal)