class BFS:

    def __init__(self):
        self.n = 0
        self.A = []
        self.visited = []
        self.queue = []
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
        self.size = []

    def scanner(self):
        self.n = int(input())
        self.size = [0] * self.n
        [self.A.append(list(map(int, input().split(" ")))) for i in range(self.n)]

    def boundCheck(self, a,b):
        return (a >= 0 and a < self.n) and (b >= 0 and b < self.n)

    def bfSearch(self, a, b, c):
        self.queue.append((a, b))
        self.A[a][b] = c

        while len(self.queue) > 0:
            vertex = self.queue.pop(0)
            for i in range(len(self.dx)):
                if self.boundCheck(vertex[0] + self.dx[i],vertex[1] + self.dy[i]) \
                        and (self.A[vertex[0] + self.dx[i]][vertex[1] + self.dy[i]]==1):
                    self.A[vertex[0] + self.dx[i]][vertex[1] + self.dy[i]] = c
                    self.queue.append((vertex[0] + self.dx[i],vertex[1] + self.dy[i]))


if __name__ == "__main__":
    temp = BFS()
    temp.scanner()
    count = 0
    for i in range(temp.n):
        for j in range(temp.n):
            if temp.A[i][j] == 1:
                count+=1
                temp.bfSearch(i,j,count+1)
    for i in range(temp.n):
        for j in range(temp.n):
            if temp.A[i][j]:
                temp.size[temp.A[i][j] - 2] += 1

    ans = []
    for item in temp.size:
        if item != 0:
            ans.append(item)
    ans = sorted(ans)
    print(len(ans))
    [print(item) for item in ans]