import streamlit as st
import pandas as pd
import openpyxl as px
import os
import datetime
import time
import sys
import base64

# 参照URL: https://www.youtube.com/watch?v=4nsTce1Oce8
#--------------------------------------------------------------------------
#CSVファイルが無ければ作る


#-------------------------------------------------------------------------------
#pandasの編集

filename = r"C:/Users/user/OneDrive/デスクトップ/DB_New.csv"

#ファイルがない場合は「DB_New.csv」をデスクトップに作成してプログラム実行
#所定の端末のパスを指定する必要あり
        
#--------------------------------------------------------------------------
#Webフォームの


with st.form(key = 'profile_form'):
    st.markdown('データ入力フォーム')

#-------------------------------
    name = st.text_input('名前')
    #age = st.text_input('年齢')
    age = st.slider(label='年齢',
                    min_value=0,
                    max_value=130,
                    value=30,
    )
    
    adress = st.text_input('住所')
    phone = st.text_input('連絡先')
    mail = st.text_input('メールアドレス')

    date = st.date_input('登録日')
#-------------------------------

    submit_btn = st.form_submit_button('登録')
    cancel_btn = st.form_submit_button('キャンセル')

#--------------------------------------------------------------------------
    if submit_btn:

        df1 = pd.DataFrame({'名前': [name],
                           '年齢': [age],
                           '住所': [adress],
                           '連絡先': [phone],
                           'メールアドレス': [mail],
                           '登録日': [date]})
        df1
        print(df1)


        df2 = pd.read_csv(filename,encoding="cp932")

        print(df2)

         
        df3 = pd.concat([df2,df1],axis=0,ignore_index=True)
        print(df3) 
        
        df3.to_csv(filename,index=False,encoding="cp932")

#--------------------------------------------------------------------------

df4 = pd.DataFrame({'名前': [],
                    '年齢': [],
                    '住所': [],
                    '連絡先': [],
                    'メールアドレス': [],
                    '登録日': []})
  
csv = df4.to_csv(index=False) 
b64 = base64.b64encode(csv.encode('utf-8-sig')).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="DB_New.csv">Download Link</a>'

st.markdown(f"レコードファイルのダウンロード（新規開始の場合）:  {href}", unsafe_allow_html=True)

