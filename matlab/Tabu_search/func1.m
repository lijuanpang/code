function F = func1(D,s)%s��һ��n�е�����
DistanV = 0;
n = size(s,2);%size(����1)��ʾ�����������size(����2)��ʾ�����������n=31
for i = 1:(n-1)
    DistanV = DistanV + D(s(i),s(i+1));
end
DistanV = DistanV + D(s(n),s(1));
F = DistanV;
end
    
        