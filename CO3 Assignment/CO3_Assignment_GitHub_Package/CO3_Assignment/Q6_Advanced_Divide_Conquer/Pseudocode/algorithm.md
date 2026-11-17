# Q6_Advanced_Divide_Conquer

MEDIAN_OF_MEDIANS(A,k): group into fives, find group medians, recursively select median of medians as pivot; partition into less/equal/greater and recurse only on required partition. T(n)<=T(n/5)+T(7n/10)+O(n)=O(n).
MEET_IN_MIDDLE(A,target): split list into two halves; enumerate 2^(n/2) subset sums of each half; sort second list; for each left sum binary-search complement; return found/not found. Time O(n*2^(n/2)) with naive generation and sort; space O(2^(n/2)).
