"""
获取基金历史净值（单位净值，累积净值）
name,code,netWorth, ACWorth = getWorth(FundCode)来获取数据，格式为列表，倒序排列
"""
import requests
import time
import execjs
import matplotlib.pyplot as plt

# 构造url
def getUrl(fscode):
  head = 'http://fund.eastmoney.com/pingzhongdata/'
  tail = '.js?v='+ time.strftime("%Y%m%d%H%M%S",time.localtime())
  
  return head+fscode+tail


def getWorth(fscode):
    content = requests.get(getUrl(fscode))
    jsContent = execjs.compile(content.text)
    name = jsContent.eval('fS_name')
    code = jsContent.eval('fS_code')
    #单位净值
    netWorthTrend = jsContent.eval('Data_netWorthTrend')
    #累计净值
    ACWorthTrend = jsContent.eval('Data_ACWorthTrend')

    netWorth = []
    ACWorth = []

    for dayWorth in netWorthTrend[::-1]:
        netWorth.append(dayWorth['y'])

    for dayACWorth in ACWorthTrend[::-1]:
        ACWorth.append(dayACWorth[1])
    return name, code, netWorth, ACWorth

"""
if __name__ == "__main__":
    print("输入基金代码：")
    FundCode = input()
    # 以列表形式返回净值数据
    netWorth, ACWorth = getWorth(FundCode)
    # 倒置净值表
    netWorth = netWorth[::-1]
    ACWorth = ACWorth[::-1]
    # 历史净值绘图
    plt.figure(figsize=(100,100))
    plt.plot(netWorth[:])
    plt.plot(ACWorth[:],color = 'red')
    plt.show()
"""