class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        guess = init
        
        for i in range(iterations):
            print(guess)
            guess = guess - 2*guess * learning_rate
            print(guess)


            if guess>0 and init<0 or guess<0 and init>0:
                break

        return round(guess, 5)