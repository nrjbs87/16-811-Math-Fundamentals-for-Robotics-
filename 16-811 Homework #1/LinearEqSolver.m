% Solve Ax = b using Naive Gauss Elimination
% A = [2 2 5; 1 1 5; 3 2 5;];
% b = [5; -5; 0;];
A = [-3 -4 -1; 2 3 1; 3 5 2;];
b = [3; 5; 1;];
%% Gaussian Elimination
% Get Augmented matrix
Ab = [A,b];
[m,n] = size(A);

if m ~= n
    fprintf('Ab is not a square matrix');
end

L = eye(n);
P = L;
U = Ab;

for k = 1:n
%     disp(k:n);
%     % mx holds the index of the largest abs value of each col
%     [~, mx] = max(Ab(U(k:n, k)));
%     mx = mx+k-1;
%   
%     
%     if mx ~= k 
%         
%         temp = U(mx, :);
%         U(mx, :) = U(k,:);
%         U(k,:) = temp;
%         
%         % interchange rows m and k in P
%         temp = P(k, :);
%         P(k, :) = P(m, :);
%         P(m, :) = temp;
%         
%         
%         if k >= 2
%             temp = L(k, 1:k-1);
%             L(k, 1:k-1) = L(mx, 1:k-1);
%             L(mx, 1:k-1) = temp;
%         end
%         
%     end
%    
    
    for j = k+1:m
        Alpha = U(j,k)/U(k,k);
        U(j,:) = U(j,:) - Alpha*U(k,:);
        L(j,k) = Alpha;
        
    end

   
end

sol = zeros(m,1);

for i = 3:-1:1
    
    sol(i) = ( Ab(i,end) - ( Ab(i,i+1:n) * sol(i+1:n) ) ) / Ab(i, i);
    
end

disp(sol);