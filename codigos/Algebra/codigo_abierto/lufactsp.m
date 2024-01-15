function [L,U]=lufact(A)
%este programa calcula una factorizacionLU, de la matrix A,  empleando el método de
%eliminacion gaussiana con pivoteo de filas...
%L es una matriz triangular inferior, U es una matriz triangular superior y
%P es una matriz de permutaciones tal que P*A=L*U

%vamos a aprovechar la potencia de matlab para no evitar algunos buques en
%los calculos..

%primero definimos la matriz de permutaciones como la matriz identidad de
%orden igual al de la matriz A, (si no hay pivoteo de filas la matirz de
%permutaciones es precisamente la identidad)

%Suponnemosdex que la matriz es cuadrada... deberíamos comprobarlo
t=size(A,1); %obtenemos el tamaño de la matriz
P=eye(t);
%Ademas inicializamos a cero las matrices L y U
L=P;
U=A;


%iniciamos un bucle para ir recorriendo las columnas
for j=1:t-1
    LA=zeros(t);
    %Buscamos el elemento mas grande de la columna j
%     maxcol=abs(U(j,j)); 
%     index=j;
%     for i=j:t
%         if abs(U(i,j))>maxcol
%             maxcol=abs(U(i,j));
%             index=i;
%         end
%     end
    
    %ponemos la fila correspondiente la primera
    %Si varias filas comparten en valor más grande, nos quedamos con la
    %primera,
%     Aux=U(j,:);
%     Aux2=P(j,:);
%     Aux3=L(j,1:j-1);
    
    %Reordenamos U (Toda la fila)
%     U(j,:)=U(index,:);
%     U(index,:)=Aux;
    
    %Reordenamos L (Solo los elementos de la fila anteriores a la diagonal
%     L(j,1:j-1)=L(index,1:j-1);
%     L(index,1:j-1)=Aux3;
    
    %modificamos la matriz de permutaciones
%     P(j,:)=P(index,:);
%     P(index,:)=Aux2;
    
   %Calculamos una matriz auxiliar con los factores de las filas a eliminar. 
   LA(j+1:t,j)=U(j+1:t,j)/U(j,j);
   
   %MOdificamos L y U
   L(j+1:t,j)=U(j+1:t,j)/U(j,j)
   U=(eye(t)-LA)*U
   pause
end
