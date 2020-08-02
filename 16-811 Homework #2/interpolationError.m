function [error] = interpolationError(n)

% create tabled data to input 
x = zeros(n, 1);
for i = 0:n
   x(i+1) = (i * (2/n)) - 1; 
end

y = zeros(n, 1);
for i = 0:n
   y(i+1) =  6/(1 + 25 * x(i+1)^2);
end

testXs = linspace(-1, 1, 200);

for i = 1:length(testXs)
    [~, DDsols(i)] = dividedDifference(x, y, testXs(i));
    realSols(i) =  6/(1 + (25 * testXs(i)^2));
    errors(i) = abs(realSols(i) - DDsols(i));
end

subplot(2,1,1);
plot(testXs, realSols);
xlabel('Value of x');
ylabel('Function Value');
subplot(2,1,2);
plot(testXs, errors);
xlabel('Linearly Spaced Values of x');
ylabel('Error Value');


disp(DDsols);
disp(realSols);

error = max(errors);
disp(error);
end