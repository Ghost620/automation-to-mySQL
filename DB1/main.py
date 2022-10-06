from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pymysql
import logging
import os
os.chdir(r'C:\Users\Administrator\Desktop\DB1')
logging.basicConfig(filename="france.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is new debug info ")


from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("window-size=1200x600")
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

lst = ['BHP', 'RIO', 'FMG', 'MIN', 'HIO', 'MGT', 'WHC', 'VMS', 'CIA', 'WPL', 'ANZ', 'CBA', 'WBC', 'NAB', 'MQG', 'BEN', 'BOQ', 'CHN', 'OZL', 'MZZ', 'RDS', 'AGL', 'ORG', 'MEZ', 'STO', 'QAN', 'BPT', 'WOR', 'NEW', 'GNX', 'OSH', 'NCM', 'SLR', 'EVN', 'SVL', 'PDI', 'TMZ', 'MZZ', 'SYR', 'CXO', 'AZL', 'MNS', 'PLS', 'EUR', 'SYA', 'LKE', 'WSA', 'ADD','TLS','CSL', 'CWN', 'FLT', 'TWE', 'QBE', 'CWY', 'NUF', 'EMD', 'AIZ', 'A2M', 'IXR', 'MRD', 'WOW', 'MYR', 'WES', 'HVN', 'COL', 'RBL', 'APX', 'HUM', 'ZIP', 'ERA', '92E']
data = [['COMPANY', 'PRICE', "VOLUME", 'P/E RATIO', 'PRICE/FREE CASH FLOW', 'ANNUAL YIELD']]
lst = list(set(lst))
for i in lst:
    
    driver.get("https://www2.asx.com.au/markets/company/"+f'{i}')
    
    time.sleep(5)
    price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Last Price')]/../*[2]"))).text.split(' ')[0]
    volume = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='company_header']/div/div[1]/div/div[2]/dl[2]/dd"))).text
    pe = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'P/E ratio')]/../*[2]"))).text
    pf = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Price/free cash flow')]/../*[2]"))).text
    an_yield = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Annual yield')]/../*[2]"))).text
    
    print(i, price, volume, pe, pf, an_yield)
    data.append([i, price, volume, pe, pf, an_yield])
connection = pymysql.connect(host='database1-instance-1.crydakzjfkez.ap-southeast-2.rds.amazonaws.com',
                             user='admin',
                             password='sadwyr-sobbun-6tuRzo',
                             )
cursor = connection.cursor()
cursor.execute('use Script')
for i in range(1,len(data)):
    query = f'''INSERT INTO DR1 (`Name`, `Price`, `Volume`,`P/E ratio`, `Price/free Cashflow`, `Annual yield`)
VALUES ('{data[i][0]}','{data[i][1]}','{data[i][2]}','{data[i][3]}','{data[i][4]}','{data[i][5]}');'''
#     print(query)
    cursor.execute(query)
    cursor.connection.commit() 
# with xlsxwriter.Workbook('test.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()

#     for row_num, dat in enumerate(data):
#         worksheet.write_row(row_num, 0, dat)