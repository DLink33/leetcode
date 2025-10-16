cmake_minimum_required(VERSION 3.15)
project(app CXX)

# Toolchain & language
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON) # gnu++17 (good on Linux)

# Warnings (tuned for g++ 11.x)
add_compile_options(
  -Wall -Wextra -Wpedantic
  -Wshadow -Wconversion -Wsign-conversion
  -fno-omit-frame-pointer
)

# Optionally enable sanitizers in Debug
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  add_link_options(-fsanitize=address,undefined)
  add_compile_options(-O1 -fsanitize=address,undefined)
endif()

# ---- Library with your logic ----
add_library(app_lib
  src/solution.cpp
)
target_include_directories(app_lib PUBLIC ${CMAKE_SOURCE_DIR}/include)

# ---- App executable ----
add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE app_lib)

# ---- Tests (Catch2 via FetchContent) ----
include(FetchContent)
FetchContent_Declare(
  catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v3.6.0
)
FetchContent_MakeAvailable(catch2)

add_executable(tests tests/test_solution.cpp)
target_link_libraries(tests PRIVATE app_lib Catch2::Catch2WithMain)

include(CTest)
include(Catch)
catch_discover_tests(tests)  # enables `ctest`

