


# TODO: Make the printing look nice

class Volleyball:
    def __init__(self, input_players: list):
        
        self._player_list = self._turn_title(input_players)
        self._starting_player_list = input_players


    def _turn_title(self, input_list: list):
        return [each_string.title() for each_string in input_list]
        

    def rotate(self) -> None:
        """Rotates the players in the list like a volleyball game rotation"""
        self._player_list.insert(0, self._player_list.pop(len(self._player_list)-1))
        

    def get_subs(self) -> list:
        """Returns the current subsitutes in the rotation"""
        return list(self._player_list[3], self._player_list[7])


    def get_active_line_only(self) -> list:
        """Returns the current active players on the field"""
        temp_list = self._player_list[:]

        # TODO: need to check for how many players there are first
        # Removes the sub list
        temp_list.pop(6)
        temp_list.pop(len(temp_list)-3)
        
        return temp_list

    
    def get_full_cycle_rotation(self) -> list:
        """Returns a list of lists for each rotation available"""
        temp_list = []

        for _ in range(len(self._starting_player_list)):
            temp_list.append(str(self._player_list))
            self.rotate()

        # To fix the rotation back to normal
        self.rotate()

        return temp_list


    def get_starting_line(self) -> list:
        """Returns starting 6 players position"""
        return self._starting_player_list


    def get_current_rotation(self) -> list:
        """Returns the current curation of players"""
        return self._player_list


    def remove_player(self, player_name: str) -> None:
        """Removes player from the current rotation"""
        
        try:
            if player_name.title() in self._player_list:
                self._player_list.remove(player_name.title())

            if len(self.get_active_line_only()) < 6:
                print('Now you don\'t have enough players')
                
        except ValueError:
            print('Sorry that player doesn\'t exist')



if __name__ == '__main__':
    game = Volleyball(['Gabby', 'Connor', 'maGgie', 'Clark', 'Cooper', 'Rossi', 'Asa', 'Cece'])

    print(game.get_active_line_only())

    game.remove_player('MagGiE')

    print(game.get_active_line_only())



