# Program to write a  transpose a matrix using a nested loop

X = [[42,18],
    [15,13],
    [36,28]]

res = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       res[j][i] = X[i][j]

for r in res:
   print(r)
