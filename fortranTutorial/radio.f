      program circle

c*********************************************
c This program reads a real number and prints
c the area of a circle with radius r.
c Autor: Antonio Galv''an
c Since 18 June 2014
c*********************************************

      real r, area
      parameter (pi = 3.14159)
      
      write(*,*) 'Give radius r:'
      read(*,*) r
      area = pi*r*r
      write (*,*) 'Area =', area
      stop
      end
