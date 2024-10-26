      program wf
      implicit none

      integer i
      double precision r,rcut,lambda,alpha,d1,d2,d3,u

      parameter (rcut   = 2.0d0)
      parameter (lambda = 0.2d0)
      parameter (alpha  = 1.0d0)
      

      do i=1,200

         r = dble(i)*0.01d0

         d1 = r*r       + alpha*(1.0d0-lambda)
         d2 = rcut*rcut + alpha*(1.0d0-lambda)
         d3 = d2/d1 - 1.0d0

         u = lambda*(1/d1 - 1.0d0)*d3*d3
         
         if(u.lt.5.0d0) write(21,*) r,u

      enddo

      stop
      end
      
     
