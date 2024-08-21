function y=euler(fun,ya,a,b,h)
% implimentacion del metodo de Euler para resolver el problema y'(t)=f(y,t)
% con condición inicial ya
%Uso: y=euler(fun,ya,a,b,h)
%variables de entrada: fun, debe contener el nombre de una función (sera la
%función f) entrecomillas. ya, condición inicial. a, instante de tiempo 
%inicial o valor inicial de la variable independiente (t). 
%b, instante de tiempo final o valor final de la variable independiente
%h paso de integración
%podemos por elemental prudencia, comprobar que b>a
%lo elegante no es pasar el paso como he hecho aqui, sino calcularlo en
%funcion de cuantos puntos de la solucion queremos en el intervalo...
if a>=b
    y='el intervalo debe ser creciente, para evitarse lios';
    return
end
y=ya;
paso=1;
t(paso)=a;
while t(paso)<=b
    t(paso+1)=t(paso)+h;
    y(paso+1)=y(paso)+h*feval(fun,t(paso),y(paso));
    paso=paso+1;
end
%dibuja la solucion,
plot(t,y)
