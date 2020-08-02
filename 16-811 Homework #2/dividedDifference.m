function [DDTable, sum] = dividedDifference(x, y, v)

if nargin ~= 3
    disp("Not enough inputs to the function");
    return;
end

DDTable = zeros(length(x));
DDTable(:,1) = y';
[m,n] = size(DDTable);

% generates DDTable
for i = 2:n % i manages columns
    for k = 1:m + 1 - i % k manages rows
        DDTable(k, i) =(DDTable(k+1, i-1) - DDTable(k, i-1))/(x(k+i-1) - x(k)); 
    end
    
end

% solves for value = n
coeff = DDTable(1,:);
sum = coeff(1);

for i = 2:length(coeff)
    product = 1;
    for j = 1:i -1 
        product = product * (v - x(j));
    end
    sum = sum + (coeff(i) * product);
end


end