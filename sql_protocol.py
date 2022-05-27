

import pymysql
from pymysql import Error
import config2
from config2 import password,host,user,db_name      

def normal_vid(a):
    a = str(a)
    a = a.replace('(','')
    a = a.replace(',)','')
    a = a.replace("'",'')
    return a
engine = pymysql.connect(host=host,user=user,password=password,db=db_name)

nameGoods = []
namePromo = []
priceGoods = []
promoBonus = []
result = ''
with open('C:\\vscode\\project\\11.txt','r') as file:
    main_info = file.readline()

try:
    with engine.cursor() as cursor:
        sql = f"SELECT nameGoods from magnit; "
        cursor.execute(sql)
        
        while result != 'None':
            result = cursor.fetchone()
            result = normal_vid(result)
            if result != 'None':
                nameGoods.append(result)
        sql = f"SELECT priceGoods FROM magnit WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        result1 = str(cursor.fetchone())
        result1 = int(normal_vid(result1))

        sql = f"SELECT priceGoods FROM fiveka WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        result2 = (cursor.fetchone())
        result2 = int(normal_vid(result2))
        sql = f"SELECT priceGoods FROM okey WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        result3 = (cursor.fetchone())
        result3 = int(normal_vid(result3))
        
        sql = f"SELECT namePromo FROM magnit WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        name_promo1 = normal_vid(cursor.fetchone())
        sql = f"SELECT namePromo FROM fiveka WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        
        name_promo2 = normal_vid(cursor.fetchone())
        sql = f"SELECT namePromo FROM okey WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        name_promo3 = normal_vid(cursor.fetchone())



        sql = f"SELECT promoBonus FROM magnit WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        price_promo1 = normal_vid(cursor.fetchone())
        sql = f"SELECT promoBonus FROM fiveka WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        price_promo2 = normal_vid(cursor.fetchone())
        sql = f"SELECT promoBonus FROM okey WHERE nameGoods = '{main_info}';"
        cursor.execute(sql)
        price_promo3 = normal_vid(cursor.fetchone())
        with open('C:/vscode/project/12.txt','w') as f:
                f.write('Магнит '+str(result1)+ ' '+ str(name_promo1)+ ' '+ str(price_promo1)+'\n')
                f.write('Пятёрочка '+str(result2)+ ' '+ str(name_promo2)+ ' '+ str(price_promo2)+'\n')
                f.write('Окей '+str(result3)+ ' '+ str(name_promo3)+ ' '+ str(price_promo3))                            
except Error as ex:
    ex
finally: 
    # print('Соединение завершено')
    engine.close()