function [c,yi]=spcubic(x,y,xi)
%uso [c,yi]=spcubic(x,y,xi)
%Esta función interpola los puntos contenidos en los vectores columna x e y
%empleando parae ello splines cúbicos naturales. devuelve los coeficientes
%de los polinomios en una matriz de dimension (n-1)*4. Cada fila contiene
%un splin desde So a Sn-1 los coeficiente están guardados el la fila en
%orden depotencia creciente: ejemplo c(i,1)+c(i,2)*x+c(i,3)*x^2+c(i,4)*x^3
%ademas devuelve los valores interpolados yi correspondientes a puntos xi
%contenidos en el intervalo definido por los valores de x

%obtenemos la longitud de los datos...
l=length(x);
%obtencion de los coeficientes M
%Construimos el vector de diferencias h y un vector de diferencias
%Dy=y(i+1)-y(i) Que nos será muy útil a la hora de calcular el vector de
%términos independientes del sistema

for i=1:l-1
    h(i)=x(i+1)-x(i);
    Dy(i)=y(i+1)-y(i);
end

%Construimos la matriz del sistema. (Lo ideal seria definirla como una
%matriz sparse pero en fin no sabeis, porque sois todavía pequeños, etc...)

CSP(l-2,l-2)=2*(h(l-2)+h(l-1));
b(l-2,1)=6*(Dy(l-1)/h(l-1)-Dy(l-2)/h(l-2));
for i=1:l-3
    CSP(i,i)=2*(h(i)+h(i+1));
    CSP(i,i+1)=h(i+1);
    CSP(i+1,i)=h(i+1);
    b(i,1)=6*(Dy(i+1)/h(i+1)-Dy(i)/h(i));
end

%calculamos los coeficientes M,
M=CSP\b;

%Añadimos el primer y el último valor como ceros (Splines naturales)
M=[0;M;0];

%calulamos los coeficientes A,
for i=1:l-1
    A(i)=Dy(i)/h(i)-(M(i+1)-M(i))*h(i)/6;
end
%Calculamos los coeficientes B,
for i=1:l-1
    B(i)=y(i)-M(i)*h(i)^2/6;
end
%Podemos ahora calcular el valor que toma el polinomio para los puntos
%que se desea interpolar

%miramos cuantos puntos tenemos
l2=length(xi);
for i=1:l2
    %miramos en que intervalo esta el punto xi(i)
    j=1;
    while xi(i)>x(j)
        j=j+1;
    end
    if j>l-1
        j=l-1; %aunque estamos extrapolando
    elseif j<2
        j=2; %estamos calculando el primer punto o estamos tanbien
        %extrapolando
    end
    
    yi(i)=-M(j-1)*(xi(i)-x(j))^3/(6*h(j-1))+...
        M(j)*(xi(i)-x(j-1))^3/(6*h(j-1))+A(j-1)*(xi(i)-x(j-1))+B(j-1);
end

%calcumos los coeficientes c del spline en forma 'normal'
%la primera columna, son los valores de i,
c=zeros(l-1,4);
for i=1:l-1
    c(i,1)=y(i);
    c(i,2)=Dy(i)/h(i)-M(i)*h(i)/3-M(i+1)*h(i)/6;
    c(i,3)=M(i)/2;
    c(i,4)=(M(i+1)-M(i))/(6*h(i));
end
