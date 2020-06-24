class AnonymousSurvey():
    """Collet anonymous answers to a survey question."""

    def __init__(self, question):
        """"storek a question, and prepare to store response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """sotre a single response  to the survey"""
        self.responses.append(new_response)

    def show_result(self):
        """show all the responses that have been given."""
        print("survey result:")
        for response in self.responses:
            print('- ' + response)
