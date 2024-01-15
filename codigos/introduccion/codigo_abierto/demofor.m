function y=demofor(x)
%este programa emplea un bucle for sencillo para ir mostrando uno a uno
%los elementos del vector de entrada x por pantalla. además los suma y 
%guarda el resultado total en el vector y,

y=0; %iniciamos la suma a cero

for i=x
    disp(i)
    y=y+i;
    i=35
end