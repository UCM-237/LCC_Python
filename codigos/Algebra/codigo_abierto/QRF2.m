function [Q,R]=QRF2(A)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Calculo de factorizacion QR de la matriz A, mediante la ortogonaliación de
%grand.smitch modificada. Este algoritmo si que es estable...
%Obtenemos las dimensiones de A
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[m,n]=size(A);

%creamos una matriz auxiliar v sobre la que vamos a realizar la
%factorización. Se podría realizar directamente sobre A Machacando sus
%columnas según la factorización progresa... Sería lo correcto para ahorrar
%espacio de almacenamiento. Pero en fin, quizá así queda más claro aunque
%sea menos eficiente.
v=A;
%Como siempre, vamos factorizando por columnas de la matriz A


for i=1:m %la matriz Q tiene que ser mXm, aunque el numero de columnas de A sea n)
    %calculamos cada R(i,i) como el modulo del vector auxiliar v(1:m,i)
    R(i,i)=0;
    for k=1:m
        R(i,i)=R(i,i)+v(k,i)^2;
    end
    R(i,i)=sqrt(R(i,i));
    %calculamos el la columna i de la matriz Q, normalizando la columna i
    %de la matriz v
    for k=1:m
        Q(k,i)=v(k,i)/R(i,i);
    end
    %Modificamos todos los R(i,j) con ij>i, en cuanto tenemos la columna j
    %de la matriz Q, nos basta calcular el producto escalar con las
    %columnas de A (En nuestro caso de v porque están copiadas, de las
    %filas siguientes
    for j=i+1:n
        R(i,j)=0;
        for k=1:m
            R(i,j)=R(i,j)+Q(k,i)*v(k,j);
        end
        %i por último modificamos todas las columnas de la matriz v desde
        %i+1 hasta el final de la matriz. Aqui es donde cambia el algoritmo
        %ya que estamos modificando la matriz A, y las sucesivas matrices V
        %cada vez que obtenemos una nueva fila de valores de R
        for k=1:m
            v(k,j)=v(k,j)-R(i,j)*Q(k,i);
        end
    end
end
