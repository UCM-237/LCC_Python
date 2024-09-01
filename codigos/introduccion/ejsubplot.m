%Este script muestra el uso del comando subplot

%vamos a crear una figura con 2X3=6 gr�ficas, se disponen en la figura como
%si fueran los elementos de una matriz...
%usamos el comando subplot de modo que cree el primer eje de los 6
subplot(2,3,1)

%definimos un vector x de puntos equiexpacios en el intervalo (-1,1)
x=linspace(-1,1,20);

%calculamos los valores de polinomio 3x^2+2^x-1
y=3*x.^2+2*x-1;

%dibujamos la funci�n en los ejes
plot(x,y)

%A�adimos r�tulos a los ejes
xlabel('eje x')
ylabel('eje y')
%A�adimos un titulo al grafico
title('gr�fico 1')

%Generamos los siguientes ejes (a la derecha del anterior)
subplot(2,3,2)
%dubujamos la misma funci�n pero ahora en linea discontinua roja
plot(x,y,':r')

%A�adimos r�tulos a los ejes
xlabel('eje x')
ylabel('eje y')
%A�adimos un titulo al grafico
title('gr�fico 2')

%Generamos los siguientes ejes (a la derecha del anterior)
subplot(2,3,3)
%dubujamos la misma funci�n pero ahora en linea de punto y raya negra
plot(x,y,'-.k')

%A�adimos r�tulos a los ejes
xlabel('eje x')
ylabel('eje y')
%A�adimos un titulo al grafico
title('gr�fico 3')

%Generamos los siguientes ejes (debajo de los primeros)
subplot(2,3,4)
%dubujamos la misma funci�n pero ahora solo con circulos azules
plot(x,y,'o')

%A�adimos r�tulos a los ejes
xlabel('eje x')
ylabel('eje y')
%A�adimos un titulo al grafico
title('gr�fico 4')

%Generamos los siguientes ejes (a la derecha del anterior)
subplot(2,3,5)
%dubujamos la misma funci�n pero ahora solo con cruce rojas
plot(x,y,'+r')

%A�adimos r�tulos a los ejes
xlabel('eje x')
ylabel('eje y')
%A�adimos un titulo al grafico
title('gr�fico 5')

%Generamos los �ltimos ejes (a la derecha del anterior)
subplot(2,3,6)
%dubujamos la misma funci�n pero ahora en linea continua y asteriscos
%negros
plot(x,y,'-*k')

%A�adimos r�tulos a los ejes
xlabel('eje x')
ylabel('eje y')
%A�adimos un titulo al grafico
title('gr�fico 6')

