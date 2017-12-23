function [p_opt,fval]=mindynprogl(x1,x2,DecisFun,StageObjFun,Stage_TransFun,ObjFun)
M=140;
[k1,k] = size(x1);[k2,k] = size(x2);
x1_isnan=~isnan(x1);
x2_isnan=~isnan(x2);
%f_vub=inf;
f_opt=nan*ones(k1,k2,k);%行与列,f_opt（i,j,m）为第m阶段初状态值为（x1(i,m),x2(j,m)）下的最优质，初值为非数
%t_vubm=inf*ones(k1,k2,k);
d_opt1=f_opt;
d_opt2=f_opt;%(d_opt1(i,j,m),d_opt2(i,j,m))为m阶段初状态值（x1(i,m),x2(j,m)）下的最优决策值，非数
tmp11=find(x1_isnan(:,k));
tmp21=find(x2_isnan(:,k));%找出第k阶段状态值(不是非数)的下标
tmp12=length(tmp11);
tmp22=length(tmp21);
for i=1:tmp12
    for t=1:tmp22
        [u1,u2]=feval('DecisFun',k,x1(tmp11(i),k),x2(tmp21(t),k));
        tmp13=length(u1);
        tmp14=length(u2);
        t_vubm=inf;%%%%%
        %下面两个for语句可求出第k阶段初状态值为xl一(tmpll(i)，k)，x2(tmp21(t)，k)时的最优函数值及最优决策值
        for j=1:tmp13
            for l=1:tmp14
                if u1(j)+u2(l)<=M
                    tmp=feval('StageObjFun',k,x1(tmp11(i),k),x2(tmp21(t),k),u1(j),u2(l));
                    if tmp<=t_vubm %f_vub
                        f_opt(tmp11(i),tmp21(t),k)=tmp;
                        d_opt1(tmp11(i),tmp21(t),k)=u1(j);
                        d_opt2(tmp11(i),tmp21(t),k)=u2(l);
                        t_vubm=tmp;%t_vub=tmp;
                    end
                end
            end
        end
    end
