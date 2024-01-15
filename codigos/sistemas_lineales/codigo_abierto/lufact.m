function [L,U,P]=lufact(A)
%este programa calcula una factorizacionLU, de la matrix A,  empleando 
%el método de eliminacion gaussiana con pivoteo de filas...
%L es una matriz triangular inferior, U es una matriz triangular superior y
%P es una matriz de permutaciones tal que P*A=L*U

%vamos a aprovechar la potencia de matlab para evitar algunos buques en
%los calculos..

%primero definimos la matriz de permutaciones como la matriz identidad de
%orden igual al número de filas de la matriz A, (si no hay pivoteo de filas 
%la matriz de permutaciones es precisamente la identidad)

t=size(A,1); %obtenemos el numero de filas de la matriz A
P=eye(t); %Construimos la matriz identidad 
%Ademas, inicializamos las matrices L y U
L=P;
U=A;


%iniciamos un bucle para ir recorriendo las columnas (solo tenemos que
%recorrer tantas columnas como fila - 1 tenga la matriz A
for j=1:t-1
    LA=zeros(t); %Matriz auxiliar (Lambda) de cada iteración.
    %Buscamos el elemento mas grande de la columna j
    maxcol=abs(U(j,j)); 
    index=j;
    for i=j:t
        if abs(U(i,j))>maxcol
            maxcol=abs(U(i,j));
            index=i;
        end
    end
    
    % reordenamos las filas de P, L y U de modo que el valor mas grande de
    % j pase a acupar la diagonal (Esto es equivalente a multiplicar U por
    %la matriz de permetuciones correspondiente, ir calculado
    %iterativamente el valor de la matriz de permutaciones P final, y
    %reordenar las filas ya calculadas de L (aportadas por los valores de
    %las matrices lambdas anteriores... a lambda_j)
    
    Aux=U(j,:);
    Aux2=P(j,:);
    Aux3=L(j,1:j-1);
    
    %Reordenamos U (Toda la fila)
    U(j,:)=U(index,:);
    U(index,:)=Aux;
    
    %Reordenamos L (Solo los elementos de la columnas anteriores...situados
    %por debajo de la diagonal).
    L(j,1:j-1)=L(index,1:j-1);
    L(index,1:j-1)=Aux3;
    
    %modificamos la matriz de permutaciones
    P(j,:)=P(index,:);
    P(index,:)=Aux2;
    
   %Calculamos una matriz auxiliar con los factores de los elementos
   %a eliminar. 
   LA(j+1:t,j)=U(j+1:t,j)/U(j,j); %estos elementos son directamente los que 
   %se añaden a la matriz L
   %Modificamos L y U
   L(j+1:t,j)=U(j+1:t,j)/U(j,j);
   U=(eye(t)-LA)*U; %la expresión eye(t)-LA nos permite cambiar de signo los
   %elementos situados por debajo de la diagonal principal...
end
