from modules import multiply_the_number


def describe_multiply_the_number():
    def validate_that_input_3_returns_15():
        """🧪 expect input 3 to return 15"""
        assert multiply_the_number.multiply(3) == 15

    def validate_that_input_10_returns_250():
        """🧪 expect input 10 to return 250"""
        assert multiply_the_number.multiply(10) == 250

    def validate_that_input_200_returns_25000():
        """🧪 expect input 200 to return 25000"""
        assert multiply_the_number.multiply(200) == 25000
