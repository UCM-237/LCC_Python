function [ieee,signo,mantisa,exponente]=dec2ieee754(numero)

%convierte un número en basa 10 al estandar ieee de precision simple

%en primer lugar extraesmo el signo
if numero==abs(numero)
    signo=0
else
    signo=1
    numero=-numero
end

%en segundo lugar separamos la parte entera de la parte fracionaria del
%numero,

entera=fix(numero);
decimal=numero-entera;

%creamos una mantisa llena de ceros...
mantisa=zeros(1,52);
%miramos si el numero tiene o no  parte entera

if entera>0
    %tiene parte entera
    expodec=0;
    while entera>1

        %desplazar la mantisa para incluir el nuevo numero
        %%%%%%usando un for%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %     for i=2:52
        %         mantisa(i)=mantisa(i-1)
        %     end
        %     mantisa(1)=rem(entera,2)
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        mantisa=[rem(entera,2) mantisa(1,1:51)];
        entera=fix(entera/2);
        expodec=expodec+1;
        if expodec>1023
            % el numero no es representable sacamos entoces la representacion
            % de infinito
            mantisa=zeros(1,52);
            expodec=1024;
            break
        end
    end
    %lsolo podemos añadir decimales para los huecos de mantisa que nos queden
    for i=expodec+1:52
        mantisa(i)=fix(decimal*2);
        decimal=decimal*2-fix(decimal*2);
    end
else
    % no tiene parte entera. Tenemos que ir decrementando el exponente hasta
    % que aparezca el primer 1
    expodec=-1;
    while fix(decimal*2)==0
        expodec=expodec-1;
        %desnormalización....
        if expodec==-1023
            %hay que desnormalizar el número con lo cual empezamos a meter
            %ceros en la mantisa... Basta calcular las 52 posiciones que
            %nos quedan... no podemos bajar mas el exponente
            break
        end
        decimal=decimal*2-fix(decimal*2);
        disp(decimal);
    end
    %rellenamos las posiciones de mantisa que nos queda.
    for i=1:52
        decimal=decimal*2-fix(decimal*2);
        mantisa(i)=fix(decimal*2);
    end
end
   %tan solo nos queda representar el exponente en binario....
   %como está calculado en exceso a 1023... le sumamos al exponente
   %obtenido 1023..
   
   expodec=expodec+1023;
   
 
   %solo queda pasar a binario en numero resultante... podemos usar el
   %codigo ways de las condicionales ya que solo podemos rellenar 11 bits
   
   %construimos un vector del 11 bits, todos a cero.
    exponente=zeros(1,11);
    
    for i=1:11
        if 2^(11-i)>expodec
            exponente(i)=0;
        else
            exponente(i)=1;
            expodec=expodec-2^(11-i);
        end
        
    end
    
    %para hacer felices a los que propusieron el programa montamos un solo
    %vector con todos los resultados...
    ieee=[signo exponente mantisa];
   



            
