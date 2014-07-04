      program array_examples

c***********************************************
c Program to make examples of arrays in fortran
c Autor: Antonio Galv''an
c Since: 18 June 2014
c***********************************************

      integer i,j,lda,sq(100)
      real A(4,4),B(4,4),C(4,4),Z(5,3)
      parameter(pi = 3.14159)

c***********************************************
c*** Make the array of the square of   *********
c*** the firts 100  integers positives *********
c***********************************************

      i = 1
      sq = 0
      
      do 10 i = 1, 100
         sq(i) = i**2
         write(*,*)'The square of ',i,' is ',sq(i)
 10      continue
         write(*,*)'-----------------------------'
         
c************************************************
c***  Return in screen the sum of two Arrays  ***
c***      Of integers and  dimension 4x4      ***    
c************************************************
         
      Z = 0
      lda = 3
      do 20 i = 1,4
         do 30 j = 1,4
            A(i,j)=j
            B(i,j)=j+pi
            C(i,j)= A(i,j)*B(i,j)
            write(*,*)'The value of C',i,j,' is  =',C(i,j)
 30      continue
 20   continue
      write(*,*)'-----------------------------'

      stop
      end
      
