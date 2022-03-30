import time
from matplotlib import gridspec
start=time.time()

#--------------------------------------------------------------------------------------
#Library
import pyupbit
import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc
import matplotlib.gridspec as gridspec
import sympy as sp

#--------------------------------------------------------------------------------------
#Init Variable
coin_name=[]
coin_price=[]
filter_name=[]
filter_price=[]
daylst=[]
openlst=[]
highlst=[]
lowlst=[]
closelst=[]

#--------------------------------------------------------------------------------------
#Function

def makecsvngraph(namelst,c):
    global daylst,openlst,highlst,lowlst,closelst
    for i in range(len(namelst)):
        fig=plt.figure(figsize=(12,8))
        gs=gridspec.GridSpec(nrows=2,ncols=1,height_ratios=[3,1])
        ax=plt.subplot(gs[0])
        df=pyupbit.get_ohlcv(namelst[i],count=c)
        df.drop(df.index[-1])
        candlestick2_ohlc(ax,df["open"],df["high"],df["low"],df["close"],width=0.5,colorup="r",colordown="b")
        ax.grid()
        ax1=plt.subplot(gs[1])
        tolst=df.values.tolist()
        for j in range(len(tolst)):
            daylst.append(j)
        ax1.bar(daylst,df["volume"],color="k",width=0.6,align="center")
        ax1.grid()
        plt.savefig("C:\\Users\\jmpark\\Desktop\\mPLUS\\VSCode_Folder\\normal\\graph\\"+namelst[i]+".png")
        df.to_csv("C:\\Users\\jmpark\\Desktop\\mPLUS\\VSCode_Folder\\normal\\csv\\"+namelst[i]+".csv")
        print("Save csv&graph : "+namelst[i]+"  "+str(i+1)+"/"+str(len(namelst)))
        plt.close()
        
        daylst=[]
        openlst=[]
        highlst=[]
        lowlst=[]
        closelst=[]
        df=0


#--------------------------------------------------------------------------------------
#Ready Trading

coin_name=pyupbit.get_tickers(fiat="KRW")
krw_price=pyupbit.get_current_price(coin_name)
coin_price=list(krw_price.values())

for i in range(len(coin_name)):
    if coin_price[i]>100 and coin_price[i]<100000:
        filter_name.append(coin_name[i])
        filter_price.append(coin_price[i])
    else:
        pass

makecsvngraph(filter_name,300)

end=time.time()
term=end-start
print("Run Time : ",term)