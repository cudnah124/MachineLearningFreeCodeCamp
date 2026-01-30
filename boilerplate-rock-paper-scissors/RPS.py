# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return 'R'  
    else:
        context = ''.join(opponent_history[-3:])
        for i in range(3):
            if context in ''.join(opponent_history):
                indices = [i for i in range(len(opponent_history) - 3) if ''.join(opponent_history[i:i + 3]) == context]
                next_moves = [opponent_history[i + 3] for i in indices if i + 3 < len(opponent_history)]
                if next_moves:
                    predicted_move = max(set(next_moves), key=next_moves.count)
                    if predicted_move == 'R':
                        return 'P'  
                    elif predicted_move == 'P':
                        return 'S'
                    else:
                        return 'R'  
        
        return opponent_history[-3] 
    


    
