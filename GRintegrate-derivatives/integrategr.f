      Program Integrategr
      Implicit None

      Double Precision Delta
      Integer Nbin, Gamma

      Parameter (Delta  = 0.01d0)
      Parameter (Nbin   = 20000)
      Parameter (Gamma  = 2)

      character(len=30) :: filename
      
      Integer I,J
      
      Double Precision Gg(Nbin),Ggg(Nbin),Int1,Int2,Int3,Int4,X,F1,F2,F3
     $     ,Glng,R2
      
      write(filename,'(a,i0,a)') 'GR/gr_',Gamma,'.dat'
      Open(21,File=filename)

      Do J=1,Nbin

         Read(21,*) X,Gg(J)
         
         Ggg(J) = Glng(Gg(J)) - Gg(J) + 1.0d0

         Gg(J)  = Gg(J) - 1.0d0

      Enddo

      Close(21)
      write(filename,'(a,i0,a)') 'integrategr_',Gamma,'.dat'
      Open(22,File=filename)

      Do I=1,Nbin

         Int1 = 0.0d0
         Int2 = 0.0d0
         Int3 = 0.0d0
         Int4 = 0.0d0

         Do J=1,I
            X  = (Dble(J)-0.5d0)/Dble(I)

            R2 = Delta*(((Dble(J)-0.5d0)*Delta)**2)
                        
            F1 = 1.0d0 - 1.5d0*X + 0.5d0*X*X*X

C           F2 is the first derivative

            F2 = 1.0d0 - X*X*X 

C           F3 is the second derivative

            F3 = 1.0d0 + 0.5d0*X*X*X
               
            Int1 = Int1 + (16.0d0*Datan(1.0d0))*R2*Gg(J)*F1
            Int2 = Int2 + (16.0d0*Datan(1.0d0))*R2*Gg(J)*F2
            Int3 = Int3 + (16.0d0*Datan(1.0d0))*R2*Gg(J)*F3

C           Int 4 is the first term of the third derivative expansion 

            Int4 = Int4 + (16.0d0*Datan(1.0d0))*R2*Gg(J)
         Enddo

C           R2 outside the loop is the second part of the third derivative expansion 

         R2 = (8.0d0*Datan(1.0d0))*Gg(I)*((Dble(I)*Delta)**3)

C           Int1 is with no approximation; Int2 is the first order approximation; Int3 is the second order approximation; Int3+R2 is the third order aprroximation;  Int 4 is the first term of the third derivative expansion 

         Write(22,*) 1.0d0/(Dble(I)*Delta),Int1,Int2,Int3,Int4+R2,Int4
      Enddo

      Close(22)
      write(filename,'(a,i0,a)') 'integrateggr_',Gamma,'.dat'
      Open(23,File=filename)

      Do I=1,Nbin

         Int1 = 0.0d0
         Int2 = 0.0d0
         Int3 = 0.0d0
         Int4 = 0.0d0

         Do J=1,I
            X  = (Dble(J)-0.5d0)/Dble(I)

            R2 = Delta*(((Dble(J)-0.5d0)*Delta)**2)
            
            
            F1 = 1.0d0 - 1.5d0*X + 0.5d0*X*X*X

            F2 = 1.0d0 - X*X*X

            F3 = 1.0d0 + 0.5d0*X*X*X
               
            Int1 = Int1 + (16.0d0*Datan(1.0d0))*R2*Ggg(J)*F1
            Int2 = Int2 + (16.0d0*Datan(1.0d0))*R2*Ggg(J)*F2
            Int3 = Int3 + (16.0d0*Datan(1.0d0))*R2*Ggg(J)*F3
            Int4 = Int4 + (16.0d0*Datan(1.0d0))*R2*Ggg(J)
         Enddo

         R2 = (8.0d0*Datan(1.0d0))*Ggg(I)*((Dble(I)*Delta)**3)

         Write(23,*) 1.0d0/(Dble(I)*Delta),Int1,Int2,Int3,Int4+R2,Int4
      Enddo
      
      Close(23)

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