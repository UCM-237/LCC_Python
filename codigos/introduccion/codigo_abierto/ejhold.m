%ejemplo de uso de hold on para reprsentar dos funciones en el mismo
%gr�fico

%vamos a representar las funciones seno y coseno en el intervalo [-pi, pi]

%creamos un vector de 100 puntos en el intervalo,
x=[-pi:2*pi/99:pi];

%calculamos el valor de la funcion seno sobre los puntos x
seno=sin(x);

%calculamos el valor de la funci�n coseno sobre los puntos x
coseno=cos(x);

%pintamos la funcion seno, con linea continua azul
plot(x,seno)

%le pedimos que mantenga el gr�fico creado
hold on

%pintamos encima la funci�n coseno en linea continua roja

plot(x,coseno,'r')
