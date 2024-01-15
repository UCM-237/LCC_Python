function U=eligauss(A)
%Esta funci�n obtiene una matriz triangular superior, a partir de una
%matriz dada, aplicando el m�todo de eliminaci�n gaussiana.
%No realiza piboteo de filas, as� que si alg�n elemento de la diagonal de A
%queda cero o proximo a cero al ir eliminado dar� problemas...

%Obtenemos el n�mero de filas de la matriz..
nf=size(A,1);
U=A
%
for j=1:nf-1 %recorro todas la columnas menos la �ltima
    for i=j+1:nf %Recorro las filas desde debajo de la diagonal hasta la �ltima
        %en matlab tengo la suerte de poder manejar cada fila de un solo
        %golpe.
        U(i,:)=U(i,:)-U(j,:)*U(i,j)/U(j,j)
    end
end
    