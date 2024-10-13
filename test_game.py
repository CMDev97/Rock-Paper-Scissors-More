import unittest
from io import StringIO
from unittest.mock import patch
import game
import constant


class TestGame(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user_rating_with_no_user_in_rating(self, mock_stdout):
        # Arrange
        ratings = {}
        user = "mario"

        # Act
        game.show_user_rating(user, ratings)

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "Your rating: 0")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user_rating_with_one_user(self, mock_stdout):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "mario"

        # Act
        game.show_user_rating(user, ratings)

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "Your rating: 500")

    def test_add_user_rating_with_one_user_with_loss_result(self):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "mario"
        result = constant.LOSS

        # Act
        game.add_user_rating(user, ratings, result)

        #assert
        self.assertEqual(ratings["mario"], 500)

    def test_add_user_rating_with_one_user_with_draw_result(self):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "mario"
        result = constant.DRAW

        # Act
        game.add_user_rating(user, ratings, result)

        # assert
        self.assertEqual(ratings["mario"], 550)

    def test_add_user_rating_with_one_user_with_win_result(self):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "mario"
        result = constant.WIN

        # Act
        game.add_user_rating(user, ratings, result)

        # assert
        self.assertEqual(ratings["mario"], 600)

    def test_add_user_rating_with_no_user_with_win_result(self):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "cris"
        result = constant.WIN

        # Act
        game.add_user_rating(user, ratings, result)

        # assert
        self.assertEqual(ratings["cris"], 100)

    def test_add_user_rating_with_no_user_with_draw_result(self):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "cris"
        result = constant.DRAW

        # Act
        game.add_user_rating(user, ratings, result)

        # assert
        self.assertEqual(ratings["cris"], 50)

    def test_add_user_rating_with_no_user_with_loss_result(self):
        # Arrange
        ratings = {
            "mario": 500
        }
        user = "cris"
        result = constant.LOSS

        # Act
        game.add_user_rating(user, ratings, result)

        # assert
        self.assertEqual(ratings["cris"], 0)

    @patch('builtins.input', side_effect=["Mario"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_read_user_info_with_name(self, mock_stdout, mock_input):
        # Act
        user_name = game.read_user_info()

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, Mario")
        self.assertEqual(user_name, "Mario")

    @patch('builtins.input', side_effect=["1234"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_read_user_info_with_number(self, mock_stdout, mock_input):
        # Act
        user_name = game.read_user_info()

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, 1234")
        self.assertEqual(user_name, "1234")

    def test_evaluate_hand_with_draw(self):
        # Arrange
        options = ['rock', 'paper', 'scissors']
        user_command = 'paper'
        computer_command = 'paper'

        # Act
        result = game.evaluate_hand(options, user_command, computer_command)

        # Assert
        self.assertEqual(constant.DRAW, result)

    def test_evaluate_hand_with_loss(self):
        # Arrange
        options = ['rock', 'paper', 'scissors']
        user_command = "paper"
        computer_command = "scissors"

        # Act
        result = game.evaluate_hand(options, user_command, computer_command)

        # Assert
        self.assertEqual(constant.LOSS, result)

    def test_evaluate_hand_with_win(self):
        # Arrange
        options = ['rock', 'paper', 'scissors']
        user_command = "rock"
        computer_command = "scissors"

        # Act
        result = game.evaluate_hand(options, user_command, computer_command)

        # Assert
        self.assertEqual(constant.WIN, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result_hand_with_result_win(self, mock_stdout):
        # Arrange
        computer_command = "scissors"
        result = constant.WIN

        # Act
        game.print_result_hand(result, computer_command)

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "Well done. The computer chose scissors and failed")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result_hand_with_result_loss(self, mock_stdout):
        # Arrange
        computer_command = "scissors"
        result = constant.LOSS

        # Act
        game.print_result_hand(result, computer_command)

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "Sorry, but the computer chose scissors")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result_hand_with_result_draw(self, mock_stdout):
        # Arrange
        computer_command = "scissors"
        result = constant.DRAW

        # Act
        game.print_result_hand(result, computer_command)

        # Assert
        self.assertEqual(mock_stdout.getvalue().strip(), "There is a draw (scissors)")

    @patch('builtins.input', side_effect=['xxx', 'scissors'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_command(self, mock_stdout, mock_input):
        # Arrange
        validation = ["scissors", "rock", constant.EXIT, constant.RATING]
        # Act
        result = game.get_user_command(validation)

        # Assert
        self.assertIn("Invalid input", mock_stdout.getvalue())
        self.assertEqual(result, 'scissors')

    @patch('builtins.input', side_effect=['rock,fire,scissors,sponge,paper,air,water'])
    def test_input_game_options_with_new_options(self, mock_input):
        # Arrange
        options_assert = ['rock', 'fire', 'scissors', 'sponge', 'paper', 'air', 'water']

        # Act
        result = game.input_game_options()

        # Assert
        self.assertEqual(options_assert, result)

    @patch('builtins.input', side_effect=['    '])
    def test_input_game_options_with_spacing_string(self, mock_input):
        # Arrange
        options_assert = constant.SIMPLE_GAMES

        # Act
        result = game.input_game_options()

        # Assert
        self.assertEqual(options_assert, result)

    @patch('builtins.input', side_effect=[''])
    def test_input_game_options_with_empty_string(self, mock_input):
        # Arrange
        options_assert = constant.SIMPLE_GAMES

        # Act
        result = game.input_game_options()

        # Assert
        self.assertEqual(options_assert, result)

    @patch('builtins.input', side_effect=['xxx, xxx', "xxx, xxxx, xxxxx"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_input_game_options_with_only_two_options(self, mock_stdout, mock_input):
        # Act
        result = game.input_game_options()

        # Assert
        self.assertEqual("Invalid input", mock_stdout.getvalue().strip())
        self.assertEqual(['xxx', 'xxxx', 'xxxxx'], result)

    def test_get_validation_command(self):
        # Arrange
        games = ['rock', 'fire', 'scissors', 'sponge', 'paper', 'air', 'water']
        validation_commands_assert = list(games)
        validation_commands_assert.extend(constant.OTHER_COMMAND)

        # Act
        result = game.get_validation_command(games)

        # Assert
        self.assertEqual(validation_commands_assert, result)

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="")
    def test_read_file_to_dictionary_when_file_is_empty(self, mock_file):
        # Act
        result = game.read_file_to_dictionary()

        # Assert
        mock_file.assert_called_once_with(constant.RATING_FILE, 'r')
        self.assertEqual(result, {})

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="Tim 234\n cris 0\n")
    def test_read_file_to_dictionary_when_file_not_empty(self, mock_file):
        # Arrange
        rating_assert = {
            "Tim": 234,
            "cris": 0
        }
        # Act
        result = game.read_file_to_dictionary()

        # Assert
        mock_file.assert_called_once_with(constant.RATING_FILE, 'r')
        self.assertEqual(result, rating_assert)

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_new_ratings(self, mock_file):
        # Arrange
        ratings = {
            "Mario": 1500,
            "Luigi": 1200,
            "Peach": 1600
        }

        # Act
        game.save_new_ratings(ratings)

        # Assert
        mock_file.assert_called_once_with(constant.RATING_FILE, 'w')
        mock_file_handle = mock_file()
        mock_file_handle.write.assert_any_call('Mario 1500\n')
        mock_file_handle.write.assert_any_call('Luigi 1200\n')
        mock_file_handle.write.assert_any_call('Peach 1600\n')


if __name__ == "__main__":
    unittest.main()