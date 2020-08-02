p1 = @(x,y)(2*x^2+2*y^2-1);
ezplot(p1, [-2, 2, -2, 2]);
hold on 
p2 = @(x,y)(x^2 + y^2 + 2*x*y - x + y);
ezplot(p2, [-2, 2, -2, 2]);
title('Zero Contours')
hold off