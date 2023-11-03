class Problem:
    """Represents an arithmetic problem."""
    
    MAX_DIGITS = 4
    VALID_OPERATORS = ['+', '-']
    ERROR_INVALID_OPERATOR = "Error: Operator must be '+' or '-'."
    ERROR_TOO_MANY_DIGITS = "Error: Numbers cannot be more than four digits."
    ERROR_INVALID_NUMBER = "Error: Numbers must only contain digits."
    ERROR_INVALID_FORMAT = "Error: Only two numbers and an operator accepted."

    def __init__(self, first_number, operator, second_number):
        self.validate_number(first_number)
        self.validate_number(second_number)
        self.validate_operator(operator)

        self.first_number = first_number
        self.operator = operator
        self.second_number = second_number

    @classmethod
    def from_string(cls, problem_string):
        """Parse a problem string into a Problem instance."""
        parts = problem_string.split()
        if len(parts) != 3:
            raise ValueError(cls.ERROR_INVALID_FORMAT)
        return cls(*parts)

    def validate_number(self, number):
        """Validate if a number is a digit and does not exceed the max digit length."""
        if not number.isdigit():
            raise ValueError(self.ERROR_INVALID_NUMBER)
        if len(number) > self.MAX_DIGITS:
            raise ValueError(self.ERROR_TOO_MANY_DIGITS)

    def validate_operator(self, operator):
        """Validate if the operator is valid."""
        if operator not in self.VALID_OPERATORS:
            raise ValueError(self.ERROR_INVALID_OPERATOR)

    def calculate_answer(self):
        """Calculate the answer of an arithmetic problem."""
        operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        return operations[self.operator](int(self.first_number),
                                         int(self.second_number))

    def format(self, display_answer=False):
        """Format a single arithmetic problem for display."""
        PADDING = 2
        SEPARATOR = '-'
        length = max(len(self.first_number), len(self.second_number)) + PADDING
        top = self.first_number.rjust(length)
        bottom = self.operator + self.second_number.rjust(length - 1)
        separator = SEPARATOR * length
        answer_str = str(
            self.calculate_answer()).rjust(length) if display_answer else ''
        return top, bottom, separator, answer_str


def validate_problems(problems):
    """Validate a list of problems."""
    MAX_PROBLEMS = 5
    if len(problems) > MAX_PROBLEMS:
        raise ValueError("Error: Too many problems.")
    return [Problem.from_string(problem_str) for problem_str in problems]


def join_lines(lines, space_count=4):
    """Join the lines of the problem with a given space count."""
    space = ' ' * space_count
    return '\n'.join(space.join(line) for line in lines)


def construct_output(lines, display_answers):
    """Construct the final output of formatted problems."""
    if not display_answers:
        return join_lines([lines["top"], lines["bottom"], lines["separator"]])
    return join_lines(
        [lines["top"], lines["bottom"], lines["separator"], lines["answer"]])


def arithmetic_arranger(problems, display_answers=False):
    """Arrange arithmetic problems in a visually appealing way."""
    try:
        problems_list = validate_problems(problems)
    except ValueError as e:
        return str(e)

    lines = {"top": [], "bottom": [], "separator": [], "answer": []}
    for problem in problems_list:
        formatted = problem.format(display_answer=display_answers)
        for name, value in zip(lines.keys(), formatted):
            lines[name].append(value)

    return construct_output(lines, display_answers)
