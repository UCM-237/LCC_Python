function s=condensador(t,Vo)
%t tiempo en este ejemplo la funci�n no depende del tiempo por lo que esta
%variable realmente no se usa... pero como el programa Euler se la pasa, 
%empleamos el simbolo ~ para que no de errores...
%Vo Valor del voltaje en cada iteraci�n

%hay que definir los parametros fijos del circuito...
C=0.0001; %Capacidad del condesador en Faradios
R=1000; %resitencia en Ohmios
%el voltaje de entrada podr�a Vi podria ser una funci�n del tiempo... Aqu�
%vamos a considerar que es constante...
Vi=10; %Voltaje suministrado al circuito en Voltios
%Aqui cosntruimos la funcion que representa el circuito RC,

s=(Vi-Vo)/R/C;

















