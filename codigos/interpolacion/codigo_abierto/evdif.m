function y=evdif(a,x,x1)
%esta función obtiene el valor de un polinomio de diferencias divididas a
%partir de los coeficientes (a) del polinomio, los puntos (x) sobre los que
%se ha calculado el polinomio y el punto o vector de puntos (x1) para el
%que se quiere calcular el valor que toma el polinomio.

%obtenemos el tamaño del vector de coeficientes del polinomio,

n=length(a);

%Construimos un bucle para calcular el valor del polinomio,
y=a(1);
for k=1:n-1
    %calculamos el valor del producto de los binomios que multiplican al
    %coeficiente i
    binprod=1;
    for j=1:k
        binprod=binprod.*(x1-x(j));
    end
    y=y+a(k+1)*binprod;
end
