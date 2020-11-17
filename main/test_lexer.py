from lexer import Lexer


def main():
     input = 'tesererer erev efeeeeeeeeeeeee'
     lexer_test = Lexer(input)

     while lexer_test.look_ahead_next_char() != '\0':
          next_char = lexer_test.current_char
          print(next_char)
          lexer_test.process_next_char()

main()