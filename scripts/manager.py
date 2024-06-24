import matplotlib.pyplot as plt # graphics
import pandas as pd # data management
import numpy as np  # numerical operations 
import yfinance as yf


class FinanceManager:
  def __init__(self,inputs):
    self.inputs=inputs
    print(f"Welcome {inputs['Username']} to the finance manager app!"+'\n')
    print('------------'+'\n')

   #always run 
    self.readdb()
    run=True
    while run:
      self.MENU()
      run=self.keeprunning()

   #Keep runnig app
  def keeprunning(self):
    keep=input('Do you want to perform another action? (y/n): ')
    if keep=='y' or keep=='yes':
      return True
    else:
      return False
    self.MENU()
    
   #app MENU
  def MENU(self):
    print('----------'+'\n')
    print('---Menu---')
    print('1. GENERATE REPORT')
    print('2. ADD LOG')
    print('3. FINANCIAL TICKERS')
    print('\n'+'----------')
    request=input('Option number to perform: ')
    print('\n')
    self.handlemenurequest(request)
  
   #Hnadle menu request
  def handlemenurequest(self,request):
    if request=='1':
      self.report()
    elif request=='2':
      self.addlog()
    elif request=='3':
      self.getTickers()
    else:
      print('Entry not valid D:')

   #report
  def report(self):
    self.balance()
    self.graphlogs() 

   #calculate current balance
  def balance(self):
    b=self.data['AMOUNT'].sum()
    print(f'current balance: ${b}')

   #graphs historical logs
  def graphlogs(self):
    plt.figure(figsize=(10,6))
    plt.title('Historical development of logs')

    #simple logs
    plt.plot(self.data['AMOUNT'],'o',label='Individual log')
    #cumulative
    plt.plot(np.cumsum(self.data['AMOUNT']),'--',label='Cummulative')

    plt.legend()
    plt.show()

   #read database 
  def readdb(self):
    self.data=pd.read_csv(self.inputs['data_route'])

   #save database  
  def savedb(self):
    self.data.to_csv(self.inputs['data_route'],index=False)

   #get log
  def getlog(self):
    print('----------'+'\n')
    day=input('Give a day number: ')
    month=input('Give a month number: ')
    year=input('Give a year number: ')
    amount=float(input('Amount: '))
    category=input('Category: ')
    subcategory=input('subcategory: ')
    comment=input('comment: ')
    print('\n'+'----------')  
    date=f'{day}-{month}-{year}'
    log=[date,amount,category,subcategory,comment]
    return log

   #add log
  def addlog(self):
    log=self.getlog()
    self.data.loc[len(self.data)]=log
    self.savedb()

   #calculate compound interest
  def compound(self,initial,rate,time):
    return initial*(1+rate/100)**time

  def getTickers(self):
    self.downloadtickers(self.selectTickers())
    self.graphTickers()
    self.tickersReport()

  def graphTickers(self):
    plt.figure(figsize=(10,6)); self.tickers['Close'].plot();plt.title('Time series');plt.show()
  
  def selectTickers(self):
    tickers=[]
    add=True
    while add:
      t=input('Tickers: ')
      tickers.append(t)
      s=input('add another ticker? (y/n): ')
      if s=='y':
        add=True
      else:
        add=False
    return tickers 

   # donwload ticker information
  def downloadtickers(self,tickers):
    ticker_string=""
    for i in range(len(tickers)-1):
      ticker_string=ticker_string+tickers[i]+" "
      ticker_string=ticker_string+tickers[-1]
    self.tickers=yf.download(tickers=ticker_string,period="1y")

   # financial report for tickers 
  def tickersReport(self):
    pass 
  
      