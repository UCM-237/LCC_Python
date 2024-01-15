function x = regresivas(A,b)
%uso: x=regresivas(A,b)
%Esta Función permite obtener la solucion de un sistema triangular superior
%empleando sustituciones regresivas. La variables de entrada son la matriz
%de coeficientes A  y el vector de terminos independientes b. la solucion se
%devuelve como un vector columna en la varible x.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Obtenemos el tamaño de la matriz de coeficientes y comprobamos que es
%cuadrada,
[f,c]=size(A);
if f~=c
    error('la matriz de coeficientes no es cuadrada')
end
%construimos un vector solucion, inicialmente formados por ceros,
x=zeros(f,1);
%construimos un bucle for para ir calculando regresivamente las soluciones
%del sistema
for i=f:-1:1
    %primero igualamos la solución al termino independiente de la ecuación
    %que toque...
    x(i)=b(i);
    %y luego creamos un bucle para ir restando todas las soluciones
    %posteriores... (Este bucle se puede tambien hacer hacia delante:
    %j=i+1:f
    for j=f:-1:i+1
    x(i)=x(i)-A(i,j)*x(j);
    end
    %para terminar dividimos por el elemento de la diagonal de la matriz de
    %coeficientes...
    x(i)=x(i)/A(i,i);
end

