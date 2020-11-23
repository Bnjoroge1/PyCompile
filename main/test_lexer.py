from lexer import Lexer, Token, TokenType

def main():
     
     def test_look_ahead_char():
          input = 'Let a = 23'
          lexer_test = Lexer(input)

          while lexer_test.look_ahead_next_char() != '\0':
               next_char = lexer_test.current_char
               print(next_char)
               lexer_test.process_next_char()
def test_arithmetic_operators():
     input = '+-*/'
     lexer_arithmetic = Lexer(input)
     token = lexer_arithmetic.get_next_token()
     while token.type != '' TokenType.EOF:
          print(token.type)
          token_confirm =  lexer_arithmetic.get_next_token()

if __name__ == "__main__":
         main()
