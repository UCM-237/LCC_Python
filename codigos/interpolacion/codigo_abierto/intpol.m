y=3*x.^2+2*x;
y=y+10-20*rand(size(y));
x1=[1:0.05:10]; [a,y1]=newgre(x,y,x1);
plot(x,y,'or')
hold on
plot(x1,y1)