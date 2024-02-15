from modules import multiply_the_number


def describe_multiply_the_number():
    def should_validate_true():
        """🧪 expect the validation to be true"""
        assert multiply_the_number.validate() == True
