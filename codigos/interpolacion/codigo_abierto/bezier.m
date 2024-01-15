function ber = bezier(p,res)
%estas funcion pinta la curva de Bezier correspondiente a los puntos de 
%control p. 
%p debe ser una matriz de dimension n*2 donde n es el número de puntos de 
%control empleados La primera columna contiene las coordenadas x 
%y la segunda las coordenas y.
%El codigo sigue directamente la definicion de los polinomios de Bernstain
%por tanto, NO es un codigo optimo. Calcula varias veces las mismas
%cantidades.
%Los coeficientes binomiales de los polinomios de Berstein se 
%pueden calcular directamente con el comando de matlab nchoosek. Sin 
%enbargo, en el programa se han calculado a partir de la definicion:
% n!/((n-k)!k!)
%la variable de entrada res nos da el paso que empleará el parámatro t
%para calcular y dibujar el polinomio

t = 0:res:1;
ber = zeros(2,length(t));
%calculamos un vector de coeficientes para los polinomios.

%coeficientes para la coordenada x.

n = size(p,1)-1;
num = factorial(n);
for i = 0:n    
    f=num/factorial(i)/factorial(n-i);
    ber(1,:) = ber(1,:) + f*p(i+1,1)*(1-t).^(n-i).*t.^i;
    ber(2,:) = ber(2,:) + f*p(i+1,2)*(1-t).^(n-i).*t.^i;
end
plot(p(:,1),p(:,2),'or')
hold on
%plot(p(:,1),p(:,2),'r')
plot(ber(1,:),ber(2,:))