function s=Stage_TransFun(k,x1,x2,u1,u2)
P1=0.5;
P2=0.4;
% n1=P1*x1;
% n2=P2*x2;
% n1=ceil(P1*x1);%%
% n2=ceil(P2*x2);
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
R1=roundn((0.44+1/(2*(1+exp(1-c1+1)))),-2);%6.时等于0.94
R2=roundn((0.55+(2/5)/(1+exp(1-c2+1))),-2);%7时等于0.95
s(1)=round(x1*R1);
s(2)=round(x2*R2);

% 
% 
% %s(1)=x1-u1;s(2)=x2-u2;

% function s=Stage_TransFun(k,x1,x2,u1,u2)
% s(1)=x1-u1;s(2)=x2-u2;