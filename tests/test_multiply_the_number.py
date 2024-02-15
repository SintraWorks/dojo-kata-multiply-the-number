from modules import multiply_the_number


def describe_multiply_the_number():
    def validate_that_input_3_returns_15():
        """🧪 expect input 3 to return 15"""
        assert multiply_the_number.multiply(3) == 15
