import os
import system

def isIdle(self, pid, n):
    # The current format of the file is:
    # <pid> <cpu %> <mem %>
    # idle is defined as 'the trendline is +- 1

    self.outputFile = "data.txt"
    # Calculating Memory
    data: List[List[int]] = []
    for line in system.os(f"grep {pid} {self.outputFile} | tail -n {n}").splitlines():
        data.append(list(map(int, line.split())))

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


