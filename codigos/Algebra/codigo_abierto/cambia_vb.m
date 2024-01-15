function aB2=cambia_vb(aB1,B1,B2)
%este programa cabia de base un vector de dimensión 3 y lo representa en
%relación con las bases antigua y nueva.
%variables de entrada:
%aB1, componentes del vector en la base 1
%B1 base representada como una matriz, (cada columna contiene un vector de
%la base) En la que está representado el vector aB1
%B2, base representada como una matriz, (cada columna contiene un vector de
%la base) en la que se quiere representar el vector aB1
%Si solo se incluye un vector y una base, el programa asume que la segunda
%base es la canonica B2=[1 0 0;0 1 0; 0 0 1]
%variables de salida:
%aB2, Componentes del vector aB1 en la nueva base B2.

if nargin==2
    %asumimos que queremos cambiar el vector de B1 a la base canonica
    %¿Es B1 una base sensanta?
    if det(B1)<=eps
        error('los vectores de la base no son l. independientes')
    end
    aB2=B1*aB1;
    B2=eye(3); %creamos la base para luego pintarla...
elseif nargin==3
    %cambio de base B1 a B2
    if (det(B1)<=eps)||(det(B2)<=eps)
        error('los vectores de al menos una de las bases no son l. independientes')
    end
    aB2=inv(B2)*B1*aB1;
else
    error('el numero de variables de entrada es menor de dos o mayor de tres')
end

%Dibujo de los vectores con la función pintavec....

pintavec(B1,'r') %vectores de la base original
xlabel('x')
ylabel('y')
zlabel('z')
grid on
pintavec(B2,'b') %vectores de la base nueva
for i=1:3
    pintavec(aB1(i)*B1(:,i),'k') %componentes de aB1
    pintavec(aB2(i)*B2(:,i),'k') %componentes de aB2
end
aBc=B1*aB1; %representacion del vector en la base canónica
pintavec(aBc,'g') %vector representado



function pintavec(a,par)
%función auxiliar para pintar vectores... con origen en el origen de
%coordenadas (0,0,0).
%la variable a puede ser un vector o una matriz. y par, es una cadena que contiene los
%típicos parámetros(color, tipo de línea`etc'). El programa considera que
%los vectores están siempre definidos como vectores columnas...
d=size(a,2); %miramos cuantas columnas tiene a, cada columna representará un
%vector distinto
if nargin==2
    for i=1:d
        quiver3(0,0,0,a(1,i),a(2,i),a(3,i),0,par)
        hold on
    end
else
    for i=1:d
        quiver3(0,0,0,a(1,i),a(2,i),a(3,i),0)
    end
end
