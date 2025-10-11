### LEETCODE PRACTICE MAKEFILE ###

# COMPILATION STAGES (example CLI for learning)
# 1) Preprocessing:  gcc -E main.c -Iinclude -DMODE=1 -o main.i
# 2) Compilation:    gcc -S main.i -std=c11 -O2 -o main.s
# 3) Assembly:       gcc -c main.s -o main.o
# 4) Linking:        gcc main.o utils.o -o app -L/path/to/libs -lm

# --- Tool & flags ---
CC        := gcc                      # C compiler
CFLAGS    := -Wall -Wextra -Wpedantic -std=c11 -O0 -g -MMD -MP
# -Wall/-Wextra: common warnings; -Wpedantic: ISO diagnostics
# -std=c11: C standard; -O0: no opt (debug); -g: debug symbols
# -MMD -MP: emit header dependency files (.d) for Make

CPPFLAGS  := -Iinclude -DMODE=1       # add project headers & an example macro

# --- Layout ---
SRC_DIR   	:= src
INCLUDE_DIR := include
BUILD_DIR 	:= build

# --- Sources / objects / deps ---
SRCS := $(wildcard $(SRC_DIR)/*.c)                          # all .c in src/
OBJS := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SRCS)) # map to build/*.o
DEPS := $(OBJS:.o=.d)                                       # matching .d files

# --- Final binary ---
TARGET := $(BUILD_DIR)/sol

# Default target: build the binary
.PHONY: all
# Default to running the test target (safe when sources don't provide a demo main)
all: test

# Link: make build/sol from objects
$(TARGET): $(OBJS)
	@mkdir -p $(@D)
	$(CC) -o $@ $(OBJS)

# Compile: make build/*.o from src/*.c
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(@D)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Include header dependency files if present
-include $(DEPS)

# Utilities
.PHONY: run clean
# Running tests is the safe default run action (test provides a runnable main)
run: test

TEST_SRC := $(wildcard test/*.c)
TEST_OBJS := $(patsubst test/%.c,$(BUILD_DIR)/%.o,$(TEST_SRC))

# Build test objects
$(BUILD_DIR)/%.o: test/%.c
	@mkdir -p $(@D)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Link test binary (links implementation object and test object(s))
.PHONY: test
test: $(OBJS) $(TEST_OBJS)
	@mkdir -p $(BUILD_DIR)
	$(CC) -o $(BUILD_DIR)/test_runner $(OBJS) $(TEST_OBJS)
	$(BUILD_DIR)/test_runner

clean:                        # remove all build outputs
	rm -rf $(BUILD_DIR)

# EOF
