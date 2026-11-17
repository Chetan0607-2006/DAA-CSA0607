# Q3_Karatsuba_Multiplication

KARATSUBA(x,y): if either number is single digit multiply; split x=a*B+b and y=c*B+d; z0=K(b,d),z2=K(a,c),z1=K(a+b,c+d)-z0-z2; return z2*B^2+z1*B+z0. T(n)=3T(n/2)+Theta(n)=Theta(n^log2(3)).
SCHOOLBOOK: multiply each decimal digit pair, carry and combine; Theta(n^2).
