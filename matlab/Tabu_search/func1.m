function F = func1(D,s)%s是一行n列的数组
DistanV = 0;
n = size(s,2);%size(矩阵，1)表示矩阵的行数；size(矩阵，2)表示矩阵的列数，n=31
for i = 1:(n-1)
    DistanV = DistanV + D(s(i),s(i+1));
end
DistanV = DistanV + D(s(n),s(1));
F = DistanV;
end
    
        