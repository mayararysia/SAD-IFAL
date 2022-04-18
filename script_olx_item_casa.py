"""
Este script coleta e armazena dados da categoria 'Para sua casa' do OLX"

Dependências:
    - MySQL na máquina
    $ pip install selenium # Para Instalar o Selenium
    $ pip install pandas #Pandas
    $ pip install mysql-connector-python==8.0.28 #conexão com o mysql v 8.0.28
"""

#Configuramos o driver do browser, no caso o chrome... <br>
#mais informações na documentação [webdriver](https://www.selenium.dev/documentation/webdriver/)

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

print('***');
print('Configurando o driver do browser...Feito!');
print('***');

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import pandas as pd

import mysql.connector
from mysql.connector import errorcode
from datetime import date
import datetime

from selenium.webdriver.common.keys import Keys

#passando o executável do chromedriver instalado na máquina para o selenium se comunicar com o navegador Chrome
#Pode ser esse:
#driver = webdriver.Chrome(executable_path='C:\seleniumChromeDriver/chromedriver.exe');

#Ou esse com options:
driver = webdriver.Chrome('C:\seleniumChromeDriver/chromedriver.exe', options=chrome_options);

print('***');
print('Configurando o path do webdriver.Chrome...Feito!');
print('***');

class ScriptOLX():

    def test_cria_banco_de_dados_OLXOLAPSIAD(self):
         #Cria banco de dados
        try:
            db_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root'
            );

            cursor = db_connection.cursor();
            cursor.execute("CREATE DATABASE IF NOT EXISTS OLXOLAPSIAD");
            
            print("Database OLXOLAPSIAD connection made!");
            print('***');

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong");
            else:
                print(error);
        else:
            db_connection.close();
            print("Close MySQL connection");
            print('***');
    
    def test_cria_tabelas_dimensoes_DW(self):
        try:
            db_connection = mysql.connector.connect(host='localhost', user='root', password='root', database='OLXOLAPSIAD');
  
            cursor = db_connection.cursor();
            
            cursor.execute("DROP TABLE IF EXISTS `dm_fato`");
            cursor.execute("DROP TABLE IF EXISTS `dm_anunciante`");
            cursor.execute("DROP TABLE IF EXISTS `dm_itemCasa`");
            cursor.execute("DROP TABLE IF EXISTS `dm_tempo`");
            cursor.execute("DROP TABLE IF EXISTS `dm_local`");
            
            cursor.execute("""CREATE TABLE `dm_local` (
                `id` bigint(11) NOT NULL AUTO_INCREMENT,
                `estado` varchar(250) DEFAULT NULL,
                `cidade` varchar(250)  DEFAULT NULL,
                `bairro` varchar(250) DEFAULT NULL,
                PRIMARY KEY (`id`))
                ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;""");


            cursor.execute("""CREATE TABLE `dm_tempo` (
                `id` bigint(11) NOT NULL AUTO_INCREMENT,
                `ano` integer DEFAULT NULL,
                `mes` varchar(20)  DEFAULT NULL,
                `dia` varchar(50) DEFAULT NULL,
                `hora` varchar(50) DEFAULT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;""");

            cursor.execute("""CREATE TABLE `dm_itemCasa` (
                `id` bigint(11) NOT NULL AUTO_INCREMENT,
                `marca`  varchar(250) DEFAULT NULL,
                `nome` varchar(250)  DEFAULT NULL,
                `ano` bigint(11) DEFAULT NULL,
                `descricao` varchar(50) DEFAULT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;""");

            cursor.execute("""CREATE TABLE `dm_anunciante` (
            `id` bigint(11) NOT NULL AUTO_INCREMENT,
            `nome`  varchar(250) DEFAULT NULL,
            `tipo` varchar(250)  DEFAULT NULL,
            `contato` varchar(250)  DEFAULT NULL,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;""");


            cursor.execute("""CREATE TABLE `dm_fato` (
                `id_tempo` bigint(11) NOT NULL,
                `id_local` bigint(11) NOT NULL,
                `id_itemCasa` bigint(11) NOT NULL,
                `id_anunciante` bigint(11) NOT NULL,
                `preco` numeric DEFAULT NULL,
                `quantidade_parcela` int DEFAULT NULL,
                PRIMARY KEY (`id_tempo`,  `id_local`,  `id_itemCasa`, `id_anunciante`),
                FOREIGN KEY (`id_tempo`) REFERENCES `dm_tempo`(`id`),
                FOREIGN KEY (`id_local`) REFERENCES `dm_local`(`id`),
                FOREIGN KEY (`id_itemCasa`) REFERENCES `dm_itemCasa`(`id`),
                FOREIGN KEY ( `id_anunciante`) REFERENCES `dm_anunciante`(`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;""");
 
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist");
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong");
            else:
                print(error);
        else:
            db_connection.close();
            print("Close MySQL connection");

    def test_cria_tabela_varredura_produtoolx(self):
        try:
            db_connection = mysql.connector.connect(host='localhost', user='root', password='root', database='OLXOLAPSIAD');
  
            cursor = db_connection.cursor();
            
            cursor.execute("DROP TABLE IF EXISTS `produtoolx`");
            
            cursor.execute("""CREATE TABLE `produtoolx` (
                `id` bigint(11) NOT NULL AUTO_INCREMENT,
                `nome_anunciante` varchar(250) DEFAULT NULL,
                `tipo_anunciante` varchar(250)  DEFAULT NULL,
                `contato_anunciante` varchar(250)  DEFAULT NULL,
                `marca` varchar(250) DEFAULT NULL,
                `nome` varchar(250) DEFAULT NULL,
                `ano_produto` bigint(11) DEFAULT NULL,
                `preco` varchar(50) DEFAULT NULL,
                `quantidade_parcela` int DEFAULT NULL,
                `ano` integer DEFAULT NULL,
                `mes` varchar(20)  DEFAULT NULL,
                `dia` varchar(50) DEFAULT NULL,
                `hora` varchar(50) DEFAULT NULL,
                `data` timestamp DEFAULT NULL,
                `estado` varchar(250) DEFAULT NULL,
                `cidade` varchar(250)  DEFAULT NULL,
                `bairro` varchar(250) DEFAULT NULL,
                PRIMARY KEY (`id`))
                ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;""");
                
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist");
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong");
            else:
                print(error);
        else:
            db_connection.close();
            print("Close MySQL connection");

    def test_chama_categoria_para_sua_casa_olx(self):
        db_connection = mysql.connector.connect(host="localhost", user="root", passwd="root", database="OLXOLAPSIAD");
        cursor = db_connection.cursor();

        driver.maximize_window();#maximizando a janela do Chrome
        url = 'https://al.olx.com.br/alagoas/maceio/para-a-sua-casa';
        driver.get(url);

        #sInsert ='';
        arrayItensCasa=[];
        itensCasa=[];
        # endereco = [];

        i = 54;
        #for i in range(54):
        for i in range(51):
             try:
                sXPath = '//*[@id="ad-list"]/li[' + str(i+1) +  ']';
                sxPathEndereco = '//*[@id="ad-list"]/li['+str(i+1)+']/div/a/div/div[2]/div[2]/div[2]/div[1]/div/div[1]';

                #sXPath= "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[7]/div/div/div/div[10]/div/div/div/ul/li[" + str(i+1) + "]";

                # endereco.append(driver.find_element(By.XPATH, sxPathEndereco));
                itensCasa.append(driver.find_element(By.XPATH, sxPathEndereco));
                itensCasa.append(driver.find_element(By.XPATH,sXPath));

                if itensCasa[i] and itensCasa[i].text:
                    arrayItensCasa.append(itensCasa[i].text.splitlines());

                print("\nindex: ", i);
               
                #if itensCasa[i] and itensCasa[i].text:
                if itensCasa[i] and itensCasa[i].text and arrayItensCasa[i]:
                 print("\n");
                # print("itensCasa[i].text:", itensCasa[i].text);
                 print("arrayItensCasa[i]: ", arrayItensCasa[i]);

                 descricao = None;
                 diaInserido = None;
                 dia = None;
                 mes = None;
                 ano = None;
                 hora = None;
                 nome_anunciante = None;
                 quantidade_parcela = None;
                 date_time_obj=None;

                 horaInserida = arrayItensCasa[i][len(arrayItensCasa[i])-1];
                 horaInserida2 = horaInserida.split(" ");
                 hora = horaInserida2[len(horaInserida2)-1];

                 print("horaInserida2: ", horaInserida2);
                 print("hora: ", hora);

                 diaInserido = horaInserida2[0].replace(",", "");
                 #splitHora = hora.split(':');

                 print("diaInserido: ", diaInserido);
                 
                 """
                 if not (':'in hora):
                    print('aqui');
                    descricao = descricao+hora;
                    hora = datetime.time;
                """

                 current_date = date.today();

                 if ':'in hora:

                    if diaInserido.lower() == 'hoje':
                        data = str(current_date.strftime('%Y-%m-%d')) + ' '+str(hora);
                        date_time_obj = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M')
                        dia = str(current_date.strftime('%d'));
                        mes=str(current_date.strftime('%m'));
                        ano= str(current_date.strftime('%Y'));
                    else:
                        # //pegar o dia e converter pra numero abr ==04 e etc
                        data = str(diaInserido) + ' '+str(hora);
                        print("não é hoje - data: ", data);
                        dia = data.split('/')[0];
                        print("dia: ", dia);
                        mes=data.split('/')[1];
                        print("mes: ", mes);
                        ano=data.split('/')[2];
                        print("ano: ", ano);

                print("descricao: ", descricao);
                # print("dia: ", dia);
                # print("mes: ", mes);
                # print("ano: ", ano);
                if date_time_obj != None:
                    print('Date:', date_time_obj.date());
                    print('Time:', date_time_obj.time());
                    print('Date-time:', date_time_obj);

                """
                marca = None;
                nome = arrayItensCasa[i][0];
                preco = arrayItensCasa[i][1];

                nome_anunciante = None;
                quantidade_parcela = None;
                tipo = arrayItensCasa[i][2];

                
                sql = "INSERT INTO produtoolx (nome_anunciante, tipo_anunciante, contato_anunciante, marca, nome, ano_produto, preco, quantidade_parcela, ano, mes, dia, hora, estado, cidade, bairro) VALUES (%s, %s, %s, %s, %s, %s, %d, %s, %d, %d, %s, %s, %s, %s, %s, %s)";
                values = ("AL", "Maceió");
                cursor.execute(sql, values);
                db_connection.commit();
                """

             except:
                print("Ocorreu um erro ao tentar imprimir o item de casa no OLX. Contate a administração.");

if __name__ == "__main__": #condição do python para executar diretamente esse script
    test_olx = ScriptOLX(); #instaciando a classe "ScriptOLX()"

    #commands DDL
    """
    test_olx.test_cria_banco_de_dados_OLXOLAPSIAD();
    test_olx.test_cria_tabelas_dimensoes_DW();
    test_olx.test_cria_tabela_varredura_produtoolx();
    """

    test_olx.test_chama_categoria_para_sua_casa_olx();