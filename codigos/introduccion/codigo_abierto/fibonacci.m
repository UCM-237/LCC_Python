function s=fibonacci(n)
%obtiene el t�rmino enesimo de la sucesi�n de fibonacci empleando una
%funci�n recursiva. que funcione no quiere decir que sea eficiente...
%n n�mero del t�rmino que se desea obtener

if n<2
    %el valor del t�rmino de fibonacci es �l mismo
    s=n; 
else
    %si n� es la suma de los dos anteriores...
    s=fibonacci(n-1)+fibonacci(n-2);
end   