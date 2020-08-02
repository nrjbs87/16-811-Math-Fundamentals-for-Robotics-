p = @(x) 0.5 + sin(x);
ezplot(p, [-pi/2, pi/2]);
hold on
p1 = @(x) 0.5 + 0.724 * x;
ezplot(p1, [-pi/2, pi/2]);
title("0.5 + sin(x) over [-pi/2, pi/2]");
