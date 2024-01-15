function [ x,it,tolf] =jacobiamor_matriz(A,b,tol,maxiter,w,gr)
%uso[ x,it,tolf] =jacobi(A,b,tol,maxiter)
%esta funci�n resuleve un sistema lineal de dimension arbitraria n por el
%metodo de jacobi empleando matrices en lugar de bucles para el calculo de 
%las iteraciones.
%las variables de entrada son, A: matriz de coeficientes del sitema, b:
%vector columna de terminos independientes, tol: tolerancia por debajo de
%la cual se considera que la solucion alcanzada es valida, maxiter: numero
%maximo de iteraciones que se permite ejecutar al algoritmo sin encontrar
%la soluci�n, gr si se incluye esta variable, con un valor cualquiera, el
%programa va pintando la evoluci�n de la diferencia entre dos soluciones
%sucesivas.
%las variables de salida son x: vector de soluciones, it numero de
%iteraciones empleado para obtener la soluci�n, tolf diferencia entre dos
%soluciones, (se de como estima de la precisi�n o el error cometido.

%obtenemos el tama�o del sistema,

n=size(A,1);
%creamos un vector de soluciones inicial,
x0=zeros(n,1);
%creamos las matrices del m�todo
D=diag(diag(A));
U=A-tril(A);
L=A-triu(A);
I=eye(n);
%ALternativamente para jacobi podemos crear una solo matriz equivalenta a
%L+U, LpU=A-D
f=w*D^-1*b;
H=-w*D^-1*(L+U)+(1-w)*I;

%calculamos la primera iteraci�n,
x=f+H*x0;

%calculamos la diferencia entre las dos soluciones,
tolf=norm(x-x0);
%ponemos a 1 el contador de iteraciones.
it=1;

%si hay que pintar, pintamos (mejor ser�a si hay que pintar hacer separar
%TODOS los calculos desde el principio pero en fin... asi es menos
%eficiente pero mas sencillo.

if nargin==5
    plot(it,tolf,'.')
    hold on
end

%bucle principal... se permanece en el salvo que se obtenga una diferencia
%entre soluciones consecutivas menor que la tolerancia tol, o se haya
%superado el numero maximo de iteraciones permitido

while (tolf>tol)&&(it<maxiter)
    %volvemos a repetir una y otra vez el calculo de una iteraci�n
    x0=x;
    x=f+H*x0;
     %calculamos la diferencia entre las dos soluciones,
        tolf=norm(x-x0);
        %incrementamos el contador de iteraciones
        it=it+1;
        %si hay que pintar, pintamos 
        
        if nargin==5
            plot(it,tolf,'.')
            hold on
        end
  
end

