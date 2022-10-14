# Guessing Game

Let's write a guessing game where the player must guess a secret number between 1 and 100. Since we don't know how to generate random numbers and working with random numbers are unpredictable, we will always have the same secret number.

The goal of this exercise is to master the use of loops.

Your main function shall have an almost infinite loop. The only way to exit out of the almost infinite loop is if the player wins and then chooses to exit the game by refusing to play again.

There are two ways you can control an almost infinite loop.

The first is to create a boolean variable like `is_game_over` and set it to `false`. Then in your loop check to see if `not is_game_over` is true. If it is true, continue playing the game. If it turns out to be false, then the player doesn't want to continue.

For example, let's imagine we want to loop until the player enters `"n"`.

```c++
bool is_game_over{false};
std::string input;
while (!is_game_over) {
    std::cin >> input;
    if (input == "n") {
        is_game_over = true;
    }
}
```

The second approach is to write a `while` or `do-while` loop where the condition is always true. Let's say we want a `do-while` loop that is truly infinite.
```c++
do {
	std::cout << "This will go on forever!\n";
} while (true);
```

There is no way to escape this loop and the computer user must kill the program. (Remember, to kill a program press control key and the 'c' key at the same time.) There is a C++ keyword named [`break`](https://en.cppreference.com/w/cpp/language/break) which breaks you out of a loop.

```c++
do {
	break;
	std::cout << "This will go on forever!\n";
} while (true);
```

Placing a break in our infinite loop turns it into a loop that does not even run. This is because the moment the computer sees the break instruction, the computer jumps out of the loop.

The first approach is the best approach because the logic is clear and it tends to create a more readable programs.

Inside the loop, the player will be prompted to enter guesses. As the player guesses, keep track of their current guess and their last guess using variables. If their current guess gets the player closer to the secret number than their last guess then they are getting warmer. If their current guess is further way from the secret number than the last guess then they are getting colder. Give these hints to the player as they make guesses to help the game along.

To calculate if the player's guesses are getting warmer or colder, consider the distance from the guess to the secret number. Mathematically, you can think of distance as the absolute value of the difference between the secret number and a given guess. When the distance decreases from the last guess to the current guess, then the player is getting warmer. Otherwise, the player is getting colder.

Let's imagine that the secret number is 10. The player's last guess was 2 and the player just guess 7. Clearly, the player is getting warmer because their new guess 7 is closer to 10 than the old guess. We can understand this mathematically by thinking of the distance from 2 to 10 as $|10 - 2|$ which means the absolute value of 10 minus 2. (Notice that the distance from 2 to 10 is the same as the distance from 10 to 2 because $|10 - 2| = |2 - 10|$.) The other distance is to the player's new guess which is $|10 - 7|$. Because $|10 - 7| \lt |10 - 2|$, the new guess is _warmer_.

We should consider a new guess as warmer strictly when the distance has decreased from the last guess. This means that if the player guesses 2, then 7, then 7 again, the program will answer _warmer_ the first time 7 is guessed and _colder_ the second time 7 is guessed.

In C++, the find the absolute value, you use the function [`std::abs()`](https://en.cppreference.com/w/cpp/numeric/math/abs).

Putting all these ideas together, you can write it in C++ similar to the example given below.

```c++
if (std::abs(secret_number - current_guess) < std::abs(secret_number - last_guess)) {
    std::cout << "You're getting warmer!\n";
} else {
    std::cout << "You're getting colder.\n";
}
```

And remember, if the player guesses a number outside of the range allowed in the game

## Requirements

The entire game runs within a loop in the main function. The loop continues until the player wins and chooses to exit.

The player is only allowed to guess numbers between 1 and 100.

The secret number the player is trying to guess is 42. This must be stored as a `const int` named `kSecretNumber`.

Declare two variables, `guess` and `last_guess` to keep track of the player's guesses. Initialize both to zero. After every guess, assign the value of guess to last_guess so that the game knows what the player is guessing currently and has guessed previously. This is needed to figure out if the player is getting warmer or colder.

You shall use [cout](https://en.cppreference.com/w/cpp/io/cout) to print messages to the terminal.

Whenever a guess is made that is incorrect, print out a message saying the guess was incorrect.

If the guess is incorrect, print a message hinting at which direction (greater or lesser than the current guess) the player should guess.

The starting code defines a series of `TODO` comments which you can use to formulate your plan and develop your program.

Write your program progressively. Compile your program often and check that you're making progress. Make sure your program behaves the way you expect.

The output of your program must match the output given in the section Example Output below.

To compile your program, you use the `make` command. A Makefile is provided for this exercise.

The Makefile has the following targets:
  
* all: builds the project
* clean: removes object and dependency files
* spotless: removes everything the clean target removes and all binaries
* format: outputs a [`diff`](https://en.wikipedia.org/wiki/Diff) showing where your formatting differes from the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)
* lint: output of the [linter](https://en.wikipedia.org/wiki/Lint_(software)) to give you tips on how to improve your code
* header: check to make sure your files have the appropriate header
* test: run tests to help you verify your program is meeting the assignment's requirements. This does not grade your assignment.

## Don't Forget

Please remember that:

- You need to put a header in every file.
- You need to follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).
- Remove the `TODO` comments.

## Testing Your Code

Computers only ever do exactly what they are told, exactly the way they are told it, and never anything else. Testing is an important process to writing a program. You need to test for the program to behave correctly and test that the program behaves incorrectly in a predictable way.

As programmers we have to remember that there are a lot of ways that we can write the wrong program and only one to a few ways to write the correct program. We have to be aware of [cognitive biases](https://en.wikipedia.org/wiki/List_of_cognitive_biases) that we may exercise that lead us to believe we have correctly completed our program. That belief may be incorrect and our software may have errors. [Errors in software](https://www.wired.com/2005/11/historys-worst-software-bugs/) may lead to loss of [life](https://www.nytimes.com/2019/03/14/business/boeing-737-software-update.html), [property](https://en.wikipedia.org/wiki/Mariner_1), [reputation](https://en.wikipedia.org/wiki/Pentium_FDIV_bug), or [all of the above](https://en.wikipedia.org/wiki/2009%E2%80%9311_Toyota_vehicle_recalls).

### Test strategy

Start simple, and work your way up. Good tests are specific, cover a broad range of fundamentally different possibilities, can identify issues quickly, easily, and directly, without need for much set up, and can almost be diagnosed by inspection if the code fails to execute the test correctly.

## Example Input and Output

Please ensure your program's output is identical to the example below.

```
$ make 
set -e; clang++ -MM -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -D AMD64 guessing_game.cc \
| sed 's/\(guessing_game\)\.o[ :]*/\1.o guessing_game.d : /g' > guessing_game.d; \
[ -s guessing_game.d ] || rm -f guessing_game.d
clang++ -g -O3 -Wall -pedantic -pipe -std=c++17 -D LINUX -D AMD64 -c guessing_game.cc
clang++ -g -O3 -Wall -pedantic -pipe -std=c++17 -o guessing_game guessing_game.o 
$ ./guessing_game 
Hi - I'm a computer and I've thought of a number between 1 and 100.
Let's play a guessing game...
What's your guess?> 42
	Hooray! You guessed the secret number!!
Do you want to play again? (y or n)> n
$ ./guessing_game 
Hi - I'm a computer and I've thought of a number between 1 and 100.
Let's play a guessing game...
What's your guess?> -1
Please guess a number between 1 and 100.
What's your guess?> -2
Please guess a number between 1 and 100.
What's your guess?> -3
Please guess a number between 1 and 100.
What's your guess?> -4
Please guess a number between 1 and 100.
What's your guess?> 42
	Hooray! You guessed the secret number!!
Do you want to play again? (y or n)> y
Great!! I'd love to play again...
What's your guess?> 101
Please guess a number between 1 and 100.
What's your guess?> 102
Please guess a number between 1 and 100.
What's your guess?> 103 
Please guess a number between 1 and 100.
What's your guess?> 42
	Hooray! You guessed the secret number!!
Do you want to play again? (y or n)> n
$ ./guessing_game 
Hi - I'm a computer and I've thought of a number between 1 and 100.
Let's play a guessing game...
What's your guess?> 1
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 2
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 3
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 4
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 5
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 42
	Hooray! You guessed the secret number!!
Do you want to play again? (y or n)> n
$ ./guessing_game 
Hi - I'm a computer and I've thought of a number between 1 and 100.
Let's play a guessing game...
What's your guess?> 1
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 100
	Nope - that's not it.
	You're getting colder.
What's your guess?> 2
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 99
	Nope - that's not it.
	You're getting colder.
What's your guess?> 3
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 98
	Nope - that's not it.
	You're getting colder.
What's your guess?> 4
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 97
	Nope - that's not it.
	You're getting colder.
What's your guess?> 42
	Hooray! You guessed the secret number!!
Do you want to play again? (y or n)> n
$ ./guessing_game 
Hi - I'm a computer and I've thought of a number between 1 and 100.
Let's play a guessing game...
What's your guess?> 1
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 3
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 3
	Nope - that's not it.
	You're getting colder.
What's your guess?> 7
	Nope - that's not it.
	You're getting warmer!
What's your guess?> 7
	Nope - that's not it.
	You're getting colder.
What's your guess?> 42
	Hooray! You guessed the secret number!!
Do you want to play again? (y or n)> n
$ 
```

## What to Do

1. With your partner, edit the `guessing_game.cc` source file using VS Code. Add the required header. Replace all the TODO comments with working code.
1. Compile your program with the `$ make` shell command. Use the **debug compile error** procedure to debug any compile errors.
1. Run your program with the `$ ./guessing_game` shell command.
1. Test that your program passes all of the test cases in the test suite above. If your program suffers a runtime error, use the **debug runtime error** procedure to debug the error. If your program does not produce the expected output, use the **debug logic error** procedure to debug the error.
1. Test your program against automated test with the `$ make test` command. Debug any runtime errors or logic errors using the same procedures.
1. Check your header with the `$ make header` shell command. Correct any errors.
1. Check for format errors with the `$ make format` shell command. Correct any errors.
1. Check for lint errors with the `$ make lint` shell command. Correct any errors.
1. After your program passes all of these tests and checks, push your code to GitHub. Use the usual trio of commands: `git add`, `git commit`, and `git push`.

## Next Steps

After you have pushed your code, you are done with this lab. You may ask your TA for permission to sign out and leave.

