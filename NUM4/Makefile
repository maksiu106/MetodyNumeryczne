CO = g++
TARGETS = counter NUM4

.PHONY: all clean run

all: $(TARGETS)

counter: counter.cpp
	$(CO) -o $@ $^

NUM3: NUM3.cpp
	$(CO) -o $@ $^

run: all
	./NUM4 80
	./counter
	python3 NUM4_alt.py

clean:
	rm -f $(TARGETS)
