from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pymysql
# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(options=options)
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
os.chdir(r'C:\Users\Administrator\Desktop\DB3')
logging.basicConfig(filename="france.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is new debug info ")
driver = webdriver.Chrome(ChromeDriverManager().install())
 
datas = ['contract', 'opan', 'high', 'low', 'last', 'current_price', 'vol']
    
contracts = ['@HG.1', '@HG.2', '@HG.3', '@HG.4', '@HG.5', '@HG.6', '@GC.1', '@GC.2', '@GC.3', '@GC.4', '@GC.5', '@GC.6', '@SI.1', '@SI.2', '@SI.3', '@SI.4', '@SI.5', '@SI.6', '@CL.1', '@CL.2', '@CL.3', '@CL.4', '@CL.5', '@CL.6', '@NG.1', '@NG.2', '@NG.3', '@NG.4', '@NG.5', '@NG.6', 'US10Y', 'US2Y', 'US5Y', '@UXX.1']
for j in contracts:
    driver.get("https://www.cnbc.com/quotes/"+j)
    driver.implicitly_wait(30)
    contract = j
    opan = driver.find_element(By.XPATH, "//div[@class='Summary-subsection']//*[contains(text(), 'Open')]/following-sibling::*").text
    high = driver.find_element(By.XPATH, "//div[@class='Summary-subsection']//*[contains(text(), 'Day High')]/following-sibling::*").text
    low = driver.find_element(By.XPATH, "//div[@class='Summary-subsection']//*[contains(text(), 'Day Low')]/following-sibling::*").text
    last = driver.find_element(By.XPATH, "//div[@class='Summary-subsection']//*[contains(text(), 'Prev Close')]/following-sibling::*").text
    try:
        current_price = driver.find_element(By.XPATH, "//div[@class='Summary-subsection']//*[text()='Price']/following-sibling::*").text
    except:
        current_price = '-'
    try:
        vol = driver.find_element(By.XPATH, "//div[@class='Summary-subsection']//*[contains(text(), 'Average Volume')]/following-sibling::*").text
    except:
        vol = '-'
    
    print(contract, opan, high, low, last, current_price, vol)
    datas.append([contract, opan, high, low, last, current_price, vol])
    
try:
    driver.get("http://www.dce.com.cn/webquote/mobile/m_futures_quote_en.jsp?varietyid=I")
    driver.implicitly_wait(30)
    data = [i.text.split(' ') for i in driver.find_elements(By.XPATH, '//table[@id="dataTable"]/tbody//tr')[:6]]
    for i in data:
        contract, opan, high, low, last, vol = i[0], i[1], i[2], i[3], i[4], i[10]
        print(contract, opan, high, low, last, current_price, vol)
        datas.append([contract, opan, high, low, last, current_price, vol])
    connection = pymysql.connect(host='database1-instance-1.crydakzjfkez.ap-southeast-2.rds.amazonaws.com',
                             user='admin',
                             password='sadwyr-sobbun-6tuRzo',
                             )
    cursor = connection.cursor()
    cursor.execute('use Script')
    for i in range(1,len(datas)):
        query = f'''INSERT INTO DR2 (`contract`,`Open`,`High`, `Low`, `Last`,`Current_price`,`Volume`)
    VALUES ('{datas[i][0]}','{datas[i][1]}','{datas[i][2]}','{datas[i][3]}','{datas[i][4]}','{datas[i][5]}','{datas[i][6]}');'''
    #     print(query)
        cursor.execute(query)
        cursor.connection.commit()
except:
    pass