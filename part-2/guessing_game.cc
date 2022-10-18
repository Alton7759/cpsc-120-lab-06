// Christian Alton Bonilla
// CPSC 120-01
// 2022-10-12
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 06-02
// Partners: @jaylinmai
//
// guessing game
//

#include <cmath>
#include <iostream>
#include <string>

int k_secret_number = 42;
int main(int argc, char const *argv[]) {
  int guess = 0;
  int last_guess = 0;
  std::string answer;
  bool is_game_over{false};

  std::cout << "Hi - I'm a computer and I've thought of a number between "
               "1 and 100.\n";
  std::cout << "Let's play a guessing game...\n";
  while (!is_game_over) {
    std::cout << "What's your guess?> ";
    std::cin >> guess;

    if (k_secret_number == guess) {
      std::cout << "Hooray! You guessed the secret number!!\n";
      std::cout << "Do you want to play again? (y or n)> ";
      std::cin >> answer;
      if (answer == "n") {
        return 0;
      }
    }

    if (std::abs(k_secret_number - guess) <
        std::abs(k_secret_number - last_guess)) {
      std::cout << "You're getting warmer!\n";
    } else {
      std::cout << "You're getting colder.\n";
    }
    last_guess = guess;
  }
  return 0;
}
