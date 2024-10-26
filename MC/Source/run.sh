#!/bin/bash

NAME='maxbin_2000.exe'

touch ./COMPILE-debug
touch ./COMPILE

echo "#!/bin/bash" > ./COMPILE-debug
echo "#!/bin/bash" > ./COMPILE

echo "gfortran -C -g -ffixed-line-length-132 -static *.f -o $NAME" >> ./COMPILE-debug

echo "gfortran -O3 -ffixed-line-length-132 -static *.f -o $NAME" >> ./COMPILE-debug

./COMPILE-debug
./COMPILE
