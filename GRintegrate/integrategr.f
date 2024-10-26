      Program Integrategr
      Implicit None

      Double Precision Delta
      Integer Nbin

      Parameter (Delta = 0.01d0)
      Parameter (Nbin  = 2000)
      
      Integer I,J
      
      Double Precision Gg(Nbin),Int1,Int2,Int3,X,F1,F2,F3,Glng


      Do J=1,Nbin
         Read(21,*) X,Gg(J)
      Enddo

      Do I=1,Nbin

         Int1 = 0.0d0
         Int2 = 0.0d0
         Int3 = 0.0d0

         Do J=1,I
            X = (Dble(J)-0.5d0)/Dble(I)
               
            F1 = (((Dble(J)-0.5d0)*Delta)**2)*
     &           (1.0d0 - (23.0d0/8.0d0)*X*X*X +
     &           0.75d0*X*X*X*X + 1.125d0*X*X*X*X*X )

            F2 = ((Dble(J)-0.5d0)*Delta)**2

            F3 = (((Dble(J)-0.5d0)*Delta)**2)*
     &           (1.0d0 - 1.5d0*X + 0.5d0*X*X*X)
               
            Int1 = Int1 + Delta*(Glng(Gg(J)) - Gg(J) + 1.0d0)*F1
            Int2 = Int2 + Delta*(Glng(Gg(J)) - Gg(J) + 1.0d0)*F2
            Int3 = Int3 + Delta*(Glng(Gg(J)) - Gg(J) + 1.0d0)*F3
         Enddo

         Write(22,*) Dble(I)*Delta,Int1,Int2

         Write(23,*) 1.0d0/(Dble(I)*Delta),Int2,Int3

         Write(24,*) Dble(I)*Delta,Dble(I)*Delta*Int3
            
      Enddo
      
      Stop
      End

      Function Glng(X)
      Implicit None

      Double Precision Glng,X

      If(X.Lt.1.0d-20) Then
         Glng = 0.0d0
      Else
         Glng = X*Dlog(X)
      Endif

      Return
      End
      
