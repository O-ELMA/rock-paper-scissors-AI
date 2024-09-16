# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# Dictionary mapping moves to their respective symbols
MOVES = {'ROCK': 'R', 'PAPER': 'P', 'SCISSORS': 'S'}

# Dictionary defining the move that beats each move
BEATS = {
    MOVES['ROCK']: MOVES['PAPER'],  # Paper beats Rock
    MOVES['PAPER']: MOVES['SCISSORS'],  # Scissors beats Paper
    MOVES['SCISSORS']: MOVES['ROCK']  # Rock beats Scissors
}

# Default move to start with if no previous play
DEFAULT_FIRST_MOVE = MOVES['ROCK']


def player(prev_play, opponent_history=[], move_frequency={}):
    """
    Determine the next move based on the opponent's previous moves and known patterns.

    Args:
    - prev_play (str): The opponent's last move.
    - opponent_history (list): List of the opponent's previous moves.
    - move_frequency (dict): Frequency of observed 5-move sequences.

    Returns:
    - str: The next move to play.
    """
    # Use the default move in the beginning of the game
    if not prev_play:
        prev_play = DEFAULT_FIRST_MOVE

    # Add the previous play to the history
    opponent_history.append(prev_play)

    # Default move to start with if no pattern is detected
    next_move = MOVES['SCISSORS']

    # Check if there are enough moves to start analyzing data (more than 4 moves)
    if len(opponent_history) > 4:
        # Join the last 5 moves into a string
        last_five_moves = "".join(opponent_history[-5:])

        # Update the frequency of the 5-move sequence in the dictionary
        move_frequency[last_five_moves] = move_frequency.get(
            last_five_moves, 0) + 1

        # Generate all possible next 5-move sequences by adding each possible move
        possible_sequences = [
            "".join(opponent_history[-4:] + [move]) for move in MOVES.values()
        ]

        # Count the frequency of the generated sequences
        sequence_count = {
            sequence: move_frequency.get(sequence, 0)
            for sequence in possible_sequences
        }

        # If there are observed sequences, select the most frequent one
        if sequence_count:
            most_frequent_sequence = max(sequence_count,
                                         key=sequence_count.get)
            next_move = most_frequent_sequence[-1:]

    # Return the move that beats the predicted next move
    return BEATS[next_move]
