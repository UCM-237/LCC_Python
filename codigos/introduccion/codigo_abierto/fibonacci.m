function s=fibonacci(n)
%obtiene el término enesimo de la sucesión de fibonacci empleando una
%función recursiva. que funcione no quiere decir que sea eficiente...
%n número del término que se desea obtener

if n<2
    %el valor del término de fibonacci es él mismo
    s=n; 
else
    %si nó es la suma de los dos anteriores...
    s=fibonacci(n-1)+fibonacci(n-2);
end   