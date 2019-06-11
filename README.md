

# 인간공학적인 자동차 칵핏 설계를 위한 신체계측치 분석

학과 | 학번 | 성명
---- | ---- | ---- 
산업공학과 |201227540|이동준


## 프로젝트 개요
   본인의 전공인 산업공학과의 인간공학 과목에서 자동차 칵핏에서의 한 가지를 인간공학적인 요소를 고려하여 설계하는 과제가 있었다. 카시트 디자인을 하기로 결정하고 한국인에게 가장 맞는 사이즈의 카시트 설계를 하고자 했다. 수업에서 배운 바로는 설계하는 과정에서 대부분의 사용자 타겟이 이용할 수 있게 설계하는 것이 무엇보다도 중요하므로 95 percentile, 99 percentile과 minimum, maximum 값을 찾는 것이 가장 중요하다. 따라서 이 데이터을 찾는 프로그램을 만들어 보고자 했다. 자동차의 경우에는 모든 연령의 사람들이 이용하므로 전체 연령대의 신체계측치를 이용하였다. 이는 한국인 인체치수를 측정한 데이터를 통해 찾을 수 있을 것 같아서 파이썬과 pandas를 통해 분석해보기로 했다. 
   
## 프로그램 흐름
   1. SizeKorea(한국인인체치수조사) 사이트에서 2015년 제 7차 신체 측정 데이터 파일을 받아온다.
   2. 파이썬에서 pandas를 이용하여 입력받은 후 알고자 하는 데이터 이름과 percentile을 입력한다.
   3. 그 후 입력된 percentile에 해당하는 데이터 값과 그래프를 출력한다.
![map.png](흐름도.png)

## 사용한 공공데이터 
[데이터보기](https://github.com/dongjuuun/p2019/blob/master/%EC%8B%A0%EC%B2%B4%EC%A7%81%EC%A0%91%EC%B8%A1%EC%A0%95%20%EB%8D%B0%EC%9D%B4%ED%84%B03.csv)

## 소스
* [링크로 소스 내용 보기]
https://github.com/dongjuuun/p2019/blob/master/last_code.py



* 코드 삽입

~~~python
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
 ~~~
