# 案例12:99乘法口诀表(扩展)
"""
1*1 = 1
1*2 = 2   2*2 = 4
1*3 = 3   2*3 = 6   3*3 = 9
1*4 = 4   2*4 = 8   3*4 = 12   4*4 = 16
.....
1*9 = 9   2*9 = 18  3*9 = 27   4*9 = 36   5*9 = 45   6*9 = 54   7*9 = 63
"""
for k in range(1, 10):            # k  1~9
    for y in range(1, k+1):       # y  1~9
        print(f'{y}*{k}={k * y}', end="\t")
    print()                       # 换行
"""
          k y   
k=1  y=1  1*1=1  
     y=2  1*2=2
     y=3  1*3=3
     ....
     y=9  1*9=9
----------------------------------
k=2  y=1  2*1=2
     y=2  2*2=4
     y=3  2*3=6
     ....
     y=9  2*9=19  
----------------------------------
k=3
....
k=9
"""




