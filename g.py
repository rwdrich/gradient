import os
import sys

def isIdle(self, pid, n):
    # The current format of the file is:
    # <pid> <cpu %> <mem %>
    # idle is defined as 'the trendline is +- 1

    self.outputFile = "data.txt"
    # Calculating Memory
    data: List[List[int]] = []
#    for line in system.os(f"grep {pid} {self.outputFile} | tail -n {n}").splitlines():
 #       data.append(list(map(int, line.split())))

    sumMem = 0
    for row in data:
        sumMem += row[2]
    averageMem: float = sumMem / n
    averageTime: float = ( 1 + n ) / 2

    # trendline = (sum of x - averageX) (sum of y - averageY) / (sum of x - averageX) ^2
    sumY: float = 0
    for row in data:
        sumY += row[2] - averageMem
    sumX: float = 0
    for i in range(n + 1):
        sumX += i - averageTime
    trendline = ( sumX * sumY ) / ( sumX * sumX ) * averageMem

    return abs(trendline) < 1

def g(self, pid, n):

    self.outputFile = "data.txt"
    # Calculating Memory
    data: List[List[int]] = []
    for line in os.system(f"grep {pid} {self.outputFile} | tail -n {n}").splitlines():
        data.append(list(map(int, line.split())))

    sumy = 0
    xiyi: float = 0
    yi2 = 0
    sumx = 0
    for x in len(range(data)):
        sumy += data[x][2]
        sumxiyi += data[x][2] * (x+1)
        sumxi2  += x * x
        sumx    += x

    trendline = ( n * sumxiyi) - (sumx * sumy )   /  (n * sumxi2) - (sumx * sumx)

    sx = ((n+1 * n) / 2)
    t = (n * sumxiyi) - sx / (n * sumxi2) -  (sx * sx)

