// Christian Alton Bonilla
// CPSC 120-01
// 2022-10-12
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 06-01
// Partners: @person
//
// makes a cool pattern
//

#include <iostream>

const int kCounterMax{22};

int main(int argc, char const *argv[]) {
  int thecount = 0;
  for (int i = 0; i < kCounterMax; i++) {
    for (int dash = 0; dash < thecount; dash++) {
      std::cout << "-";
    }
    std::cout << "*";
    for (int line = 22; line > thecount; line -= 1) {
      std::cout << "|";
    }
    std::cout << "\n";
    thecount++;
  }
  return 0;
}
