      program cicles
      integer a,b,i,n,j,k,m,sum



c***********************************************
c Program to make examples of loops in fortran
c Autor: Antonio Galv''an
c Since: 18 June 2014
c***********************************************      


********************************************
***Fisrt example of loops, the sum of the***
***    n number integer non negatives    ***
********************************************

      write(*,*)'***************************'
      sum = 0
      write(*,*)'Give me a integer positive:'
      read(*,*)n

      do 10 i = 1, n
         sum = sum + i
         write(*,*)'i   =', i
         write(*,*)'sum =', sum
 10      continue

      write(*,*)'***************************'
      write(*,*)' '

*********************************************
***    An example of the label statement  ***
*********************************************

      write(*,*)'***************************'
      do 20 i = 10, 1, -2
         write(*,*)'i =',i
 20   continue
      write(*,*)'***************************'
      write(*,*)' '

*********************************************
***    An example of the label statement  ***
*********************************************

      write(*,*)'***************************'
      write(*,*)'Please give me a value of j integer positive'
      read(*,*)j
      do 30 i = 1, 10
         k = j * i
         write(*,*)'The result is =', k
 30   continue

      write(*,*)'***************************'
      write(*,*)' '

*********************************************
****     An example of the while loops   ****
*********************************************
      
      write(*,*)'***************************'
      write(*,*)'Give me a integer positive, lower tan 100'
      read(*,*)m
      do while(m.LT.100)
         write(*,*)m
         m = m*2
      enddo

      write(*,*)'***************************'
      write(*,*)' '


*********************************************
****     An example of the while loops   ****
*********************************************

      write(*,*)'***************************'
      a = 1

 40   if(a.le.100)then
         write(*,*)'This is the value of a', a
         a=2*a
         goto 40
      endif
      write(*,*)'***************************'
      write(*,*)' '

*********************************************
****     An example of the  do loops     ****
*********************************************


      write(*,*)'***************************'
      do i= 1,12
         write(*,*)'The value of i =',i
      enddo
      write(*,*)'***************************'
      write(*,*)' '

*********************************************
****     An example of the  do loops     ****
*********************************************


      write(*,*)'***************************'
      b = 0
      do
         write(*,*)'The value of b =',b
         b = b+1         
      until(b.lt.10)
      write(*,*)'***************************'
      write(*,*)' '



      stop
      end
