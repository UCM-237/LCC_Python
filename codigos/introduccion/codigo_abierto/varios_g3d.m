%este script (varios_g3d.m) incluye el diseño de varias retículas
%circulares para trazar gráficos de superficies en el espacio.

%retícula circular para un cono
 r=0:2/20:2;
 theta=0:2*pi/36:2*pi;
 [rm,them]=meshgrid(r,theta);
 
%calculamos las compontes en x e y partir de rm y thm,
 xm=rm.*cos(them);
 ym=rm.*sin(them);
 
%Definimos la componente z, a partir de la ecuación de un cono,
 zm=2-sqrt(xm.^2+ym.^2);

%lo dibujamos empleando el comando mesh
 mesh(xm,ym,zm)
 
%Para dibujar una esfera, podríamos emplear la misma retícula, pero sale
%más proporcionada, si de emplear intevalos de r equispaciodos, los hacemos
%proporcionales al águlo de elevacion (0,pi/2). Asique recalculamos r.

 r=2*cos(0:pi/2/18:pi/2); %tomamos 16 intervalos entre r= y r=2
%para theta usamos el mismo de antes, no hace falta volver a calcularlo.

%calculamos los puntos de la retícula en polares,
[rm,them]=meshgrid(r,theta);

%calculamos las componentes x e y a partir de rm y thm
 xm=rm.*cos(them);
 ym=rm.*sin(them);
 
 
 
 %definimos la componente z, como es la ecuación de una esfera, debemos
 %calcularla en dos partes,
 
 zm_mas=sqrt(4-(xm.^2+ym.^2));
 zm_menos=-sqrt(4-(xm.^2+ym.^2));
 
 %vamos a emplear la misma ventana gráfica en la que hemos dibujado el
 %cono, asi que pedimos a matlab que retenga lo ya dibujado,
 
 hold on
 
 %para que no salga un dibujo encima del otro, dibujamos la esfera
 %desplazando su origen al punto (3,3,0)
 %emplearemos ahora el comando surf para representarla
 
 %primero representamos la mitad superior
  surf(xm+3,ym+3,zm_mas)
 
 %y despues la parte inferior
  surf(xm+3,ym+3,zm_menos)
  
 %por último vamos a obtener la gráfica de un cilidro vertical, Para ello,
 %volvemos a alterar los valore de r. Costruimos un vector que repita
 %siempre los mismos valores y le damos tanto elementos como divisiones
 %'verticales queramos que tenga el cilindro, por ejemplo 20
 r=2*ones(1,20); 
 
 %volvemos a crear la reticula
 [rm,them]=meshgrid(r,theta);

%calculamos las componentes x e y a partir de rm y thm
 xm=rm.*cos(them);
 ym=rm.*sin(them);
 
 % Para calcular los valores de z, debemos dividir la altura total que
 % queremos dar al cilindro entre el número de divisiones en r que tiene la
 % retícula original por ejemplo si la altura fuera 2
  z=2/(length(r)-1)*(0:length(r)-1);
 % Tenemos una columna de la matriz z, pero necesitamos repetirlas para
 % cada valor de them,
  zm=ones(size(xm))*diag(z);
 
 %podemos ahora dibujar en cilindro. Como hemos hecho con la esfera, lo
 %vamos a desplazar a una posición en la que no se sobreponga a otra
 %figura, por ejemplo al punto (+3 -3 -1).
 
 %lo vamos a representar usando de nuevo en comando mesh
 
 mesh(xm+3,ym-3,zm-1)

 
    
 
 
 