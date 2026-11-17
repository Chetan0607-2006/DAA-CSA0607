# Q1_MaxMin_Binary_Search

MINMAX(A): if 1 element return (x,x); if 2 elements compare once; otherwise split A in half, recursively get (min,max) from each, compare minima and maxima to combine.
BINARY_SEARCH(A,x): lo=0,hi=n-1; while lo<=hi compare A[mid] to x; return mid if equal; eliminate half based on comparison; return -1.
Recurrences: MinMax T(n)=2T(n/2)+2 = Theta(n); binary search T(n)=T(n/2)+Theta(1)=Theta(log n).
