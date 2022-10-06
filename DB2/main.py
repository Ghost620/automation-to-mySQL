import requests,time
import pymysql
import logging
import os
os.chdir(r'C:\Users\Administrator\Desktop\DB2')
logging.basicConfig(filename="france.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is new debug info ")

equity_comp = ['BTC', 'ETH']
for a in equity_comp:
    url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={a}&market=USD&interval=5min&apikey=PJEBBJNC5XGIIA9J&outputsize=compact'
    r = requests.get(url)
    data = r.json()

    datas = []
    for i,j in data["Time Series Crypto (5min)"].items():
        timee, opan, high, low, close, vol = i, j['1. open'], j['2. high'], j['3. low'], j['4. close'], j['5. volume']
        datas.append([a, timee, opan, high, low, close, vol])

    datas = datas[:96]
    print(datas)
    print('------------------------------------------------------------------------------------------')
    print()
    connection = pymysql.connect(host='database1-instance-1.crydakzjfkez.ap-southeast-2.rds.amazonaws.com',
                             user='admin',
                             password='sadwyr-sobbun-6tuRzo',
                             )
    cursor = connection.cursor()
    cursor.execute('use Script')
    for i in range(1,len(datas)):
        query = f'''INSERT INTO DR3 (`Type`, `Time`, `Open`,`High`, `Low`, `CLose`,`Volume`)
    VALUES ('{datas[i][0]}','{datas[i][1]}','{datas[i][2]}','{datas[i][3]}','{datas[i][4]}','{datas[i][5]}','{datas[i][6]}');'''
    #     print(query)
        cursor.execute(query)
        cursor.connection.commit()
time.sleep(10)



equity_comp = ['BHP', 'RIO', 'GOLD', 'FCX', 'VALE', 'ARKK', 'GS', 'AAPL', 'GOOG']
for a in equity_comp:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={a}&interval=15min&apikey=PJEBBJNC5XGIIA9J&outputsize=compact'
    r = requests.get(url)
    data = r.json()

    datas = []
    time.sleep(12)
    for i,j in data["Time Series (15min)"].items():
        timee, opan, high, low, close, vol = i, j['1. open'], j['2. high'], j['3. low'], j['4. close'], j['5. volume']
        datas.append([a, timee, opan, high, low, close, vol])

    datas = datas[:96]
    print(datas)
    print('------------------------------------------------------------------------------------------')
    print()
    connection = pymysql.connect(host='database1-instance-1.crydakzjfkez.ap-southeast-2.rds.amazonaws.com',
                             user='admin',
                             password='sadwyr-sobbun-6tuRzo',
                             )
    cursor = connection.cursor()
    cursor.execute('use Script')
    for i in range(1,len(datas)):
        query = f'''INSERT INTO DR3 (`Type`, `Time`, `Open`,`High`, `Low`, `CLose`,`Volume`)
    VALUES ('{datas[i][0]}','{datas[i][1]}','{datas[i][2]}','{datas[i][3]}','{datas[i][4]}','{datas[i][5]}','{datas[i][6]}');'''
    #     print(query)
        cursor.execute(query)
        cursor.connection.commit()

equity_comp = ['USD', 'EUR', 'GBP', 'NZD', 'CNY']
for a in equity_comp:
    url = f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={a}&to_symbol=AUD&interval=15min&apikey=PJEBBJNC5XGIIA9J&outputsize=compact'
    r = requests.get(url)
    data = r.json()
    
    datas = []
    for i,j in data["Time Series FX (15min)"].items():
        timee, opan, high, low, close, vol = i, j['1. open'], j['2. high'], j['3. low'], j['4. close'], '-'
        datas.append([a, timee, opan, high, low, close, vol])

    datas = datas[:96]
    print(datas)
    print('------------------------------------------------------------------------------------------')
    print()
    connection = pymysql.connect(host='database1-instance-1.crydakzjfkez.ap-southeast-2.rds.amazonaws.com',
                             user='admin',
                             password='sadwyr-sobbun-6tuRzo',
                             )
    cursor = connection.cursor()
    cursor.execute('use Script')
    for i in range(1,len(datas)):
        query = f'''INSERT INTO DR3 (`Type`, `Time`, `Open`,`High`, `Low`, `CLose`,`Volume`)
    VALUES ('{datas[i][0]}','{datas[i][1]}','{datas[i][2]}','{datas[i][3]}','{datas[i][4]}','{datas[i][5]}','{datas[i][6]}');'''
    #     print(query)
        cursor.execute(query)
        cursor.connection.commit()