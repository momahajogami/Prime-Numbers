# Prime-Numbers
Algorithms from [*Prime Numbers, A Computational Perspective*](http://www.springer.com/us/book/9780387252827) by Crandal and Pomerance.

As a beginning, choose Algorithm 6.4.1 on page 304, the Index-calculus method for computing discrete logs in (F_p)\*. 

This is a complicated algorithm which is dependant on several other algorithms in the book, such as a smoothness test and computing inverses modulo a prime. 


Here is a brief To do list for implementing Index-Calculus for
discrete logs in (F_p)\* 6.4..1 p 340:

1. generate primes. 3.2.1 p 122 (done)
1. compute inverses in (F_p)*. 2.1.4 p 85 (done)
1. Bernstein's smoothness test. 3.3.1 p 130 (done) *or* Pollard rho 5.2.5 *or* Elliptic curve method 5.2.1

For doing linear algebra modulo a composite m:

1. CRT reconstruction. 2.1.7 p 88 (done)
1. Hensel lifting 2.3.11 p 105 (nonsingular case done)

