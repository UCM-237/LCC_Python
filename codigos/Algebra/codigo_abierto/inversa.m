function B=inversa(A)
%este programa calcula la inversa de una matriz a partir de definici�n
%t�pica: A^(-1)=[adj(A)]'/det(A)
%Se ha includo al final del programa una funcion (determinante) para 
%calcular determinantes
%Todo el programa es MUY INEFICIENTE. El �nico interes de esto es ense�ar que
%las estructuras basicas de programacion funcionan, y como se majenan las
%llamadas a funciones en matlab etc.


%Lo primero que hacemos es comprobar si la matriz es cuadrada
%primero comprobamos que la matriz suministrada es cuadrada:
[a,b]=size(A);
if a~=b
    disp('la matriz no es cuadrada, Campe�n')
    B=[];
else
    %calculamos el determinante de A, si es cero hemos terminado
    dA=determinante(A)
    if dA==0
        %deber�amos condicionar en lugar de comparar con cero, los errores
        %de redondeo pueden matarnos.... Si el determinante es proximo a
        %cero
         disp('la matriz es singular, la pobre')
      B=[]  
    else
    
    %Calculamos el cofactor de cada t�mino de A mediante un doble bucle.
    for i=1:a
        for j=1:b
            %Construimos el menor correspondinste al elemento (i,j)
            m=A([1:i-1 i+1:a],[1:j-1 j+1:b])
            %calculamos el cofactor llamando a la funci�n determinante
            %lo ponemos ya en la posici�n que corresponderia a la matriz 
            %transpuesta de la adjunta.
            B(j,i)=(-1)^(i+j)*determinante(m)
        end
    end
    %Terminamos la operacion dividiendo por el determinante de A
    B=B/dA
    end
end
end
function d=determinante(M)
%este programa, calcula el determinante de una matriz empleando la formula
%de Laplace. La funci�n es recursiva, (se llama a si misma sucesivamente
%para calcular los cofactores necesarios). Desarrolla siempre por los
%elementos de la primera columna. (Es un prodigio de infeciencia numerica,
%pero permite manejar bucles y funciones recursivas, asi que supongo que
%puede ser �til para los que empiezan a programar).
%un posible ejercicio para ver lo malo que es el m�todo, consiste ir
%aumentando la dimension de la matriz y comparar lo que lo tarde en
%calcular el determinante con lo que tarda la funci�n de matlab det...

%primero comprobamos que la matriz suministrada es cuadrada:
d=0;
[a,b]=size(M);
if a~=b
    print('la matriz no es cuadrada, Campe�n')
    d=[];
else
    for i=1:a
        if a==1
            d=M;
        else
            %Elimminamos la fila y columna que toque
            N=M([1:i-1 i+1:a],2:b);
            %A�adimos el calculo correspondiente al cofactor
            d=(-1)^(i+1)*M(i,1)*determinante(N)+d;
            %pause
        end
    end
end
end
            