class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        guess = init
        
        for i in range(iterations):
            guess = guess - 2*guess * learning_rate

            if init-guess<0:
                break

        return round(guess, 5)