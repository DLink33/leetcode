# Simple Makefile for:
# include/solution.hpp
# src/main.cpp src/solution.cpp

PROJECT ?= remove_dups
CXX      ?= g++
CXXFLAGS ?= -std=c++17 -Wall -Wextra -O2 -Iinclude

SRC := src/main.cpp src/solution.cpp
OBJ := $(SRC:src/%.cpp=build/%.o)
BIN := bin/$(PROJECT)

all: $(BIN)

$(BIN): $(OBJ) | bin
	$(CXX) $(OBJ) -o $@

build/%.o: src/%.cpp | build
	$(CXX) $(CXXFLAGS) -c $< -o $@

build:
	mkdir -p build

bin:
	mkdir -p bin

run: all
	./$(BIN)

clean:
	rm -rf build bin

help:
	@echo "make          - build the project"
	@echo "make run      - build and run ./$(BIN)"
	@echo "make clean    - remove build artifacts"
	@echo "make help     - show this help"

.PHONY: all run clean help
