function [x] = newtonsMethod(f, df, x0)

f = inline(f);
df = inline(df);

x(1) = x0 - (f(x0)/df(x0));
error(1) = abs(x(1) - x0);


tol = 1 * 10^-4;

k = 2;
while error(k-1) >= tol
    x(k) = x(k-1) - (f(x(k-1))/df(x(k-1)));
    error(k) = abs(x(k) - x(k-1));
    k = k + 1; 
end

x = x(k-1);
disp(x);
end