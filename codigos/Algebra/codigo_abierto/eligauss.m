function U=eligauss(A)
%Esta función obtiene una matriz triangular superior, a partir de una
%matriz dada, aplicando el método de eliminación gaussiana.
%No realiza piboteo de filas, así que si algún elemento de la diagonal de A
%queda cero o proximo a cero al ir eliminado dará problemas...

%Obtenemos el número de filas de la matriz..
nf=size(A,1);
U=A
%
for j=1:nf-1 %recorro todas la columnas menos la última
    for i=j+1:nf %Recorro las filas desde debajo de la diagonal hasta la última
        %en matlab tengo la suerte de poder manejar cada fila de un solo
        %golpe.
        U(i,:)=U(i,:)-U(j,:)*U(i,j)/U(j,j)
    end
end
    