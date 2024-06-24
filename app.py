import matplotlib.pyplot as plt # graphics
import pandas as pd # data management
import numpy as np  # numerical operations 
import yfinance as yf
from scripts.manager import FinanceManager


inputs = {
    "Username": 'Aaron',
    "data_route": './data/finance.csv'
}

if __name__== '__main__':
    fm=FinanceManager(inputs)