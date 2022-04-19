from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import pandas as pd

import mysql.connector
from mysql.connector import errorcode
from datetime import date
from datetime import datetime, timedelta


# diaInserido="ontem";#teste remover
# hora="09:34";#teste remover

# print("diaInserido>>: ", diaInserido);
# print("hora>>: ", hora);

# presentday = datetime.now()
# yesterday = presentday - timedelta(1)
# tomorrow = presentday + timedelta(1)

# # print("Yesterday = ", yesterday.strftime('%Y-%m-%d'))
# # print("Today = ", presentday.strftime('%Y-%m-%d'))
# # print("Tomorrow = ", tomorrow.strftime('%Y-%m-%d'));


# #print("Yesterday = ", dataOntem.strftime('%d-%m-%Y');
dataOntem = datetime.now() - timedelta(1);
data = str(dataOntem.strftime('%Y-%m-%d')) + ' '+str('10:20');
date_time_obj = datetime.strptime(data, '%Y-%m-%d %H:%M');
# dia = str(dataOntem.strftime('%d'));
# mes=str(dataOntem.strftime('%m'));
# ano= str(dataOntem.strftime('%Y'));

# print("data: ", data); dataOntem = datetime.now() - timedelta(1);
# print("dataOntem: ", dataOntem);
#

#print("date_time_obj: ", date_time_obj);

# print("dia: ", dia);
# print("mes: ", mes);
# print("ano: ", ano);

try:
    db_connection = mysql.connector.connect(host="localhost", user="root", passwd="root", database="OLXOLAPSIAD");
    cursor = db_connection.cursor();
    print("INSERT INTO >>antes");

    sql = "INSERT INTO produtoolx (nome_anunciante, tipo_anunciante, contato_anunciante, marca, nome, ano_produto, preco, quantidade_parcela, ano, mes, dia, hora, data, estado, cidade, bairro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";
                        
    print('sql: ', sql);
    values = (None, '', '', '', 'Teste', 2020, 'Preço', 1, 2022, 'Mes', 'dia', 'hora', date_time_obj, 'estado', 'cidade', 'bairro');
    cursor.execute(sql, values);
    db_connection.commit();

    print("INSERT INTO >>depois");

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
    else:
        print(error);
else:
    db_connection.close();
    print("Close MySQL connection");