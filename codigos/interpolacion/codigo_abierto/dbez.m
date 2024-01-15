function d = dbez(p)
grado = size(p,1)-1
d = zeros(grado,2)
for i = 1:grado
    d(i,:) = (grado-1)*(p(i+1,:)-p(i,:))
end
end