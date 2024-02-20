CO = g++
TARGETS = Jacobi Gauss

.PHONY: all clean run

all: $(TARGETS)

counter: counter.cpp
	$(CO) -o $@ $^

NUM3: NUM3.cpp
	$(CO) -o $@ $^

run: all
	./Jacobi
	./Gauss
	python3 alternative.py
clean:
	rm -f $(TARGETS)
