import pandas as pd
from sqlalchemy import create_engine
import pymysql

# 讀取CSV文件
def csv_to_sql(name: str,table_name :str):
    df = pd.read_csv(name)
    print(df)
    
    # 清理列名(去除空格和特殊字符)
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    
    # 連接到MySQL數據庫
    # 請替換以下信息為您的實際數據庫連接信息
    db_username = 'root'
    db_password = 'a22528680'
    db_host = 'localhost'
    db_name = '就業數據'
    
    # 創建數據庫連接
    engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
                           ,pool_size = 10) #連接池大小
    
    # 將數據框寫入MySQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"數據已成功上傳到MySQL數據庫的{table_name}表中。") 

csv_to_sql('修正平均月薪.csv','月薪')
csv_to_sql('求才利用率.csv', '求才利用率')
csv_to_sql('離職失業率.csv', '離職失業率')
csv_to_sql('正常工時.csv', '正常工時')
csv_to_sql('加班工時.csv', '加班工時')