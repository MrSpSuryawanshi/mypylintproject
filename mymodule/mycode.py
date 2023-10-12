   from pylint.interfaces import IRawChecker
   from pylint.checkers import BaseChecker

   class HelloChecker(BaseChecker):
       __implements__ = IRawChecker

       name = 'hello-checker'
       msgs = {
           'W0001': (
               'Hello detected in the code',
               'warning-hello',
               'Used when "hello" is found in the code'
           )
       }

       def process_module(self, node):
           for line_num, line in enumerate(node.stream(), start=1):
               if 'hello' in line:
                   self.add_message('warning-hello', line=line_num)

   def register(linter):
       linter.register_checker(HelloChecker(linter))
