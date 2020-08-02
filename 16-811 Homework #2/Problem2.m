function y = Problem2(x)
y = x - (tan(x)/(1/cos(x)^2));
i = 1;

while(1)
if abs(y) > 1 * 10^-5
    xn = x - (tan(x)/(1/cos(x)^2));
    y = tan(xn);
    x = xn;
    i = i + 1;
else
    disp("The root is: ")
    disp(x)
    disp("Number iterations: ")
    disp(i)
    break
end

end

