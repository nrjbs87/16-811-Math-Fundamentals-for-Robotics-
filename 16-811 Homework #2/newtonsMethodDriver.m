function x = newtonsMethodDriver

v = linspace(8, 14, 50);
x = zeros(length(v), 1);
f = ('x - tan(x)');
df = ('1 - 1/cos(x)^2');

for i = 1:length(v)
    x(i) = newtonsMethod(f, df, v(i));
end
end