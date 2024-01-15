function n=potencia(x,max)
%este programa emplea un buc^le while para calcular la potencia a la que hay
%que elevar un número x para que el resultado sea mayor que otro
%determinado número max
%un número.

%NOTA EL PROGRAMA NO COMPRUEBA QUE LA VARIABLE DE ENTRADA X SEA UN NUMERO,
%Si ES UN VECTOR O UNA MATRIZ EL RESULTADO NO TIENE SENTIDO
  
pot=1;
n=0;
while pot<max %mientras la potencia calculada sea menor que max
    n=n+1;
    pot=x^n;
end