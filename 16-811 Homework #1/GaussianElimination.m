% Solve Ax = b using Naive Gauss Elimination
A = [ 1 1 1; 2 1 3; 3 4 -2];
b = [ 4; 7; 9;];

%% Gaussian Elimination
% Get augmented matrix
Ab = [A, b];
n = 3;

% With A(1,1) as pivot Element
for i = 2:3
alpha = Ab(i,1)/Ab(1,1);
Ab(i,:) = Ab(i,:) - alpha * Ab(1,:);
end

for i = 3
% With A(2,2) as pivot Element
alpha = Ab(i,2) / Ab(2,2);
Ab(i,:) = Ab(i,:) - alpha  * Ab(2,:);
end

%% Back Substitution 
sol = zeros(3,1);
% sol(3) = Ab(3,end)/Ab(3,3)

for i = 3:-1:1
    
    sol(i) = ( Ab(i,end) - ( Ab(i,i+1:n) * sol(i+1:n) ) ) / Ab(i, i);
    
end

% sol(3) = Ab(3,end)/Ab(3,3);
% sol(2) = ( Ab(2, end) - sol(3) )/Ab(2,2);
% sol(1) = Ab(1,end) - sol(3) - sol(2); 
disp(sol)