end
for ii=k-1:-1:1
    tmp011=find(x1_isnan(:,ii));
    tmp021=find(x2_isnan(:,ii));
    tmp012=length(tmp011);
    tmp022=length(tmp021);
    for i=1:tmp012
        for t=1:tmp022
            [u1,u2]=feval('DecisFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii));
            tmp013=length(u1);
            tmp014=length(u2);
            t_vubm=inf;%%%
            for j=1:tmp013
                for l=1:tmp014
                    if u1(j)+u2(l)<=M
                        tmp000=feval('StageObjFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii),u1(j),u2(l));
                        tmp100=feval('Stage_TransFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii),u1(j),u2(l));
                        tmp200=x1(:,ii+1)-tmp100(1);
                        tmp300=x2(:,ii+1)-tmp100(2);
                        tmp400=find(tmp200==0);
                        tmp500=find(tmp300==0);
                        if ~isempty(tmp400) & ~isempty(tmp500)
                            if nargin <6
                                tmp000=tmp000+f_opt(tmp400(1),tmp500(1),ii+1);
                            else
                                tmp000=feval('ObjFun',tmp000,f_opt(tmp400(1),tmp500(1),ii+1));
                            end
                            if tmp000<t_vubm %(tmp011(i),tmp021(t),ii)
                                f_opt(tmp011(i),tmp021(t),ii)=tmp000;
                                d_opt1(tmp011(i),tmp021(t),ii)=u1(j);
                                d_opt2(tmp011(i),tmp021(t),ii)=u2(l);
                                t_vubm=tmp000;%(tmp011(i),tmp021(t),ii)=tmp000;
                            end
                        end
                    end
                end
            end
        end
    end
end
fval=f_opt(x1_isnan(:,1),x2_isnan(:,1),1);
p_opt=[];
tmpx1=[];
tmpx2=[];
tmpd1=[];
tmpf=[];
tmpd2=[];
tmp11=find(x1_isnan(:,1));
tmp01=length(tmp11);
tmp12=find(x2_isnan(:,1));
tmp02=length(tmp12);
for i=1:tmp01
    q=(i-1)*k*tmp02;
    for j=1:tmp02
        t=k*(j-1);
        t=q+t;
        tmpd1(i)=d_opt1(tmp11(i),tmp12(j),1);
        tmpd2(j)=d_opt2(tmp11(i),tmp12(j),1);
        %求第一阶段的决策值
        tmpx1(i)=x1(tmp11(i),1);
        tmpx2(j)=x2(tmp12(j),1);%求出第一阶段的状态值
        if tmpd1(i)+tmpd2(j)<=M
            tmpf(i,j)=feval('StageObjFun',1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
            %求出第一阶段的指标函数值
            p_opt(t+1,[1 2 3 4 5 6])=[1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j),tmpf(i,j)];
            for ii=2:k%按顺序求出各阶段的决策值、状态值以及指标函数值
                u=feval('Stage_TransFun',ii-1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
                tmpx1(i)=u(1);
                tmpx2(j)=u(2);
                tmp1=x1(:,ii)-tmpx1(i);
                tmp2=x2(:,ii)-tmpx2(j);
                tmp3=find(tmp1==0);
                tmp4=find(tmp2==0);
                if ~isempty(tmp3) & ~isempty(tmp4)
                    tmpd1(i)=d_opt1(tmp3(1),tmp4(1),ii);
                    tmpd2(j)=d_opt2(tmp3(1),tmp4(1),ii);
                end
                tmpf(i,j)=feval('StageObjFun',ii,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
                p_opt(t+ii,[1 2 3 4 5 6])=[ii,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j),tmpf(i,j)];
            end
        end
    end
end








% function [p_opt,fval]=mindynprogl(x1,x2,DecisFun,StageObjFun,Stage_TransFun,ObjFun)
% %要
% M=200;
% % a1=0:30;
% % b1=0:30;
% % s1=nan*ones(31,1);
% % s1(1)=30;
% % s2=nan*ones(31,1);
% % s2(1)=30;
% % x1=[s1 a1' a1' a1' a1'];%31行4列
% % x2=[s2 b1' b1' b1' b1'];%32行4列
% 
% [k1,k] = size(x1);%31,4
% [k2,k] = size(x2);%32,4
% x1_isnan=~isnan(x1);%NaN的地方为0，其他为1
% x2_isnan=~isnan(x2);
% %f_vub=inf;注释在这儿不动
% f_opt=nan*ones(k1,k2,k);%行与列,f_opt（i,j,m）为第k阶段初状态值为（x1(i,m),x2(j,m)）下的最优质，初值为非数。共4个，每个是31行32列
% % %t_vubm=inf*ones(k1,k2,k);
% d_opt1=f_opt;
% d_opt2=f_opt;%(d_opt1(i,j,m),d_opt2(i,j,m))为m阶段初状态值（x1(i,m),x2(j,m)）下的最优决策值，非数
% tmp11=find(x1_isnan(:,k));%最后一列中所有行位置[1,2,...,31]
% tmp21=find(x2_isnan(:,k));%找出第k阶段状态值(不是非数)的下标,[1...32]
% tmp12=length(tmp11);%行数31，
% tmp22=length(tmp21);
% for i=1:tmp12% i=1:31
%     for t=1:tmp22% t=1:32
%         [u1,u2]=feval('DecisFun',k,x1(tmp11(i),k),x2(tmp21(t),k));%最大状态值带进去得到的决策值范围
%         tmp13=length(u1);%15,下18
%         tmp14=length(u2);
%         t_vubm=inf;%%%%%
%         
%         %下面两个for语句可求出第k阶段初状态值为xl一(tmpll(i)，k)，x2(tmp21(t)，k)时的最优函数值及最优决策值
%         
%         
%         for j=1:tmp13
%             for l=1:tmp14
%                 if u1(j)+u2(l)<=M     
%                     tmp=feval('StageObjFun',k,x1(tmp11(i),k),x2(tmp21(t),k),u1(j),u2(l));%不同的决策值带来的目标值
%                     if tmp<=t_vubm %f_vub
%                         f_opt(tmp11(i),tmp21(t),k)=tmp;
%                         d_opt1(tmp11(i),tmp21(t),k)=u1(j);
%                         d_opt2(tmp11(i),tmp21(t),k)=u2(l);
%                         t_vubm=tmp; %t_vub=tmp;%这里可能有点错误
%                     end
%                 end
%             end
%         end
%         
%     end
% end
% 
%  
%                     
%                         
% %                 tmp=feval('StageObjFun',k,x1(tmp11(i),k),x2(tmp21(t),k),u1(j),u2(l));%不同的决策值带来的目标值
% %                 if tmp<=t_vubm %f_vub
% %                     f_opt(tmp11(i),tmp21(t),k)=tmp;
% %                     d_opt1(tmp11(i),tmp21(t),k)=u1(j);
% %                     d_opt2(tmp11(i),tmp21(t),k)=u2(l);
% %                     t_vubm=tmp; %t_vub=tmp;
% %                 end
% %             end
% %         end
% %     end
% % end
% for ii=k-1:-1:1
%     tmp011=find(x1_isnan(:,ii));%1,2,3列中，之前是最后一列
%     tmp021=find(x2_isnan(:,ii));
%     tmp012=length(tmp011);
%     tmp022=length(tmp021);
%     for i=1:tmp012
%         for t=1:tmp022
%             [u1,u2]=feval('DecisFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii));
%             tmp013=length(u1);
%             tmp014=length(u2);
%             t_vubm=inf;%%%
%             
%             for j=1:tmp013
%                 for l=1:tmp014
%                     
%                     
%                     
%                     % if d1*x1(tmp11(i),k)+d2*x2(tmp21(t),k)>m
%                     if u1(j)+u2(l)<=M
%                         tmp000=feval('StageObjFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii),u1(j),u2(l));
%                         tmp100=feval('Stage_TransFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii),u1(j),u2(l));
%                         tmp200=x1(:,ii+1)-tmp100(1);
%                         tmp300=x2(:,ii+1)-tmp100(2);
%                         tmp400=find(tmp200==0);
%                         tmp500=find(tmp300==0);
%                         if ~isempty(tmp400) & ~isempty(tmp500)
%                             if nargin <6
%                                 tmp000=tmp000+f_opt(tmp400(1),tmp500(1),ii+1);
%                             else
%                                 tmp000=feval('ObjFun',tmp000,f_opt(tmp400(1),tmp500(1),ii+1));
%                             end
%                             if tmp000<t_vubm  %(tmp011(i),tmp021(t),ii)
%                                 f_opt(tmp011(i),tmp021(t),ii)=tmp000;
%                                 d_opt1(tmp011(i),tmp021(t),ii)=u1(j);
%                                 d_opt2(tmp011(i),tmp021(t),ii)=u2(l);
%                                 t_vubm=tmp000;%(tmp011(i),tmp021(t),ii)=tmp000;
%                             end
%                         end
%                     end
%                 end
%                 
%             end
%         end
%     end
% end
%         
% %                     
% %                     tmp000=feval('StageObjFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii),u1(j),u2(l));
% %                     tmp100=feval('Stage_TransFun',ii,x1(tmp011(i),ii),x2(tmp021(t),ii),u1(j),u2(l));
% %                     tmp200=x1(:,ii+1)-tmp100(1);
% %                     tmp300=x2(:,ii+1)-tmp100(2);
% %                     tmp400=find(tmp200==0);
% %                     tmp500=find(tmp300==0);
% %                     if ~isempty(tmp400) & ~isempty(tmp500)
% %                         if nargin <6
% %                             tmp000=tmp000+f_opt(tmp400(1),tmp500(1),ii+1);
% %                         else
% %                             tmp000=feval('ObjFun',tmp000,f_opt(tmp400(1),tmp500(1),ii+1));
% %                         end
% %                         if tmp000<t_vubm%(tmp011(i),tmp021(t),ii)
% %                             f_opt(tmp011(i),tmp021(t),ii)=tmp000;
% %                             d_opt1(tmp011(i),tmp021(t),ii)=u1(j);
% %                             d_opt2(tmp011(i),tmp021(t),ii)=u2(l);
% %                             t_vubm=tmp000;%(tmp011(i),tmp021(t),ii)=tmp000;
% %                         end
% %                     end
% %                 end
% %             end
% %         end
% %     end
% % end
% 
% fval=f_opt(x1_isnan(:,1),x2_isnan(:,1),1);
% p_opt=[];
% tmpx1=[];
% tmpx2=[];
% tmpd1=[];
% tmpf=[];
% tmpd2=[];
% tmp11=find(x1_isnan(:,1));
% tmp01=length(tmp11);
% tmp12=find(x2_isnan(:,1));
% tmp02=length(tmp12);
% for i=1:tmp01
%     q=(i-1)*k*tmp02;
%     
%     for j=1:tmp02
%         t=k*(j-1);
%         t=q+t;
%         tmpd1(i)=d_opt1(tmp11(i),tmp12(j),1);
%         tmpd2(j)=d_opt2(tmp11(i),tmp12(j),1);
%         %求第一阶段的决策值
%         tmpx1(i)=x1(tmp11(i),1);
%         tmpx2(j)=x2(tmp12(j),1);%求出第一阶段的状态值
%         
%         if tmpd1(i)+tmpd2(j)<=M
%             tmpf(i,j)=feval('StageObjFun',1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
%         else
%             tmpf(i,j)=0;
%         end
%         
% 
% 
%         
%         %tmpf(i,j)=feval('StageObjFun',1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
%         %求出第一阶段的指标函数值
%         p_opt(t+1,[1 2 3 4 5 6])=[1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j),tmpf(i,j)];
%         for ii=2:k%按顺序求出各阶段的决策值、状态值以及指标函数值  
%             u=feval('Stage_TransFun',ii-1,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
%             tmpx1(i)=u(1);
%             tmpx2(j)=u(2);
%             tmp1=x1(:,ii)-tmpx1(i);
%             tmp2=x2(:,ii)-tmpx2(j);
%             tmp3=find(tmp1==0);
%             tmp4=find(tmp2==0);
%             if ~isempty(tmp3) & ~isempty(tmp4)
%                 tmpd1(i)=d_opt1(tmp3(1),tmp4(1),ii);
%                 tmpd2(j)=d_opt2(tmp3(1),tmp4(1),ii);
%             end
%             tmpf(i,j)=feval('StageObjFun',ii,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j));
%             p_opt(t+ii,[1 2 3 4 5 6])=[ii,tmpx1(i),tmpx2(j),tmpd1(i),tmpd2(j),tmpf(i,j)];
%         end
%     end
% end
