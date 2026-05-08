# GUI Tic Tact Toe Project

# needs
# working TIC TAC TOE Logic - to play game
# GUI

import tkinter as tk


class Game_Logic():

    def __init__(self, root):
        """ Create the board for the game to be played onto
            Initilize most the game and all buttons onto the root"""

        self.root = root
        self.player_id = "X"
        for i in range(3):
            root.columnconfigure(i, weight=1)
            root.rowconfigure(i, weight=1)

        # create 2D array of buttons, commands when clicked to set its own symbol within its location
        self.board = [[tk.Button(self.root, text="-",
                                 command=lambda x=x, y=y:
                                 self.setSymbol(self.board[y][x]))
                       for x in range(3)] for y in range(3)]

        # output the board onto the root window so that it is visible to the user
        for y in range(3):
            for x in range(3):
                self.board[y][x].grid(row=y, column=x, sticky="nsew")

    def close_popup(self, root):
        """ Logic to destroy the new root of this pop up when parsed
            and to start a new game by calling its own class again - recursive till mainloop broken
            via closing the program """
        root.destroy()
        Game_Logic(self.root)

    def winner_popup(self, winner):
        """ Logic for a popup window to display winner letter and to close and restart the game """
        # create a new window
        new_root = tk.Tk()
        new_root.title("winner")
        new_root.geometry("200x100")
        new_root.columnconfigure(0, weight=1)
        new_root.rowconfigure(0, weight=1)
        winner += " Is the winner!!! \n click to close me \n and reset the game"
        # button to destroy this popup and restart the game
        (tk.Button(new_root, text=winner, command=lambda: self.close_popup(new_root))
         .grid(row=0, column=0, sticky="nsew"))

    def check_winner(self):
        """ check for winners on the vertical horizontal and diagonal axis """
        for letter in ["X", "O"]:
            for i in range(3):
                # Horizontal check
                if self.board[i][0]["text"] == letter and \
                        self.board[i][1]["text"] == letter and \
                        self.board[i][2]["text"] == letter:
                    self.winner_popup(letter)
                    return True
                # Vertical Check
                elif self.board[0][i]["text"] == letter and \
                        self.board[1][i]["text"] == letter and \
                        self.board[2][i]["text"] == letter:
                    self.winner_popup(letter)
                    return True
                # diagonal checks
                elif self.board[0][0]["text"] == letter and \
                        self.board[1][1]["text"] == letter and \
                        self.board[2][2]["text"] == letter:
                    self.winner_popup(letter)
                    return True
                elif self.board[0][2]["text"] == letter and \
                        self.board[1][1]["text"] == letter and \
                        self.board[2][0]["text"] == letter:
                    self.winner_popup(letter)
                    return True
        return False

    def setSymbol(self, button):
        """ button press function, when a button is pressed try and set the text of the button to the players
            symbol, every turn must check if a winner is found """

        if self.player_id == "X":
            button.config(text=self.player_id, state=tk.DISABLED, bg="blue")
            self.player_id = "O"
        elif self.player_id == "O":
            button.config(text=self.player_id, state=tk.DISABLED, bg="red")
            self.player_id = "X"
        else:
            print("unknown symbol detected, please close and reload the game")

        self.check_winner()


class Game_Runner():
    def __init__(self):
        root = tk.Tk()
        root.title("Tic Tac Toe")
        root.geometry("500x300")

        # initialize grid and main loop of the game
        Game_Logic(root)
        root.mainloop()

# to run GUI
if __name__ == "__main__":
    Game_Runner()