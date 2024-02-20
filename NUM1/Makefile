#
# make: all, clean, tar, run
#
#=========================================================================
DIR = `basename $(CURDIR)`
#------------------------
NAME1 = num1
#----------------------
EXEC1 = $(NAME1)
OBJS1 = $(NAME1).o
#############################
COFLAGS = -O
LDFLAGS = -O
CO = g++
LD = $(CO)
#############################
%.o: %.cpp
	$(CO) $(COFLAGS) -c $<
#############################
.PHONY: all
all: $(EXEC1)
#############################
$(EXEC1): $(OBJS1)
	 $(LD) -o $@ $(LDFLAGS) $^
#############################
.PHONY: clean tar
# Porzadki
EXECS = $(EXEC1)
clean:                                                     
	rm -f *.o  *~ $(EXECS) rm output.txt
#=========================================================================
# Archiwizacja i kompresja
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz  $(DIR) )
#=========================================================================
# Uruchamianie i porownanie pliku wejscia i wyjscia
run:
	(./num1;)
#=========================================================================
