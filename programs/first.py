#Printing spiral matrix

a = [[3],[2]]

max_ele = len(a) * len(a[1])
# print(max_ele)

max_row = len(a)
max_col = len(a[0])
max_ele = max_row*max_col
num_ele = 0

jth_col = 0
ith_row = 0

min_row = 0
min_col = 0

while (num_ele<=max_ele):
    # print("\nNew cycle\n")

    ith_row=min_row

    # row -> foward
    while jth_col<max_col:
        print(a[ith_row][jth_col],end = " ")
        jth_col+=1
        num_ele+=1

    # col -> downward
    ith_row+=1
    while (ith_row<max_row):
        print(a[ith_row][jth_col-1],end = " ")
        ith_row+=1
        num_ele+=1

    # row -> backward
    ith_row-=1
    jth_col-=2
    while (jth_col>=min_col):
        print(a[ith_row][jth_col],end = " ")
        jth_col-=1
        num_ele+=1
    
    #col -> upward

    jth_col+=1
    ith_row-=1

    while (ith_row>min_row):
        print(a[ith_row][jth_col],end = " ")
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
    
print()