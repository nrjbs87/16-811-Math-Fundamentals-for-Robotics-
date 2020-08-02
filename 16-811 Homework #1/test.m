% Solve Ax = b using Naive Gauss Elimination
%A = [ 1 -1 0; 0 2 -1; 1 0 -1/2; ];
A = [ -1 1 0 0 ; -1 0 1 0; 0 -4 1 0; 0 -1 0 1; 0 0 -2 1; ];

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
    [~,mx] = max(abs(U(:,k)));
    disp(U(:,k));
    
%     disp(U);
    disp(U(mx,k));
end