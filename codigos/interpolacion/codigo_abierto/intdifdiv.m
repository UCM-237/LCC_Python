function y=intdifdiv(x,xp,yp)
%Esta funci�n calcula el valor del polinomio de diferencias divididas que 
%interpola los puntos (xp,yp) el el punto, o %los puntos contenidos en x. 
%Empleando las funciones, difdiv, para calcular los coeficientes del
%polinomio y evdif para evaluarlo

%llamamos a difdiv
a=difdiv(xp,yp);
 
 %y a continuaci�n llamamos a evdif
  y=evdif(a,xp,x);