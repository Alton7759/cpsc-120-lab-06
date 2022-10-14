
// TODO: Insert your header.

#include <cmath>
#include <iostream>
#include <string>

// TODO: Declare a const int named kSecretNumber and initialize it to 42.

int main(int argc, char const *argv[]) {
  int guess = 0;
  int last_guess = 0;
  std::string answer;

  std::cout << "Hi - I'm a computer and I've thought of a number between "
               "1 and 100.\n";
  std::cout << "Let's play a guessing game...\n";

  // TODO: Write an loop that will continue until the player decides to quit
  // TODO: Inside the loop, prompt the player for their guess
  //       for example     std::cout << "What's your guess?> ";
  //       If the player enters a number less than 1 or greater than 100, prompt
  //       the player to enter a number again. You can do this with another
  //       loop.
  // TODO: Store the input from the keyboard into the variable guess
  // TODO: Check to see if guess has the same value as kSecretNumber
  //       If so, then the player has won and they can play again
  //       Prompt the player if they would like to continue playing. If the
  //       answer is "y" then restart the game. Otherwise, any other letter will
  //       cause the game to end and the program to exit.
  // TODO: Else, the player didn't win so they need to know if they are
  //       getting warmer or colder.
  //       Check to see if kSecretNumber - guess is less than kSecretNumber -
  //       last_guess If it is, print you're getting warmer. Otherwise, print
  //       you're getting colder.
  // TODO: At the end of every iteration of the loop, save the current guess
  //       into the variable last_guess.

  return 0;
}