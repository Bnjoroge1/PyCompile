'''
Lexer Code : Python file responsible for breaking the inputted code into 'tokens'(see Words/Pronunciation in English). Given a string of PyCompile's code, it will iterate character by character to do two things: decide where each token starts/stops and what type of token(e.g keyword, number, operator) it is. If the lexer is unable to do this, then it will report an error for an invalid token.
'''
import enum
class Lexer(object):
     def __init__(self, code):
          self.code_input = code + '\n' #the code input received and append a new-line to simplify parsing
          self.current_char = ' ' #Current Char in the string.
          self.current_position = -1   #Current position in the string.
          self.process_next_char()  

     def process_next_char(self):
          """Evaluates the next character in the string.
          """          
          self.current_position += 1
          if self.current_position >= len(self.code_input):
               '''End of file since the position is equal to or greater than the input's position'''
               self.current_char = '\0' #EOF
               print('end of line')
          self.current_char = self.code_input[self.current_position] 

     def look_ahead_next_char(self):
          if self.current_position + 1 >= len(self.code_input):
               return '\0' 
          return self.code_input[self.current_position +1]
               
     def abort(self, message):
          '''Skip an invalid token'''
          pass  
     def skipWhiteSpace(self):
          ''' Skips whitespace exept newlines'''
          pass

     def SkipComments(self):
          pass

     def get_next_token(self):
          '''Classifies the token and is called everytime there is a switch
          Guidelines for Token Classification.
          Operator : +, -, *, /, =, ==, !=, >, <, >=, <=
          String : Double quotation followed by zero or more characters and a double quotation. 
          Number One or more numeric characters followed by an optional decimal point and one or more numeric characters. 
          Identifier : An alphabetical character followed by zero or more alphanumeric characters.
          Keyword:  Exact text match of: LABEL, GOTO, PRINT, INPUT, LET, IF, THEN, ENDIF, WHILE, REPEAT, ENDWHILE(Extended) 
          '''
          token = None
          # Check the first character of this token to see if we can decide what it is.
          # If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest.
          if self.current_char == '+':
               token = Token(self.current_char, TokenType.PLUS)
          elif self.current_char == '-':
               token = Token(self.current_char, TokenType.MINUS)
          elif self.current_char == '*':
               token = Token(self.current_char, TokenType.ASTERISK)
          elif self.current_char == '/':
               token = Token(self.current_char, TokenType.SLASH)
          elif self.current_char == '\n':
               token = Token(self.current_char, TokenType.NEWLINE)
          elif self.current_char == '\0':
               token = Token('', TokenType.EOF)
          else:
               # Unknown token!
               pass
                    
          self.nextChar()
          return token


class Token:
     def __init__(self, TokenText, TokenType):
          self.text = TokenText # The token's actual text. Used for identifiers, strings, and numbers.
          self.type = TokenType   # The TokenType that this token is classified as.
     

# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	# Keywords.
	LABEL = 101
	GOTO = 102
	PRINT = 103
	INPUT = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	# Operators.
	EQ = 201  
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211
   










