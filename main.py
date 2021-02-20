class Cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def isInside(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False


def solution(src, dest):
    if src == dest:
        return 0
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    queue = []
    board = [[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23],
             [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47],
             [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]
    visited = [[False for i in range(0, 8)]
               for j in range(0, 8)]
    for x in range(0, 8):
        for y in range(0, 8):
            if board[x][y] == src:
                queue.append(Cell(x, y))
    for x in range(0, 8):
        for y in range(0, 8):
            if board[x][y] == dest:
                dst = Cell(x, y)
    while len(queue) > 0:
        z = queue[0]
        queue.pop(0)

        if z.x == dst.x and z.y == dst.y:
            return z.dist
        for i in range(8):
            x = z.x + dx[i]
            y = z.y + dy[i]

            if isInside(x, y) and not visited[x][y]:
                visited[x][y] = True
                queue.append(Cell(x, y, z.dist + 1))

