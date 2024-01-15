%este script toma los valores de los catetos de un triángulo rectangulo del 
%workspace de matlab (variables a y b). calcula su hipotenusa, y a partir
%de estos datos, el seno el coseno y la tangente del angulo formado por la
%hipotenusa y el cateto mayor que será siempre a

%calculo hipotenusa,

h=sqrt(a^2+b^2)

%calculo del seno

s=a/h

%calculo del coseno
a=b/h %error estamos sobreescriesdo el valor del coseno en la variable que 
      %guardaba e valor del cateto

%calculo de la tangente
t=b/a
