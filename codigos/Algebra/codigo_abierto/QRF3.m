function [Q,R]=QRF3(A)
%Calculo de factorizacion QR de la matriz A, mediante la ortogonaliación de
%householder. Este es el algoritmo bueno para hacerlo, pero habría que
%explicar a las criaturas householder...
%Obtenemos las dimensiones de A
[m,n]=size(A);


R=A
Q=eye(m,n)

%nos construimos una matriz auxiliar para ir interando las trasformaciones
%de householder
 
%Como siempre, vamos factorizando por columnas de la matriz A

for i=1:n
    %calculamos el módulo de cada vector columna, implicado en la fiesta
   A=R
    modulo=norm(R(i:m,i))
    r=-sign(R(i,i))*modulo
    for k=1:m
        v(k)=R(k,i)
    end
        
    v(i)=v(i)-r
    
    %recalculamos el modulo
    modulo=norm(v(i:m))
    for k=i:m
        v(k)=v(k)/modulo
    end
    Qa=eye(m,n)
    for t=i:m
        for s=i:n
            Qa(t,s)=Qa(t,s)-2*v(t)*v(s)
        end
    end
    for s=i:n
        for t=i:m
            for k=i:m
                R(t,s)=R(t,s)-2*v(t)*v(k)*A(k,s)
            end
        end
    end
    
   Q=Q*Qa
    %Obtenemos los valores de R por encima de la diagonal..
end
 
 
