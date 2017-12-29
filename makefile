all:type_inspection
type_inspection:main.cpp utils.cpp
	g++ -o type_inspection utils.cpp main.cpp
main.cpp:
	python gen.py
dumper.h:
	python gen.py

clean:
	rm type_inspection main.cpp dumper.h
