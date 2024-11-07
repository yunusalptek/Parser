import ASTNodeDefs as AST

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.current_char = self.code[self.position]
        self.tokens = []

    # Move to the next position in the code.
    def advance(self):
        # TODO: Students need to complete the logic to advance the position.
        self.position += 1
        if self.position >= len(self.code):
            self.current_char = None
        else:
            self.current_char = self.code[self.position]

    # Skip whitespaces.
    def skip_whitespace(self):
        # TODO: Complete logic to skip whitespaces.
        while self.current_char and self.current_char.isspace():
            self.advance()

    # Tokenize an identifier.
    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return ('IDENTIFIER', result)

        #result = ''
        # TODO: Complete logic for handling identifiers.
        #letters = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h",
                   #"I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p",
                   #"Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x",
                   #"Y": "y", "Z": "z"}
        #digits = {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1}
        #keyword = {"if": 1, "else": 1, "while": 1}
        #if self.current_char and (self.current_char in letters or self.current_char in letters.values()):
            #result += self.current_char
            #while self.current_char in letters or self.current_char in letters.values() or self.current_char in digits or self.current_char == "_":
                #result += self.current_char
                #self.advance()
            #if result in keyword:
                #return ("KEYWORD", result)
        #return ('IDENTIFIER', result)

    # Tokenize a number.
    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return ('NUMBER', int(result))

        # TODO: Implement logic to tokenize numbers.
        #digits = {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1}
        #number = ""
        #if self.current_char and self.current_char in digits:
            #while self.current_char in digits:
                #number += self.current_char
                #self.advance()
        #return ('NUMBER', int(number))

    def token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isalpha():
                ident = self.identifier()
                if ident[1] == 'if':
                    return ('IF', 'if')
                elif ident[1] == 'else':
                    return ('ELSE', 'else')
                elif ident[1] == 'while':
                    return ('WHILE', 'while')
                return ident
            if self.current_char.isdigit():
                return self.number()

            # TODO: Add logic for operators and punctuation tokens.
            if self.current_char == '=':
                self.advance()
                return ('EQUAL', '=')
            elif self.current_char == '+':
                self.advance()
                return ('PLUS', '+')
            elif self.current_char == '-':
                self.advance()
                return ('MINUS', '-')
            elif self.current_char == '*':
                self.advance()
                return ('MULTIPLY', '*')
            elif self.current_char == '/':
                self.advance()
                return ('DIVIDE', '/')
            elif self.current_char == '>':
                self.advance()
                return ('GREATER', '>')
            elif self.current_char == '<':
                self.advance()
                return ('LESS', '<')
            elif self.current_char == '(':
                self.advance()
                return ('LPAREN', '(')
            elif self.current_char == ')':
                self.advance()
                return ('RPAREN', ')')
            elif self.current_char == ':':
                self.advance()
                return ('COLON', ':')
            elif self.current_char == "!=":
                self.advance()
                return ("NOT_EQUAL", "!=")
            elif self.current_char == "==":
                self.advance()
                return ("IDENTICAL", "==")
            #if self.current_char == '=':
                self.advance()  # Move past '='
                return ('EQUALS', '=')
            #if self.current_char in {"+", "-", "*", "/"}:
                op = self.current_char
                self.advance()
                return ('PLUS', op) if op == '+' else ('MINUS', op) if op == '-' else ('MULTIPLY', op) if op == '*' else ('DIVIDE', op)
            #if self.current_char in {"(", ")"}:
                punc = self.current_char
                self.advance()
                return ('LPAREN', punc) if punc == '(' else ('RPAREN', punc)
            #operators = {"+": 1, "-": 1, "*": 1, "/": 1, "=": 1}
            #punctuation = {"(": 1, ")": 1}
            #if self.current_char in operators or self.current_char in punctuation:
                #self.tokens.append(self.current_char)
                #self.advance()
                #return self.current_char

            raise ValueError(f"Illegal character at position {self.position}: {self.current_char}")

        return ('EOF', None)

    # Collect all tokens into a list.
    def tokenize(self):
        # TODO: Implement the logic to collect tokens.
        while self.current_char:
            self.tokens.append(self.token())
        return self.tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = tokens.pop(0)  # Start with the first token

    def advance(self):
        # Move to the next token in the list.
        # TODO: Ensure the parser doesn't run out of tokens.
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = ('EOF', None)

        #self.position += 1
        #if self.position >= len(self.tokens):
            #self.current_token = None
        #else:
            #self.current_token = self.tokens[self.position]

    def parse(self):
        """
        Entry point for the parser. It will process the entire program.
        TODO: Implement logic to parse multiple statements and return the AST for the entire program.
        """
        return self.program()

    def program(self):
        """
        Program consists of multiple statements.
        TODO: Loop through and collect statements until EOF is reached.
        """
        statements = []
        while self.current_token and self.current_token[0] != 'EOF':
            # TODO: Parse each statement and append it to the list.
            statements.append(self.statement())
            if self.current_token and self.current_token[0] != "EOF":
                self.advance()
        # TODO: Return an AST node that represents the program.
        return statements

    def statement(self):
        """
        Determines which type of statement to parse.
        - If it's an identifier, it could be an assignment or function call.
        - If it's 'if', it parses an if-statement.
        - If it's 'while', it parses a while-statement.
        
        TODO: Dispatch to the correct parsing function based on the current token.
        """
        print(f"Current token in statement: {self.current_token}")
        if self.current_token[0] == 'IDENTIFIER':
            if self.peek() == 'EQUALS':  # Assignment
                #self.advance()
                return self.assign_stmt() #AST of assign_stmt
            elif self.peek() == 'LPAREN':  # Function call
                self.advance()
                return self.function_call(self.current_token[1]) #AST of function call
            else:
                raise ValueError(f"Unexpected token after identifier: {self.current_token}")
        elif self.current_token[0] == 'IF':
            return self.if_stmt() #AST of if stmt
        elif self.current_token[0] == 'WHILE':
            return self.while_stmt() #AST of while stmt
        else:
            # TODO: Handle additional statements if necessary.
            raise ValueError(f"Unexpected token: {self.current_token}")

    def assign_stmt(self):
        """
        Parses assignment statements.
        Example:
        x = 5 + 3
        TODO: Implement parsing for assignments, where an identifier is followed by '=' and an expression.
        """
        identifier = self.current_token[1]
        self.expect("IDENTIFIER")
        self.expect("EQUALS")
        expression = self.expression()
        return AST.Assignment(identifier, expression)

    def if_stmt(self):
        """
        Parses an if-statement, with an optional else block.
        Example:
        if condition:
            # statements
        else:
            # statements
        TODO: Implement the logic to parse the if condition and blocks of code.
        """
        self.expect("IF")
        condition = self.expression()
        if_block = self.block()
        else_block = None
        if self.current_token[0] == "ELSE":
            self.expect("ELSE")
            else_block = self.block()
        return AST.IfStatement(condition, if_block, else_block)

    def while_stmt(self):
        """
        Parses a while-statement.
        Example:
        while condition:
            # statements
        TODO: Implement the logic to parse while loops with a condition and a block of statements.
        """
        self.expect("WHILE")
        condition = self.expression()
        block = self.block()
        return AST.WhileStatement(condition, block)

    def block(self):
        """
        Parses a block of statements. A block is a collection of statements grouped by indentation.
        Example:
        if condition:
            # This is a block
            x = 5
            y = 10
        TODO: Implement logic to capture multiple statements as part of a block.
        """
        statements = []
        # write your code here
        while self.current_token and self.is_statement_start(self.current_token[0]):
            statements.append(self.statement())
        return AST.Block(statements)

    def expression(self):
        """
        Parses an expression. Handles operators like +, -, etc.
        Example:
        x + y - 5
        TODO: Implement logic to parse binary operations (e.g., addition, subtraction) with correct precedence.
        """
        left = self.term()  # Parse the first term
        while self.current_token[0] in ['PLUS', 'MINUS']:  # Handle + and -
            op = self.current_token  # Capture the operator
            self.advance()  # Skip the operator
            right = self.term()  # Parse the next term
            left = AST.BinaryOperation(left, op, right)
    
        return left

    def boolean_expression(self):
        """
        Parses a boolean expression. These are comparisons like ==, !=, <, >.
        Example:
        x == 5
        TODO: Implement parsing for boolean expressions.
        """
        # write your code here, for reference check expression function
        left = self.expression()
        while self.current_token[0] in ["EQUAL", "NOT_EQUAL", "LESS", "GREATER"]:
            op = self.current_token
            self.advance()
            right = self.expression()
            left = AST.BinaryOperation(left, op, right)

        return left

    def term(self):
        """
        Parses a term. A term consists of factors combined by * or /.
        Example:
        x * y / z
        TODO: Implement the parsing for multiplication and division.
        """
        # write your code here, for reference check expression function
        left = self.factor()
        while self.current_token[0] in ["MULTIPLY", "DIVIDE"]:
            op = self.current_token
            self.advance()
            right = self.factor()
            left = AST.BinaryOperation(left, op, right)
        return left

    def factor(self):
        """
        Parses a factor. Factors are the basic building blocks of expressions.
        Example:
        - A number
        - An identifier (variable)
        - A parenthesized expression
        TODO: Handle these cases and create appropriate AST nodes.
        """
        if self.current_token[0] == 'NUMBER':
            #write your code here
            value = self.current_token[1]
            self.advance()
            return AST.NumberLiteral(value)
        elif self.current_token[0] == 'IDENTIFIER':
            #write your code here
            name = self.current_token[1]
            self.advance()
            return AST.Variable(name)
        elif self.current_token[0] == 'LPAREN':
            #write your code here
            self.advance()
            expression = self.expression()
            self.expect("RPAREN")
            return expression
        else:
            raise ValueError(f"Unexpected token in factor: {self.current_token}")

    def function_call(self):
        """
        Parses a function call.
        Example:
        myFunction(arg1, arg2)
        TODO: Implement parsing for function calls with arguments.
        """
        func_name = self.current_token[1]
        self.expect("IDENTIFIER")
        self.expect("LPAREN")
        args = []
        if self.current_token[0] != "RPAREN":
            args = self.arg_list()
        self.expect("RPAREN")
        return AST.FunctionCall(func_name, args)

    def arg_list(self):
        """
        Parses a list of arguments in a function call.
        Example:
        arg1, arg2, arg3
        TODO: Implement the logic to parse comma-separated arguments.
        """
        args = []
        while True:
            args.append(self.expression())
            if self.current_token[0] == "COMMA":
                self.advance()
            else:
                break
        return args

    def expect(self, token_type):
       
        if self.current_token[0] == token_type:
            self.advance()  # Move to the next token
        else:
            raise ValueError(f"Expected {token_type} but got {self.current_token[0]}")

    def peek(self):
        if self.tokens:
            return self.tokens[0][0]
        else:
            return None
