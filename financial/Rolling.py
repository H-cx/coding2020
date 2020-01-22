"""
用于计算滚动窗口平均值
"""
def RollingMean(ACWorth,window):
    index = 0
    head = 1
    mean = 0
    lenAC = len(ACWorth)
    rolling_mean = [0] * lenAC
    windowWorth = ACWorth[:window]
    while(index < window and index < lenAC):
        mean = sum(windowWorth[:index+1]) / (index + 1)
        rolling_mean[index] = mean
        index += 1
    while(index < lenAC):
        windowWorth = ACWorth[head:index+1]
        mean = sum(windowWorth)/window
        rolling_mean[index] = mean
        index += 1
        head += 1
    return rolling_mean
