from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import pandas as pd

import mysql.connector
from mysql.connector import errorcode
from datetime import date
from datetime import datetime, timedelta


diaInserido="ontem";#teste remover
hora="09:34";#teste remover

print("diaInserido>>: ", diaInserido);
print("hora>>: ", hora);

presentday = datetime.now() 
yesterday = presentday - timedelta(1) 
tomorrow = presentday + timedelta(1) 
  
# print("Yesterday = ", yesterday.strftime('%Y-%m-%d')) 
# print("Today = ", presentday.strftime('%Y-%m-%d')) 
# print("Tomorrow = ", tomorrow.strftime('%Y-%m-%d'));


dataOntem = datetime.now() - timedelta(1);
print("dataOntem: ", dataOntem);
#print("Yesterday = ", dataOntem.strftime('%d-%m-%Y');

data = str(dataOntem.strftime('%Y-%m-%d')) + ' '+str(hora);
date_time_obj = datetime.strptime(data, '%Y-%m-%d %H:%M');
dia = str(dataOntem.strftime('%d'));
mes=str(dataOntem.strftime('%m'));
ano= str(dataOntem.strftime('%Y'));

print("data: ", data);

print("date_time_obj: ", date_time_obj);

print("dia: ", dia);
print("mes: ", mes);
print("ano: ", ano);