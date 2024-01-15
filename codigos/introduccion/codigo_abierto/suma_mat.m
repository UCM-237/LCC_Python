function s=suma_mat(x,y)
%este programa emplea dos bucles for anidados para obtener la suma de dos
%matrices.

%obtnemos el tamaño de las matrices,
t1=size(x);
t2=size(y);
if t1(1)==t2(1)&& t1(2)==t2(2)
    %si las matrices tienen el mismo tamaño pueden sumarse...
    %construimos una matriz de dicho tamañp para guardar el resultado de
    %la suma
    s=zeros(size(x));
    %construimos un bucle que recorre las filas de ambas matrices
    for i=1:t1(1)
        %i dentro, anidamos un bucle que reorre las columnas
        for j=1:t1(2)
            %Empleando ambos índices para ir sumando los elementos de las
            %dos matrices,
            s(i,j)=x(i,j)+y(i,j);
        end
    end
else
    %si no tienen el mismo tamaño no se pueden sumar...
    disp('las matrices no son del mismo tamaño')
end