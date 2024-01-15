function radesp(A,j,m)
%Calcula y pinta el radio espectral del sistema de matriz de coeficientes A
%para distintos valores del factor de amortiguamiento w,tanto para jacobi
%m = 1, como para gauss-seidel, m = 2, i representa el  numero
%valores de w probados

n=size(A,1);
D=diag(diag(A));
U=A-tril(A);
L=A-triu(A);
w = linspace(0,1,j);
I=eye(n)
if m==1
    for i = 1:length(w)
    %jacobi amortiguado
    H=-w(i)*D^-1*(L+U)+(1-w(i))*I;
    re = max(abs(eig(H)))
    plot(w(i),re,'o')
    xlabel('w')
     ylabel('re')
    hold on
    end
else
    for i = 1:length(w)
    %sor
    i
    H=(1-w(i))*I-w(i)*(D+L)^(-1)*U;
    re = max(abs(eig(H)))
     plot(w(i),re,'o')
     xlabel('w')
     ylabel('re')
    hold on
    end
end
 