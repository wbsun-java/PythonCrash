# Chapter 11 — Testing Your Code
# Key examples from the book
# Run tests with: python test_name_function.py

# --- The function being tested (name_function.py) ---
# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = first + ' ' + last
#     return full_name.title()

# --- A basic unit test (test_name_function.py) ---
# import unittest
# from name_function import get_formatted_name
#
# class NamesTestCase(unittest.TestCase):
#     """Tests for name_function.py."""
#
#     def test_first_last_name(self):
#         """Do names like 'Janis Joplin' work?"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
# unittest.main()

# --- Assert methods available in unittest.TestCase ---
# assertEqual(a, b)        -- verify a == b
# assertNotEqual(a, b)     -- verify a != b
# assertTrue(x)            -- verify x is True
# assertFalse(x)           -- verify x is False
# assertIn(item, list)     -- verify item is in list
# assertNotIn(item, list)  -- verify item is not in list

# --- Testing a class (survey.py) ---
# class AnonymousSurvey():
#     """Collect anonymous answers to a survey question."""
#
#     def __init__(self, question):
#         self.question = question
#         self.responses = []
#
#     def show_question(self):
#         print(self.question)
#
#     def store_response(self, new_response):
#         self.responses.append(new_response)
#
#     def show_results(self):
#         print("Survey results:")
#         for response in self.responses:
#             print('- ' + response)

# --- Test file with setUp() (test_survey.py) ---
# import unittest
# from survey import AnonymousSurvey
#
# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey"""
#
#     def setUp(self):
#         """Create a survey and a set of responses for use in all test methods."""
#         question = "What language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']
#
#     def test_store_single_response(self):
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)
#
#     def test_store_three_responses(self):
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response, self.my_survey.responses)
#
# unittest.main()

# --- Key ideas ---
# 1. Each test method name must start with 'test_'
# 2. setUp() runs before every test method — use it to create reusable objects
# 3. Run tests: python test_file.py
# 4. A dot (.) = passed, F = failed, E = error

print("See the commented code above for the full testing pattern.")
print("Create name_function.py and test_name_function.py to try it out.")
