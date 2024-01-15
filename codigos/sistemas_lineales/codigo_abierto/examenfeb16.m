%%examen final%%%%%

raiz1 =  1.4868 %punto de inicio x0 =1
raiz2 =  2.6189 %punto de inicio x0 = 2.5



xp=linspace(0,3,7)
yp= exp(xp)-2*xp.^2

V = vander(xp)

[l,u,p] = lu(V)
z = progresivas(l,p*yp')
a = regresivas(u,z)

%pinto el polinomio  par aver que va bien la cosa...
x= 0:0.001:3
y = polyval(a,x)
plot(x,y)
hold on
plot(xp,yp,'o')


%derivadas
%adelantada 2 puntos h = 0.5
d1a205= (yp(4) - yp(3))/0.5
%adelantada 2 puntos h = 0.25
d1a2025 = (polyval(a,1.25) - yp(3))/0.25

%centrada 2 puntos h = 0.5

d1c05 = (yp(4) - yp(2))/(2*0.5)
d1c1 = (yp(5) -yp(1))/2


%adelantada de tres puntos

d1a30025 = (-yp(4) +4*polyval(a,1.25) -3*yp(3))/(2*0.25)
d1a3005 = (-yp(5) +4*yp(4) -3*yp(3))/(2*0.5)

%integracion 
 intsimpson =   1.0859
 
 r_exacto = exp(3) -2*3^3/3 -1