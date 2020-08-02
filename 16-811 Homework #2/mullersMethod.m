function [root, value] = mullersMethod(f, guess)

x1 = guess(1);
x2 = guess(2);
x3 = guess(3);

tol = 1 * 10 ^ -4;
error = 1000;

while error >= tol
y1 = f(x1);
y2 = f(x2);
y3 = f(x3);

c1 = (y2 - y1)/(x2 - x1);
c2 = (y3 - y2)/(x3 - x2);
d1 = (c2 - c1)/(x3 - x1);
s = (c2 + d1*(x3 - x2));

x4 = x3 - ((2 * y3)/(s + sign(s) * sqrt(s^2 - (4 * y3 * d1))));

error = abs(x4 - x3);
x1 = x2;
x2 = x3;
x3 = x4;
end

value = x3;
root = f(x3);


end