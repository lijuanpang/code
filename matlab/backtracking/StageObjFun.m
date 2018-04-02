function f=StageObjFun(k,x1,x2,u1,u2)
p1=30;
p2=20;
m1=30;
m2=30;
c10=10;
c20=7;
c11=5;
c21=3;
b=0.95;
P1=0.5;
P2=0.4;

if x1>0
    c1=u1/x1;
else
    c1=0;
end
if x2>0
    c2=u2/x2;
else
    c2=0;
end

R1=roundn((0.44+1/(2*(1+exp(1-c1+1)))),-2);%7时等于0.94
R2=roundn((0.55+(2/5)/(1+exp(1-c2+1))),-2);%7时等于0.95
% a1=ceil(x1*(1-P1)+x1*P1*R1);
% a2=ceil(x2*(1-P2)+x2*P2*R2);
a1=round(x1*R1);
a2=round(x2*R2);

if a1>m1
    I1=(p1-c10)*a1-(a1-m1)*c11;
else
    I1=(p1-c10)*a1;
end
if a2>m2
    I2=(p2-c20)*a2-(a2-m2)*c21;
else
    I2=(p2-c20)*a2;
end

f=-(I1+I2-u1-u2)*0.95^(k-1);

% if x1>m1
%     I1=(p1-c10)*x1-(x1-m1)*c11;
% else
%     I1=(p1-c10)*x1;
% end
% if x2>m2
%     I2=(p2-c20)*x2-(x2-m2)*c21;
% else
%     I2=(p2-c20)*x2;
% end
% 
% f=-(I1+I2-u1-u2)*0.95^(k-1);

