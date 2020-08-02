% Solve Ax = b using Naive Gauss Elimination
% A = [ 1 -1 0; 0 2 -1; 1 0 -1/2; ];
% A = [ -1 1 0 0 ; -1 0 1 0; 0 -4 1 0; 0 -1 0 1; 0 0 -2 1; ];
A = [ 2 2 5; 1 1 5; 3 2 5;];
%% Gaussian Elimination
% Get augmented matrix
[m,n] = size(A);

% if m ~= n
%     fprintf('A is not a square matrix');
% end

L = eye(n);
P = L;
U = A;

for k = 1:n
    % mx holds the index of the largest abs value of each col
    [~, mx] = max(abs(U(k:n, k)));
    mx = mx+k-1;
  
    
    if mx ~= k 
        
        temp = U(mx, :);
        U(mx, :) = U(k,:);
        U(k,:) = temp;
        
        % interchange rows m and k in P
        temp = P(k, :);
        P(k, :) = P(m, :);
        P(m, :) = temp;
        
        
        if k >= 2
            temp = L(k, 1:k-1);
            L(k, 1:k-1) = L(mx, 1:k-1);
            L(mx, 1:k-1) = temp;
        end
        
    end
   
    
    for j = k+1:m
        alpha = U(j,k)/U(k,k);
        U(j,:) = U(j,:) - alpha*U(k,:);
        L(j,k) = alpha;
        
    end

   
end
disp(L);
disp(U);
disp(P);



