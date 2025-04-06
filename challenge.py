from random import randint

# todo break at any moment

LOWER_LIMIT = 1
UPPER_LIMIT = 100

FIRST_TURN_RANGE = 10

FIRST_TURN_HIT_MSG = "FUOCO!"
FIRST_TURN_MISS_MSG = "ACQUA!"

NEW_GUESS_CLOSE_MSG = "FUOCHERELLO!"
NEW_GUESS_FAR_MSG = "ACQUA!"

INVALID_INPUT_MSG = f"Il numero deve essere compreso tra {LOWER_LIMIT} e {UPPER_LIMIT}."



def guess_is_valid(guess):
    if LOWER_LIMIT <= guess <= UPPER_LIMIT:
        return True
    return False


class Match:
    def __init__(self, solution):
        self.current_guess = None
        self.prev_guess = None
        self.amount_of_guesses = 0
        self.solution = solution

    def get_player_guess(self):
        while True:
            try:
                guess = input("Inserisci il tuo numero\n'q' per uscire: ")
                if guess == 'q':
                    print("Hai abbandonato il gioco.")
                    exit()
                guess = int(guess)
                if not guess_is_valid(guess):
                    raise ValueError(INVALID_INPUT_MSG)
                self.amount_of_guesses += 1
                return guess
            except ValueError as e:
                print(e)

    def check_hit_or_miss(self, hit_condition, hit_msg, miss_msg):
        if self.current_guess == self.solution:
            return True
        if hit_condition:
            print(hit_msg)
        else:
            print(miss_msg)
        return False

    def print_win_msg(self):
        print(f"Hai vinto con {self.amount_of_guesses} tentativi!")

    def first_guess(self):
        self.current_guess = self.get_player_guess()
        return self.check_hit_or_miss((abs(self.current_guess - self.solution)  <= FIRST_TURN_RANGE), FIRST_TURN_HIT_MSG, FIRST_TURN_MISS_MSG)

    def guess(self):
        self.prev_guess = self.current_guess
        self.current_guess = self.get_player_guess()
        return self.check_hit_or_miss((abs(self.current_guess - self.solution) < abs(self.prev_guess - self.solution)), NEW_GUESS_CLOSE_MSG, NEW_GUESS_FAR_MSG)
        
    
def start_game():
    isPlaying = False
    hasWon = False
    round_number = 1

    while True:
        if hasWon:
            match.print_win_msg()
            new_game = input("Vuoi giocare un'altra partita? (s/n): ").lower()
            if new_game == 's':
                round_number += 1
                hasWon = False
                isPlaying = False
            else:
                print(f"Grazie per aver giocato {round_number} round!")
                exit()
        if not isPlaying:
            isPlaying = True
            print(f"ROUND #{round_number}")
            print(f"Indovina un numero tra {LOWER_LIMIT} e {UPPER_LIMIT}.")
            solution = randint(LOWER_LIMIT, UPPER_LIMIT)
            print("DEBUG: " + str(solution))
            match = Match(solution)
            hasWon = match.first_guess()
        else:
            while not hasWon:
                hasWon = match.guess()


start_game()
    