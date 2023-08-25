'''import modules'''
import unittest
import random
import game


class MyTestCase (unittest.TestCase):
    '''Class for unit test'''
    game.is_from_test=True
    random.seed(52) #seed to produce the same number making it easier to test
    num= game.number_generator() #call the actual function

    def test_number_generator(self):
        '''This function tests if the number generator is generating numbers'''
        print(self.num)
        self.assertIsNotNone(self.num)
        self.assertEqual(self.num,5396)

    def test_check_if_user_is_quitting(self):
        '''This function tests if the user is quitting'''
        input1=''
        input2='1'
        output1 = game.check_if_user_is_quitting(input1)
        output2= game.check_if_user_is_quitting(input2)
        self.assertEqual(output1, True)
        self.assertEqual(output2, False)


    def test_check_if_valid_input(self):
        '''This functions tests if the input is valid'''
        input1='a'
        input2='!!'
        input3='111'
        input4='1235'
        input5='7281'
        output1 = game.check_if_valid_input(input1)
        output2= game.check_if_valid_input(input2)
        output3 = game.check_if_valid_input(input3)
        output4= game.check_if_valid_input(input4)
        output5= game.check_if_valid_input(input5)
        self.assertEqual(output1, False)
        self.assertEqual(output2, False)
        self.assertEqual(output3, False)
        self.assertEqual(output4, True)
        self.assertEqual(output5, True)

    def test_guessing_hints(self):
        '''This functions tests if the input is equal to the generated random number''' 
        #Our number is 5396 with the seed
        input1='1234'
        input2='7286'
        input3 = '4821'
        input4 = '9276'
        input5 = '9536'
        input6 = '5396'

        game_output1 = game.check_if_correct_guess(input1)[1]
        game_output2 = game.check_if_correct_guess(input2)[1]
        game_output3 = game.check_if_correct_guess(input3)[1]
        game_output4 = game.check_if_correct_guess(input4)[1]
        game_output5 = game.check_if_correct_guess(input5)[1]
        game_output6 = game.check_if_correct_guess(input6)[1]

        # self.assertEqual(game_output1, ["_","circle","_","_"])
        self.assertEqual(game_output1, ["_", "_", "x", "_"])
        self.assertEqual(game_output2, ["_", "_", "_", "circle"])
        self.assertEqual(game_output3, ["_", "_", "_" ,"_"])
        self.assertEqual(game_output4, ["x", "_", "_", "circle"])
        self.assertEqual(game_output5, ["x", "x", "x", "circle"])
        self.assertEqual(game_output6, ["circle", "circle", "circle", "circle"])

if __name__ == '__main__':
    unittest.main ()
