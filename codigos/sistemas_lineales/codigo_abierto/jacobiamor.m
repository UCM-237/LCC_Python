function [ x,it,tolf] =jacobiamor(A,b,tol,maxiter,w,gr)
%uso[ x,it,tolf] =jacobi(A,b,tol,maxiter,w)
%esta función resuleve un sistema lineal de dimension arbitraria n por el
%metodo de jacobi amortiguado.
%las variables de entrada son, A: matriz de coeficientes del sitema, b:
%vector columna de terminos independientes, tol: tolerancia por debajo de
%la cual se considera que la solucion alcanzada es valida, maxiter: numero
%maximo de iteraciones que se permite ejecutar al algoritmo sin encontrar
%la solución, w: factor de amortiguamiento, gr si se incluye esta variable, 
%con un valor cualquiera, el programa va pintando la evolución de la 
%diferencia entre dos soluciones sucesivas.
%las variables de salida son x: vector de soluciones, it numero de
%iteraciones empleado para obtener la solución, tolf diferencia entre dos
%soluciones, (se de como estima de la precisión o el error cometido.

%obtenemos el tammaño del sistema,

n=size(A,1);
%creamos un vector de soluciones inicial,
x0=zeros(n,1);
%igualamos el vector sobre el que vamos a iterar al vector de términos
%independientes
x=b;
%calculamos una primera iteración antes de entrar en el bucle,
for i=1:n %bucle para recorrer todas las ecuaciones
    for j=1:i-1 %restamos la contribucion de todas las incognitas
        x(i)=x(i)-A(i,j)*x0(j);     %por encima de x(i)
    end
    for j=i+1:n %restamos la contribución de todas las incognitas
        %por debajo de x(i)
        x(i)=x(i)-A(i,j)*x0(j);
    end
    %dividimos por el elemento de la diagonal,
    x(i)=x(i)/A(i,i);
end
%amortiguamos
x=w*x+(1-w)*x0;

%calculamos la diferencia entre las dos soluciones,
tolf=norm(x-x0);
vtolf=tolf;
%ponemos a 1 el contador de iteraciones.
it=1;

%si hay que pintar, pintamos (mejor sería si hay que pintar hacer separar
%TODOS los calculos desde el principio pero en fin... asi es menos
%eficiente pero mas sencillo.

if nargin==5
    plot(it,tolf,'^r')
    hold on
end

%bucle principal... se permanece en el salvo que se obtenga una diferencia
%entre soluciones consecutivas menor que la tolerancia tol, o se haya
%superado el numero maximo de iteraciones permitido

while (tolf>tol)&&(it<maxiter)
    %volvemos a repetir una y otra vez el calculo de una iteración
    x0=x;
    %volvemos a inicializar el vector de soluciones al valor de los
    %terminos independientes
    x=b;
    for i=1:n %bucle para recorrer todas las ecuaciones
        for j=1:i-1 %restamos la contribucion de todas las incognitas
            x(i)=x(i)-A(i,j)*x0(j);       %por encima de x(i)
        end
        for j=i+1:n %restamos la contribución de todas las incognitas
            %por debajo de x(i)
            x(i)=x(i)-A(i,j)*x0(j);
        end
        %dividimos por el elemento de la diagonal,
        x(i)=x(i)/A(i,i);
    end
    %amortiguamos la solución...
    x=w*x+(1-w)*x0;
   
    %calculamos la diferencia entre las dos soluciones,
    tolf=norm(x-x0);
    vtolf=[vtolf tolf];
    %incrementamos el contador de iteraciones
    it=it+1;
    %si hay que pintar, pintamos
    
    if nargin==5
        plot(it,tolf,'^r')
        hold on
    end
    
end
plot(1:it,vtolf,'^r')
