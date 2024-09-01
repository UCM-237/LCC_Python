function a=mc(x,y,n,w)
%uso: a=mc(x,y,n,w). Esta función permite obtener los coeficientes del
%polinomio de mínimos cuadrados que ajusta un conjunto de datos. Las
%variables de entrada son: x, vector con la componente x de los datos a
%ajustar. y, vector con la componente y de los datos a ajustar. n grado del
%polinomio de interpolación. w vectos de pesos asociados a los datos. si no
%se sumininstra se toman todos los pesos como 1. Saidas: vector columna con
%los coeficientes del polinomio=> a(1)+a(2)*x+a(3)*x^2+a(n+1)*x^n

%comprobamos en primer lugar que tenemos datos suficientes,

m=length(x);
if m<n+1
    error('no hay datos sufiecientes para calcular el polinomio pedido')
end
%Si no se ha suministrado vector de pesos construimos uno formado por unos,

w=ones(m,1);

%Montamos un bucle para crear los elementos s de la matriz de coeficientes,
for j=1:2*n+1
    s(j)=0;    
for i=1:m
    s(j)=s(j)+w(i)*x(i)^(j-1);
end
end


%y un segundo bucle para crear los términos independientes...
for j=1:n+1
    c(j,1)=0;
    for i=1:m
        c(j,1)=c(j,1)+w(i)*x(i)^(j-1)*y(i)
    end
end

% a partir de los valores de s, construimos la matriz del sistema,
for i=1:n+1
    for j=1:n+1
        A(i,j)=s(i+j-1)
    end
end

%solo nos queda resolver el sistema... Empleamos la division por la
%izquierda de matlab

a=A\c;