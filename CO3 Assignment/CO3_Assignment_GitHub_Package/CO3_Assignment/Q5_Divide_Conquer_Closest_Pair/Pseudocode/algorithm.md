# Q5_Divide_Conquer_Closest_Pair

CLOSEST_PAIR(P): sort by x and y; if <=3 points brute force; split x-sorted list into left/right and partition y-sorted list; solve both; d=min(left,right); form y-sorted strip within d of dividing x; compare each point to up to next seven points; return best pair. T(n)=2T(n/2)+Theta(n)=Theta(n log n).
