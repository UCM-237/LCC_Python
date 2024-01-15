%este script  (figuras.m)muestra el uso de los comandos figure y plot para pintar
%varias funciones se aconseja copiarlo y probarlo en matlab para entender
%mejor cómo funciona.

%vamos a pintar un trozo de la función e^x, en concreto para el intervalo
%x=[0,1]

%Construimos un vector de 100 puntos equiespaciados en el intervalo [0,1]

x=linspace(0,1,100);

%calculamos el valor de la funcion e^x para los puntos cosntruidos,

y1=exp(x);

%pintamos los puntos y frente a x,

plot(x,y1) %plot ha construido una figura en matlab, la figura 1.

%Construimos una segunda figura en matlab
figure %se ha construido la figura 2

%construimos una tercera figura 
figure %se ha construido la figura 3


%calculamos los valores que tomará la función sin(2*pi*x) para los puntos
%x del intervalo [0,1] que ya tenemos
y2=sin(2*pi*x);

%hacemos activa la figura 2
figure(2)
%pintamos en esta figura los puntos de la función sin...

plot(x,y2)

%volvemos a hacer activa la figura 1
figure(1)
%pintamos ahora los puntos de la de la función y=e^x, pero invertidos x
%frente a y, La grafica anterior se borra y es sustituida por la nueva,
plot(y1,x)

%creamos una nueva figura asignándole un numero al crearla,
figure(13)

%volvemos activar la figura 3
figure(3)

%volvemos a pintar, ahora en la figura 3, la función y=e^x,
plot(x,y1)

%volvemos a activar la figura 13 y pintamos en ella de nuevo la funcion
%sin..

figure(13)
plot(x,y2)
