function [Q,R]=QRF1(A)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Factorización QR obtenida directamente por ortogonalización de grand-smith
%Ojo, el algoritmo es inestable... Con lo que la bondad de las soluciones
%dependera de la matriz que se quiera factorizar.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%En primer lugar obtenemos las dimensiones de la matriz
[m,n]=size(A);

%fatorizamos columna a columna
for j=1:n
    %Construimos un vector auxiliar v, nos servira para ir obteniendo las
    %columnas de la matriz Q.
    for i=1:m %Solo llegamos hasta m factorización incompleta si m>n
        v(i)=A(i,j)
    end
    for i=1:j-1
        %obtenemos los elementos de la matriz R, correspondientes a la
        %columna j, solo podemos construir hasta una fila antes de la
        %diagonal i=j-1. cada fila es el producto escalar de la columna i
        %de la matriz Q for la columna j de la Matriz A.
        R(i,j)=0
        for k=1:m
        R(i,j)=R(i,j)+Q(k,i)*A(k,j)
        end
        
        %obtenemos las componentes del vector auxiliar que nos permitira
        %construir la columna j de la matriz Q
        for k=1:m
            v(k)=v(k)-R(i,j)*Q(k,i)
        end
    end
    %Obtenemos el valor del elemento de la diagonal R(j,j) de la matriz R

    R(j,j)=0
    for k=1:m
        R(j,j)=R(j,j)+v(k)^2
    end
    R(j,j)=sqrt(R(j,j))
    
    %Y por último, divimos los elementos del vector v por R(j,j), para
    %obtener la columna j de la matriz Q
    for k=1:m
        Q(k,j)=v(k)/R(j,j)
    end
end
%trabajar en matlab empleando bucles, no es una buena idea, se pierde toda
%la potencia de matlab. Pero al menos permite trabajar con bucles.
%(Modificar el programa empleando el mínimo numero posible de bucles). La
%factorizació solo vale para matrices que tengan n>=m. en otro caso,
%tendríamos que elegir expandir la matriz Q con (m-n) vectores ortogonales
%que ya no podemos obtener por factorización...  Lo mismo pasa si la matriz
%tiene rango completo.. rang(A)=m. Factoriza pero sale un factor cero y
%todo muy pero que muy mal...