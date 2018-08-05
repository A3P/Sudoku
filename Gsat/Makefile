CFLAGS = -O2

LIB    =   -lm

SOURCES = gsat.c anneal.c urand.c  utils.c globals.c
HEADERS = gsat.h anneal.h urand.h utils.h proto.h adjust_bucket.h
OBJECTS = urand.o gsat.o globals.o anneal.o utils.o
AUX = Makefile GSAT_USERS_GUIDE gsat.1 ex.wff

gsat: $(SOURCES) $(HEADERS)
	gcc $(CFLAGS) $(SOURCES) $(LIB) -o gsat

clean:
	'rm' -f gsat *.o

tar:
	'rm' -f gsat.tar.Z*
	tar cvof gsat.tar $(SOURCES) $(HEADERS) $(AUX)
	compress gsat.tar
	uuencode gsat.tar.Z gsat.tar.Z > gsat.tar.Z.uu



