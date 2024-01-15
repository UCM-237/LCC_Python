function U=gauss_jordan(A)
%Esta funci�n realiza  la eliminaci�n de GAUSS-JORDAN, que permite obtener,
%a partir de una matriz dada, una matriz cuyos elementos por encima y 
%debajo de la diagonal son todos cero.

%Obtenemos el n�mero de filas de la matriz..
nf=size(A,1);
U=A;
%
%primera parte: reducci�n a una matriz triangular pro eliminaci�n
%progresiva
for j=1:nf-1 %recorro todas la columnas menos la �ltima
%%%%%%%%%%%pivoteo de filas%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
    %Buscamos el elemento mayor de la columna j de la diagonal para abajo
    maxcol=abs(U(j,j));
    index=j;
    for l=j:nf
        if abs(U(l,j))>maxcol
            maxcol=abs(U(l,j));
            index=l;
        end
    end
    %si el mayor no era el elemento de la diagonal U(j,j), intecambiamos la
    %fila l con la fila j
    if index~=j
        aux=U(j,:);
        U(j,:)=U(index,:);
        U(index,:)=aux;
    end
%%%%%%%%fin del pivoteo de filas%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
    for i=j+1:nf %Recorro las filas desde debajo de la diagonal hasta la 
        %�ltima en matlab tengo la suerte de poder manejar cada fila de un 
        %solo golpe.
        U(i,:)=U(i,:)-U(j,:)*U(i,j)/U(j,j);
    end
end


%segunda parte, obtenci�n de una matriz diagonal mediante eliminaci�n
%regresiva, Recorremos ahora las columnas en orden inverso empezando por el
%final... (Eliminaci�n de Gauss Jordan)

for j=nf:-1:2
    for i=j-1:-1:1 %Recorro las filas desde encima de la diagonal hasta la
        %primera, 
        U(i,:)=U(i,:)-U(j,:)*U(i,j)/U(j,j);
    end
end

