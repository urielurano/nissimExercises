      program rain

      real function r(m,t)
      real t,sum
      integer m
      
      write(*,*)'Give a me a real number:'
      read(*,*)t
      sum = 0.0
      do 10 m = 1, 12
         sum = sum + r(m,t)
 10   continue
      write(*,*)'Anual rainfall is ', sum, 'inches'

      r = 0.1*t * (m**2 + 14*m + 46)
      if (r .LT. 0) r = 0.0

      return
      end
