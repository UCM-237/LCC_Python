function U=gauss_jordan(A)
%Esta función realiza  la eliminación de GAUSS-JORDAN, que permite obtener,
%a partir de una matriz dada, una matriz cuyos elementos por encima y 
%debajo de la diagonal son todos cero.

%Obtenemos el número de filas de la matriz..
nf=size(A,1);
U=A;
%
%primera parte: reducción a una matriz triangular pro eliminación
%progresiva
for j=1:nf-1 %recorro todas la columnas menos la última
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
        %última en matlab tengo la suerte de poder manejar cada fila de un 
        %solo golpe.
        U(i,:)=U(i,:)-U(j,:)*U(i,j)/U(j,j);
    end
end


%segunda parte, obtención de una matriz diagonal mediante eliminación
%regresiva, Recorremos ahora las columnas en orden inverso empezando por el
%final... (Eliminación de Gauss Jordan)

for j=nf:-1:2
    for i=j-1:-1:1 %Recorro las filas desde encima de la diagonal hasta la
        %primera, 
        U(i,:)=U(i,:)-U(j,:)*U(i,j)/U(j,j);
    end
end

