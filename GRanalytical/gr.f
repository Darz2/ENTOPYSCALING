      Program Gr
      Implicit None

      Integer Nbin,I
      Double Precision Delta,G,R,Twopi,Gamma,Glng

      Parameter (Nbin  = 20000)
      Parameter (Delta = 0.01d0)
      
      Parameter (Twopi = 8.0d0*Datan(1.0d0))
      Parameter (Gamma = 20.0d0)
      
      Do I=1,Nbin
         R = (Dble(I)-0.5d0)*Delta

         If(R.Lt.0.95d0) Then
            G = 0.0d0
         Else
            G = 1.0d0 + 1.5d0*Dexp((1.0d0-R)/Gamma)*
     &           Dcos(Twopi*(R-1.05d0))/R

         Endif

         Write(21,*) R,G

         Write(22,*) R, 1.0d0-G , Glng(G) + 1.0d0 - G
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
      
