function n=potencia(x,max)
%este programa emplea un buc^le while para calcular la potencia a la que hay
%que elevar un n�mero x para que el resultado sea mayor que otro
%determinado n�mero max
%un n�mero.

%NOTA EL PROGRAMA NO COMPRUEBA QUE LA VARIABLE DE ENTRADA X SEA UN NUMERO,
%Si ES UN VECTOR O UNA MATRIZ EL RESULTADO NO TIENE SENTIDO
  
pot=1;
n=0;
while pot<max %mientras la potencia calculada sea menor que max
    n=n+1;
    pot=x^n;
end