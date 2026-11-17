# Q4_Strassen_Matrix_Multiplication

STRASSEN(A,B): pad square matrices to next power of 2, divide each into four blocks; calculate 7 products M1..M7 from sums/differences; combine C11=M1+M4-M5+M7, C12=M3+M5, C21=M2+M4, C22=M1-M2+M3+M6; remove padding. Base case conventional multiplication. T(n)=7T(n/2)+Theta(n^2)=Theta(n^log2(7)).
