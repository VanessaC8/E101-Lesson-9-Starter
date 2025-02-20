import unittest
from main import play_game

class test_RPSGame(unittest.TestCase):
  def test_play_game_player_loses(self):
    self.assertEqual(play_game("Rock","Paper"),"You lose!")

  def test_play_game_player_wins(self):
    self.assertEqual(play_game("Rock","Scissors"),"You win!")

  def test_play_game_tie(self):
    self.assertEqual(play_game("Rock","Rock"),"It's a tie!")


if __name__ =="__main__":
  unittest.main()
