def pos_eval(board,color):
    
    piece_val = {
        1: 10, #pawn
        2: 30, #knight
        3: 30, #bishop
        4: 50, #rook
        5: 90, #queen
        6: 900} #king
    
    legal_moves = board.legal_moves #list
    piece_map = board.piece_map() #dictionary
    
    findMax = true #white's turn 
    max = 0
    
    if(color == false): #if black's turn
        findMax = false
        min = 1000
    
    max_min_move = ""
    
    for move in legal_moves: #loop through all legal moves
        if(is_capture(move)): #if move is a capture
            end_square = move[-2:]
            piece_at_end = piece_map[end_square].piece_type
            score = piece_val[piece_at_end]
            
            if(findMax): #White's turn: find max score
                if(score > max):
                    max = score
                    max_min_move = move
            else: #black's turn: find min score
                if(score < min):
                    min = score
                    max_min_move = move
    
    return(max_min_move)
	
	
	

