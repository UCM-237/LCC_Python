function s=suma_while(x,y)
%este programa emplea dos bucles while anidados para obtener la suma de dos
%matrices.

%obtenemos el tamaño de las matrices,
t1=size(x);
t2=size(y);
if t1(1)==t2(1)&& t1(2)==t2(2)
    %si las matrices tienen el mismo tamaño pueden sumarse...
    %construimos una matriz de dicho tamañp para guardar el resultado de
    %la suma
    s=zeros(size(x));
    %construimos un bucle que recorre las filas de ambas matrices
    i=1; %inicimos un contador para las filas
    while i<=t1(1)
        %y dentro, anidamos un bucle que reorre las columnas
        j=1; %iniciamos un contador para las columnas
        while j<=t1(2)
            %Empleando ambos índices para ir sumando los elementos de las
            %dos matrices,
            s(i,j)=x(i,j)+y(i,j);
            j=j+1; %vamos incrementando el indice de columnas
        end
        i=i+1; %vamos incrementando el indice de filas
    end
else
    %si no tienen el mismo tamaño no se pueden sumar...
    disp('las matrices no son del mismo tamaño')
end