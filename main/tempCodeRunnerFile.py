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