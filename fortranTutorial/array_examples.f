      program array_examples

c***********************************************
c Program to make examples of arrays in fortran
c Autor: Antonio Galv''an
c Since: 18 June 2014
c***********************************************

      integer i,sq(100)

c***********************************************
c*** Make the array of the square of   *********
c*** the firts 100  integers positives *********
c***********************************************

      i = 1
      sq = 0
      
      do while(100.GE.i)
         sq(i) = i**2
         write(*,*)'The square of ',i,' is ',sq(i)
         i = i+1
      enddo

      stop
      end
      
