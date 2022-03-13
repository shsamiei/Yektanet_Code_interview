from asyncio.format_helpers import _format_args_and_kwargs
import random



class XoGame : 

    def __init__(self):
        self.board = []
        pass

    def game_creator(self):
        for i in range(3):
            col = []
            for i in range(3):
                col.append('-')
            self.board.append(col)
        pass
    

    def get_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j]," " , end='')
            print()

    
    def fill_spot(self , row , col , player ):
            if self.is_full(row , col ):
                return False
            else : 
                self.board[row][col] = player
                return True
         

    def is_full(self , row , col):
        if self.board[row][col] != '-' :
            return True 
        else : 
            return False
        


    def is_board_fill(self):
        for row in self.board :
            for item in row :
                if item == '-' :
                    return False
        return True
    

    def is_player_win(self ,player):
        # here we have three condition to win the game :

        number_of_row_col = len(self.board)
        # row : 
        win = None 
       
        for i in range(number_of_row_col):
            win = True 
            for j in range(number_of_row_col):
                if self.board[j][i] != player :
                    win = False 
                    break
            if win :
                return win 


        # column :
        win = None
        for i in range(number_of_row_col):
            win = True
            for j in range(number_of_row_col):
                if self.board[i][j] != player :
                    win = False
                    break
            if win :
                return win

        # diagonal : 

        win = True 
        for i in range(number_of_row_col):
              if  self.board[i][i] != player :
                  win = False
                  break
        if win : 
            return win 


        win = True
        for i in range(number_of_row_col):
            if self.board[number_of_row_col - i - 1][i] != player :
                win = False
                break
        if win :
            return win 
            

    def get_random_player(self):
        return random.randint(0,1)
    
    def change_turn(self , player):
        return 'X' if player == 'O' else 'O'

    # def set_mode(self , mode_of_game):

            

    def game_runner(self):

        self.game_creator()
        player = 'X' if self.get_random_player == 1 else 'O'


        turn_of_game = 1

        while True :

            # print(f'player {player} turn :')
           # self.get_board()

            while True :

                # player turn :
                if turn_of_game :
                    print("its player time ! ")
                    row  , col = list (map (int , input("enter row ,col  :").split()))
                    if not self.is_full(row , col):
                             turn_of_game = 0 


                # server turn 
                else : 
                    print("its server time ! ")
                    row = random.randint(0,2) 
                    col = random.randint(0,2)
                    if  not self.is_full(row ,col) :
                        turn_of_game = 1



                if  self.fill_spot(row -1, col -1 , player):
                    break
                print('its not free cell ! ')

            # now we have three condition : 
            # win the game :
            if self.is_player_win(player) :
                print(f'player {player} win the game !')
                break

            # draw 
            if self.is_board_fill() :
                print("the game is draw ! ")
                break



            # continue
            player = self.change_turn(player)

            print()
            self.get_board()
            


game = XoGame()
game.game_runner()