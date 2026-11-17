# Q2_MergeSort_QuickSort

MERGESORT(A): if length<=1 return; split in equal halves, sort both recursively, merge two sorted lists. T(n)=2T(n/2)+Theta(n)=Theta(n log n).
QUICKSORT(A): choose LAST ELEMENT pivot; partition into less/equal/greater, recursively sort less and greater, concatenate. Balanced Theta(n log n), worst Theta(n^2).
