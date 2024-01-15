function secuencia=middlesquare(semilla, longitud)
%Este programa obtiene una secuencia de números psudoaleatorios empleado el
%método 'middle square'.
%uso: secuencia=middlesquare(semilla, logitud)
%Variables entrada: semilla, numero inicial que será empleado como semilla.
%longitud, cantidad de números aleatorios que debe generar la secuencia.
%variable de salida: secuencia vector de numeros aleatorios resultante

%creamos un vector de ceros para guardar los resultados
% convertimos el número a entero de 64 bits, asi todas la operaciones son
% enteras...
%ojo si usamos una semilla de mas de nueve digitos, el cuadrado puede
%desbordar el entero más grande representable.

semilla=uint64(semilla)
%calculamos la longitud de la semilla
c=semilla;
n=0;
while c>0
    c=idivide(c,10);
    %la linea de codigo anterior, puende no funcionar en algunas versiones
    %antiguas de matlab. Alternativamente, podría implementarse como,
    %c=(c-rem(c,10))/10;
    n=n+1;
end

%creamos un bucle para ir generando los numeros pseudoaleatorio a partir de
%la semilla
%elevamos al cuadrado la semilla
    
for i=1:longitud     
    l=semilla.^2
    %primero extraemos las n/2 cifras menores
    semilla=idivide(l,10^fix(n/2));
    %la linea de codigo anterior, puende no funcionar en algunas versiones
    %antiguas de matlab. Alternativamente, podría implementarse como,
    %semilla=(l-rem(l,10^fix(n/2)))/10^fix(n/2);
   
    % y a continuacion extraemos las n cifras siguiente, que seran el
    % siguiente numero aleatorio
    semilla = rem(semilla,10^n)
    % guardamos el numero generado en el vector de salida
    secuencia(i,1)=semilla;
end