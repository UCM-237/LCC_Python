function vt=ltrans(A,v)
%este programa calcula el vector resultante de aplicar la matriz A al
%vector v y representa graficamente el vector original y el vector
%transformado,


%la transformación es simplemente el producto A*v
vt=A*v;

% representacion,

if length(v)==2
    quiver(0,0,v(1),v(2),0,'b')
    hold on
    quiver(0,0,vt(1),vt(2),0,'r')
    xlabel('x')
    ylabel('y')
    grid on
elseif length(v)==3
    quiver3(0,0,0,v(1),v(2),v(3),0,'b')
    hold on
    quiver(0,0,0,vt(1),vt(2),v(3),0,'r')
    xlabel('x')
    ylabel('y')
    zlabel('z')
    grid on
else
    error('el vector no es representable')
end
    
    