CO = g++
TARGETS = counter NUM3

.PHONY: all clean run

all: $(TARGETS)

counter: counter.cpp
	$(CO) -o $@ $^

NUM3: NUM3.cpp
	$(CO) -o $@ $^

run: all
	./NUM3 124
	./counter
	python3 NUM3_alt.py

clean:
	rm -f $(TARGETS) output.txt
