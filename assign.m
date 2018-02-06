%Chain Code 

chaincode = importdata('flower_chain_code.txt')

Ref_CIX = [1 1 0 -1 -1 -1 0 1];
Ref_CIY = [0 1 1 1 0 -1 -1 -1];

%CI = [2 1 7 6 4 4];
CI = [2 2 1 7 6 6 4 4];
[m n] = size(CI);
CIX = zeros(m,n);
CIY = zeros(m,n);
YI = zeros(m,n);
A = zeros(m,n);

%Fill CIX and CIY arrays
for i=1:n
    CIX(i) = Ref_CIX(CI(i)+1);
    CIY(i) = Ref_CIY(CI(i)+1);
end

%Compute YI and Area
for i=1:n
    if i~=1
        YI(i) = YI(i-1)+CIY(i);
        A(i) = CIX(i)*(YI(i-1)+(CIY(i)/2));
    else
        YI(i) = 0 + CIY(i);
        A(i) = CIX(i)*(0+(CIY(i)/2));
    end
end
A
SUM_AREA = sum(A)