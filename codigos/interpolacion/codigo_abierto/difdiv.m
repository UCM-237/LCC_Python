function a=difdiv(x,y)
%este polinomio permite obtener los coeficientes del polinomio de
%diferencias divididas que interpola los datos contenidos el los vectores x
%e y. Da como resultado un vector fila a con los coeficientes

%miramos cuantos datos tenemos
n=length(x);

%inicializamos el vector de coeficientes con las diferencias de orden 0, es
%decir los valores de y,

a=y;

%y ahora montamos un bucle, si tenemos n datos debemos calcular n
%diferencias, como ya tenenos la primera, iniciamos el bucle en 2,
for j=2:n
    %en cada iteración calculamos las diferencias de un orden superior,
    %como solo nos vale la primera diferencia de cada orden empezamos el
    %bucle interior en el valor del exterior j
    for i=j:n
        a(i)=(a(i)-y(i-1))/(x(i)-x(i-j+1));
    end
    %volvemos acopiar en y las diferencias obtenidas para emplearlas en la
    %siguiente iteracion
    y=a;
    
end

