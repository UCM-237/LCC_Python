function [a,y1]=newgre(x,y,x1)
%USO: [a,y1]=newgre(x,y,x1)
%este polinomio permite obtener los coeficientes del polinomio de
%newton-gregory que interpola los datos contenidos en los vectores x
%e y. Da como resultado un vector fila a con los coeficientes, si se le dan
%adema un punto o vector de puntos calcula los valores que toma el
%polinomio en dichos puntos.

%miramos cuantos datos tenemos
n=length(x);

%inicializamos el vector de coeficientes con las diferencias de orden 0, es
%decir los valores de y,
a=y;
h=x(2)-x(1);

%y ahora montamos un bucle, si tenemos n datos debemos calcular n
%diferencias, como ya tenenos la primera, iniciamos el bucle en 2,
for j=2:n
    %en cada iteración calculamos las diferencias de un orden superior,
    %como solo nos vale la primera diferencia de cada orden empezamos el
    %bucle interior en el valor del exterior j
    for i=j:n
        %ahora basta dividir en todos los casos por la distancia h
        %multiplicada por el orden de la diferencia
        a(i)=(a(i)-y(i-1))/((j-1)*h);
    end
    %volvemos acopiar en y las diferencias obtenidas para emplearlas en la
    %siguiente iteracion
    y=a;
    
end
y1=[];
if nargin==3
    %Construimos un bucle para calcular el valor del polinomio,
    y1=a(1);
    for k=1:n-1
        %calculamos el valor del producto de los binomios que multiplican al
        %coeficiente i
        binprod=1;
        for j=1:k
            binprod=binprod.*(x1-x(j));
        end
        y1=y1+a(k+1)*binprod;
    end
end