function U=eligaussp(A)
%Esta función obtiene una matriz triangular superior, a partir de una
%matriz dada, aplicando el método de eliminación gaussiana.
%realiza piboteo de filas, así que lo primero que hace es comprobar si el
%el elemento de la diagonal, de la fila que se va a emplear para eliminar
%el mayor que los que tiene por debajo en su columna, si no es así,
% intercambia la fila con la que tenga el elemento mayor en dicha columna.

%Obtenemos el número de filas de la matriz..
nf=size(A,1);
U=A;
%
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
