import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

with open('C:\\Users\movejun\Desktop\학교\신체직접측정 데이터3.csv','rt', encoding='UTF8') as f:
    data =f.readline()
    print('######데이터목록#####')
    print(data)
    while 1:
        selected_column = input("찾고자 하는 데이터를 입력하세요: ")
        percentile_num = int(input("percentile수를 입력하세요"))/100

        df = pd.read_csv('C:\\Users\movejun\Desktop\학교\신체직접측정 데이터3.csv')
        column_df = df[selected_column]

        print("--------------------------------")
        print('데이터 종류 :', selected_column)
        print("입력된 percentile에 맞는 데이터값 :" , column_df.quantile(percentile_num))
        print("--------------------------------")
        print(column_df.describe())
        np.warnings.filterwarnings('ignore')

        order = int(input("그래프로 보시겠습니까? YES: : 1, NO : 0"))
        if order == 1 :
            n, bins, patches = plt.hist(column_df, bins =10)
            plt.title(selected_column)
            plt.show()
        else:
            continue


