from queue import PriorityQueue

gridmain = [[1,2,3],[5,6,0],[7,8,4]]
gridgoal=[[1,2,3],[5,8,6],[0,7,4]]

def swapper(move, loc, gridmain = None):
    r, c = loc[0], loc[1]
    if move == 'r': #Swapping Position
        gridmain[r][c], gridmain[r][c + 1] = gridmain[r][c + 1], gridmain[r][c]
        loc = r, c+1
    elif move == 'l':
        gridmain[r][c], gridmain[r][c - 1] = gridmain[r][c - 1], gridmain[r][c]
        loc = r, c-1
    elif move == 'd':
        gridmain[r][c], gridmain[r + 1][c] = gridmain[r + 1][c], gridmain[r][c]
        loc = r+1, c
    elif move == 'u':
        gridmain[r][c], gridmain[r-1][c] = gridmain[r-1][c], gridmain[r][c]
        loc = r-1, c
    return loc, gridmain

def heuristic(move, loc, gridmain = None, gridgoal = None):
    loc, gridmain = swapper(move, loc, [x[:] for x in gridmain])
    count = 0
    for i in range(len(gridmain)):
        for j in range(len(gridmain)):
            if (i, j) == loc:
                continue
            if gridmain[i][j] != gridgoal[i][j]:
                count+=1
    return count

def aStarSearch(loc, gridmain = None, gridgoal = None):
    cur_r , cur_c = loc
    pq = PriorityQueue()
    vl = []
    cost = 0
    while gridmain != gridgoal:
        vl.append([x[:] for x in gridmain])
        if cur_r != 0:
            pq.put((heuristic('u',(cur_r,cur_c),[x[:] for x in gridmain], gridgoal) + cost,'u'))
        if cur_r != 2:
            pq.put((heuristic('d',(cur_r,cur_c),[x[:] for x in gridmain], gridgoal) + cost,'d'))
        if cur_c != 2:
            pq.put((heuristic('r',(cur_r,cur_c),[x[:] for x in gridmain], gridgoal) + cost,'r'))
        if cur_c != 0:
            pq.put((heuristic('l',(cur_r,cur_c),[x[:] for x in gridmain], gridgoal) + cost,'l'))
        
        mv = pq.get()[-1]
        (t_r, t_c), tempgrid = swapper(mv, (cur_r, cur_c), [x[:] for x in gridmain])
        while tempgrid in vl:
            mv = pq.get()[-1]
            (t_r, t_c), tempgrid = swapper(mv, (cur_r, cur_c), [x[:] for x in gridmain])
        (cur_r, cur_c), gridmain = (t_r, t_c), tempgrid
        cost+=1
        print('\nMove : ',mv)
        for i in gridmain:
            print(i)
    print(f'After {cost} moves (Tree\'s) Goal state reached' )

if __name__ == '__main__':
    aStarSearch((1,2), [x[:] for x in gridmain], gridgoal)
