from modules import multiply_the_number


def describe_multiply_the_number():
    def validate_that_input_3_returns_15():
        """🧪 expect the validation to be true"""
        assert multiply_the_number.multiply(3) == 15
