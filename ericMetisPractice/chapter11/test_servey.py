from survey import  AnonymousSurvey;
import unittest;

class survey_test(unittest.TestCase):

    def setUp(self):
        question = 'What language do you speak?';
        self.my_survey = AnonymousSurvey(question);
        self.responses = ['English' , 'Chineese' , 'Spain'];
         

    def test_store_single_response(self):
        self.my_survey.store_response('English');
        self.assertIn('English', self.my_survey.responses);
    
    def test_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response);
        
        for response in self.responses:
            self.assertIn(response , self.my_survey.responses);

unittest.main();
