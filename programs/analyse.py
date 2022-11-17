#Printing spiral matrix

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

max_ele = len(a) * len(a[1])
# print(max_ele)

flag = True
max_row = len(a)
max_col = len(a[0])

if (max_row!=max_col):
    flag = False

max_ele = max_row*max_col
num_ele = 0

jth_col = 0
ith_row = 0

min_row = 0
min_col = 0

result = []

while (num_ele<=max_ele):
    # print("\nNew cycle\n")

    ith_row=min_row

    # row -> foward
    while jth_col<max_col:
        result.append(a[ith_row][jth_col])
        jth_col+=1
        num_ele+=1

    # col -> downward
    ith_row+=1
    while (ith_row<max_row):
        result.append(a[ith_row][jth_col-1])
        ith_row+=1
        num_ele+=1

    # row -> backward
    ith_row-=1
    jth_col-=2
    while (jth_col>=min_col):
        result.append(a[ith_row][jth_col])
        jth_col-=1
        num_ele+=1
    
    #col -> upward

    jth_col+=1
    ith_row-=1

    while (ith_row>min_row):
        result.append(a[ith_row][jth_col])
        ith_row-=1
        num_ele+=1

    min_row+=1
    min_col+=1
    max_col-=1
    max_row-=1
    jth_col+=1

    if num_ele==max_ele:
        break

    # print(min_row,min_col)

    # print("cycle ends... " + str(min_row)+" "+str(min_col)+"\n")

if (flag):
    print(result)
else:
    print(result[:len(result)-1])