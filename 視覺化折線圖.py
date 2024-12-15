import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

MYSQL_HOST = 'localhost'
MYSQL_DB ='就業數據'  #用heidi的mysql，不用副檔名
MYSQL_USER = 'root'
MYSQL_PASS = input("請輸入密碼: ")
# 連接mysql
def connect_mysql():
    global connect, cursor
    connect = pymysql.connect(host = MYSQL_HOST,db= MYSQL_DB,user = MYSQL_USER,password = MYSQL_PASS,\
            charset = 'utf8',use_unicode = True)
    cursor = connect.cursor()

connect_mysql() #讀mysql
sql1 = """SELECT x軸,製造業,住宿及餐飲業,醫療保健及社會工作服務業,
        出版、影音製作、傳播及資通訊服務業,金融及保險業
        FROM 月薪"""
        
# 直接讀進來轉成DataFrame
df1 = pd.read_sql(sql1, con = connect)
df1 = df1.set_index("x軸")

# print(df1.info()) 判斷資料型態

# #建立cursor物件
# cursor1 = conn.execute(sql1)
# # 轉DataFrame
# df1 = pd.DataFrame(cursor1)
# df1 = df1.set_index(0)
# # 關閉連接
# conn.close()

# 事後才做文字處理 作法不對
# for col in df1:
#     df1[col] = df1[col].str.replace(',', '') # 取代,
#     df1[col] = df1[col].astype("int64") # astype轉成int
# 中文字設定
plt.rcParams["font.family"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 22
# 畫布設定
plt.figure(figsize=(15, 10),facecolor="#77FF00")
# markersize是 marker大小大小設定
for col in df1: # 將欄位一個一個以點與線的方式呈現出來
    plt.plot(df1[col],"o-",markersize = 10, label=col,linewidth = 5)
    #將索引以及欄位中的值一個個用text的方式標在點上 ha表水平居中 va表垂直向下
    for i, val in enumerate(df1[col]): 
        plt.text(i, val, f"{val:}", ha="center", va="bottom")
    # 放位置寫法 ncol欄位數 水平放
    # plt.legend(title = "五年間月薪資變動折線圖",ncol = 5 ,loc = 9)
    plt.legend(loc = "upper left",fontsize = 16)
    plt.xticks(np.arange(5),(df1.index)) 
    plt.xlabel("年份")
    plt.ylabel("平均月薪(元)")
    plt.ylim(30000,80000)
    plt.title("五年間月薪資變動折線圖")
    plt.grid(axis = "y",linewidth = 3)

sql2 = """SELECT x軸, 製造業,住宿及餐飲業,醫療保健及社會工作服務業,
        出版、影音製作、傳播及資通訊服務業,金融及保險業
        FROM 求才利用率"""
# 直接讀進來轉成DataFrame
df2 = pd.read_sql(sql2, con = connect)
df2 = df2.set_index("x軸")
# 中文字設定
plt.rcParams["font.family"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 22
# 畫布設定
plt.figure(figsize=(15, 10),facecolor=("#77FF00"))
# markersize是 marker大小大小設定
for col in df2: # "o-"是圓點加實線表示
    plt.plot(df2[col],"o-",markersize = 10, label=col,linewidth = 5)
    # for i, val in enumerate(df2[col]):
    #     plt.text(i, val, f"{val:}", ha="center", va="bottom")
    plt.legend(loc = "upper right",fontsize = 16)
    plt.xticks(np.arange(5),(df2.index))
    plt.xlabel("年份")
    plt.ylabel("求才利用率(%)")
    plt.ylim(45,80)
    plt.title("五年間求才利用率變動折線圖")
    plt.grid(axis = "y",linewidth = 3)

  
sql3 = """SELECT x軸,製造業,住宿及餐飲業,醫療保健及社會工作服務業,
        金融及保險業,藝術、娛樂及休閒服務業
        FROM 離職失業率"""
# 直接讀進來轉成DataFrame
df3 = df2 = pd.read_sql(sql3, con = connect)
df3 = df3.set_index("x軸")
# 中文字設定
plt.rcParams["font.family"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 22
# 畫布設定
plt.figure(figsize=(15, 10),facecolor=("#77FF00"))
# markersize是 marker大小大小設定
for col in df3: # "o-"是圓點加實線表示
    plt.plot(df3[col],"o-",markersize = 10, label=col,linewidth = 5)
    for i, val in enumerate(df3[col]):
        plt.text(i, val, f"{val:}", ha="center", va="bottom")
    plt.legend(loc = "upper left",fontsize = 16)
    plt.xticks(np.arange(5),(df3.index))
    plt.xlabel("年份")
    plt.ylabel("離職失業率(%)")
    # plt.ylim(45,80)
    plt.title("五年間離職失業率變動折線圖")
    plt.grid(axis = "y",linewidth = 3)

    
# sql4 = """SELECT x軸, 製造業,運輸及倉儲業,住宿及餐飲業,
#         出版、影音製作、傳播及資通訊服務業,金融及保險業
#         FROM 去年同期增減"""
# # 直接讀進來轉成DataFrame
# df4 = pd.read_sql_query(sql4, conn)
# df4 = df4.set_index("x軸")
# # 中文字設定
# plt.rcParams["font.family"] = "Microsoft YaHei"
# plt.rcParams["font.size"] = 22
# # 畫布設定
# plt.figure(figsize=(15, 10),facecolor=("#77FF00"))
# # markersize是 marker大小大小設定
# for col in df4: # "o-"是圓點加實線表示
#     plt.plot(df4[col],"o-",markersize = 10, label=col,linewidth = 5)
#     for i, val in enumerate(df4[col]):
#         plt.text(i, val, f"{val:}", ha="center", va="bottom")
#     plt.legend(loc = "upper left",fontsize = 16)
#     plt.xticks(np.arange(5),(df4.index))
#     plt.xlabel("年份")
#     plt.ylabel("去年同期增減率(%)")
#     plt.title("五年間月薪平均去年同期增減率變動折線圖")
#     plt.grid(axis = "y",linewidth = 3)   

    
sql5 = """SELECT x軸,製造業,住宿及餐飲業,醫療保健及社會工作服務業,
        出版、影音製作、傳播及資通訊服務業,金融及保險業
        FROM 正常工時"""
# 直接讀進來轉成DataFrame
df5 = pd.read_sql(sql5, con = connect)
df5 = df5.set_index("x軸")
# 中文字設定
plt.rcParams["font.family"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 22
# 畫布設定
plt.figure(figsize=(15, 10),facecolor=("#77FF00"))
# markersize是 marker大小大小設定
for col in df5: # "o-"是圓點加實線表示
    plt.plot(df5[col],"o-",markersize = 10, label=col,linewidth = 5)
    for i, val in enumerate(df5[col]):
        plt.text(i, val, f"{val:}", ha="center", va="bottom")
    plt.legend(loc = "upper left",fontsize = 16)
    plt.xticks(np.arange(5),(df5.index))
    plt.xlabel("年份")
    plt.ylabel("正常工時(hrs)")
    plt.ylim(150,170)
    plt.title("五年間月正常工時變動折線圖")
    plt.grid(axis = "y",linewidth = 3)

    
sql6 = """SELECT x軸,製造業,住宿及餐飲業,醫療保健及社會工作服務業,
        出版、影音製作、傳播及資通訊服務業,金融及保險業
        FROM 加班工時"""
# 直接讀進來轉成DataFrame
df6 = pd.read_sql(sql6, con = connect)
df6 = df6.set_index("x軸")
# 中文字設定
plt.rcParams["font.family"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 22
# 畫布設定
plt.figure(figsize=(15, 10),facecolor=("#77FF00"))
# markersize是 marker大小大小設定
for col in df6: # "o-"是圓點加實線表示
    plt.plot(df6[col],"o-",markersize = 10, label=col,linewidth = 5)
    for i, val in enumerate(df6[col]):
        plt.text(i, val, f"{val:}", ha="center", va="bottom")
    plt.legend(loc = "upper left",fontsize = 16)
    plt.xticks(np.arange(5),(df6.index))
    plt.xlabel("年份")
    plt.ylabel("加班工時(hrs)")
    plt.ylim(1,22)
    plt.title("五年間月加班工時變動折線圖")
    plt.grid(axis = "y",linewidth = 3)
# 計算平均時薪   
df7 = df1//(df5+df6)
# 中文字
plt.rcParams["font.family"] = "Microsoft YaHei"
plt.rcParams["font.size"] = 22
# 畫布設定
plt.figure(figsize=(15, 10),facecolor=("#77FF00"))
# markersize是 marker大小大小設定
for col in df7: # "o-"是圓點加實線表示
    plt.plot(df7[col],"o-",markersize = 10, label=col,linewidth = 5)
    for i, val in enumerate(df7[col]):#
        plt.text(i, val, f"{val:}", ha="center", va="bottom")
    plt.legend(loc = "upper left",fontsize = 16)
    plt.xticks(np.arange(5),(df7.index))
    plt.xlabel("年份")
    plt.ylabel("平均時薪含加班(元)")
    plt.ylim(190,480)
    plt.title("五年間平均時薪變動折線圖")
    plt.grid(axis = "y",linewidth = 3)

plt.show()
# 關連接
connect.close()