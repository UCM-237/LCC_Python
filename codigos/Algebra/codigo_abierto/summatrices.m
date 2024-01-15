function suma=summatrices(A,B)
%Programa que suma matrices empleando un sencillo bucle
%suma=summatrices(A,B)
%A y B deben ser matrices del mismo orden, si no dará un error,
%suma devuelve el resultado de la suma de las dos matrices


%Comprobamos si las matrices coinciden en tamaño para hacer la suma

if size(A)==size(B)
    %construimos un par de bucles para ir recorriendo las matrices
    for i=1:size(A,1)
        for j=1:size(A,2)
            suma(i,j)= A(i,j)+B(i,j);
        end
    end
else
    %no coinciden las dimensiones, luego no se pueden sumar
    error('debe coincidir el orden da las matrices')
end