AMBEM2: AMBEM2.o AMBEM2_T.o GEOM2D.o H2LC.o CGLS.o INTEIG.o CGEIG.o FNHANK.o
	gfortran -L../gsl/lib -o AMBEM2 AMBEM2.o AMBEM2_T.o GEOM2D.o H2LC.o CGLS.o INTEIG.o CGEIG.o FNHANK.o -lfgsl -lgsl -lgslcblas

AMBEM2.o: AMBEM2.FOR
	gfortran -c AMBEM2.FOR

AMBEM2_T.o: AMBEM2_T.FOR
	gfortran -c AMBEM2_T.FOR

GEOM2D.o: ../SHARED/GEOM2D.FOR
	gfortran -c ../SHARED/GEOM2D.FOR

H2LC.o: ../SHARED/H2LC.FOR
	gfortran -c ../SHARED/H2LC.FOR

CGLS.o: ../SHARED/CGLS.FOR
	gfortran -c ../SHARED/CGLS.FOR

INTEIG.o: ../SHARED/INTEIG.FOR
	gfortran -c ../SHARED/INTEIG.FOR

CGEIG.o: ../SHARED/CGEIG.FOR
	gfortran -c ../SHARED/CGEIG.FOR

FNHANK.o: ../SHARED/FNHANK.FOR
	gfortran -I../gsl/include/fgsl -c ../SHARED/FNHANK.FOR

clean:
	rm AMBEM2 AMBEM2.OUT AMBEM2.o AMBEM2_T.o GEOM2D.o H2LC.o CGLS.o INTEIG.o CGEIG.o FNHANK.o *~
