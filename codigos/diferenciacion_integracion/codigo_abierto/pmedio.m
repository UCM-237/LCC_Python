function y=pmedio(fun,ya,a,b,h)
%metodo de rungekutta de segundo orden mas conocido como del punto medio
%uso: y=pmedio(fun,ya,a,b,h)
% variables de entrada: fun, nombre entre comillas de la función que define
% el problema de valor inicial que se desea resolver. ya, valor inicial. a,
% instante de tiempo inicial o valor inicial de la variable independiente.
% b valor de tiempo final o valor final de la variable independiente. h,
% paso de integracion
%podemos por elemental prudencia, comprobar que b>a
%lo elegante no es pasar el paso como he hecho aqui, sino calcularlo en
%funcion de cuantos puntos de la solucion queremos en el intervalo...
if a>=b
    y='el intervalo debe ser creciente, para evitarse lios'
    return
end
y=ya;
paso=1;
t(paso)=a;
while t(paso)<=b
    t(paso+1)=t(paso)+h;
    y(paso+1)=y(paso)+h*feval(fun,t(paso)+h/2,y(paso)+h*feval(fun,t(paso),y(paso))/2);
    paso=paso+1;
end
%pintamos la solucion,
plot(t,y)
