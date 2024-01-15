function int=integra(fun,met,inter,dib)
%implementa los metodos del trapecio, etc...
%Uso: int=integra(fun,inter,dib)
%fun, nombre de la funci�n que se desea intergrar, debe ir entre comillas
%met, m�todo que se desea emplear para calcular la integral. los nombres
%validos para los metodos son: 'trapecio', 'simpsom' y simpsom38'
%inter, es un vector de dos elementos que contiene lo extremos de intervalo
%de integracion [a,b]
%dib, si se da un valor a esta variable de entrada, dibuja la funci�n en el
%intervalo de integraci�n y la integral obtenida. Si se omite no dibuja
%nada.
%int, valor de la integral obtenida.
%Este programa no divide el intervalo de integraci�n en subintervalos...
%para calcular la integral empleando subintervalos usar la funci�n trocea,

if strcmp(met,'trapecio')
    f0=feval(fun,inter(1));
    f1=feval(fun,inter(2));
    h=inter(2)-inter(1);
    int=h*(f0+f1)/2;
    if nargin==4
        x=inter(1):(inter(2)-inter(1))/100:inter(2);
        yfuncion=feval(fun,x);
        ypolinomio=f0+(x-inter(1))*(f1-f0)/h;
        plot(x,yfuncion,x,ypolinomio,'r')
    end
elseif strcmp(met,'simpsom')
    pmedio=inter(1)+(inter(2)-inter(1))/2;
    f0=feval(fun,inter(1));
    f1=feval(fun,pmedio);
    f2=feval(fun,inter(2));
    h=(inter(2)-inter(1))./2;
    int=h*(f0+4*f1+f2)/3;
    if nargin==4
        x=inter(1):(inter(2)-inter(1))/100:inter(2);
        yfuncion=feval(fun,x);
        ypolinomio=f0+(x-inter(1)).*(f1-f0)/h+(x-inter(1)).*(x-pmedio).*(f2-2*f1+f0)./(2*h^2);
        plot(x,yfuncion,x,ypolinomio,'r')
        hold on
        fill([x(1) x x(length(x))],[0 ypolinomio 0],'r') 
    end
elseif strcmp(met,'simpsom38')
    inter=inter(1):(inter(2)-inter(1))/3:inter(2);

    f=feval(fun,inter);
    h=(inter(4)-inter(1))/3;
    int=3*h*(f(1)+3*f(2)+3*f(3)+f(4))/8;
    if nargin==4
        x=inter(1):(inter(4)-inter(1))/100:inter(4);
        yfuncion=feval(fun,x);
        ypolinomio=f(1)+(x-inter(1)).*(f(2)-f(1))/h+(x-inter(1)).*(x-inter(2)).*(f(3)-2*f(2)+f(1))./(2*h^2)+...
            +(x-inter(1)).*(x-inter(2)).*(x-inter(3)).*(f(4)-3*f(3)+3*f(2)-f(1))./(6*h^3);
        plot(x,yfuncion,x,ypolinomio,'r')
    hold on
        fill([x(1) x x(length(x))],[0 ypolinomio 0],'r') 
    end
else
    int='metodo desconocido, los metodos conocidos son ''trapecio'', ''simpsom'' y ''simpsom38'''
end