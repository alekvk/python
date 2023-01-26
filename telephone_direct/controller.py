import data_entry
import data_output
import sort
import view

def start():
    while True:
      op = view.get_op()
      if op == 1:
          data_entry.add_phoneNumber()
      elif op == 2:
          data_output.print_table()
      elif op == 3:
          data_output.print_only_name()
      elif op == 4:
          sort.sort_names()
      elif op == 5:
          sort.sort_id()
      elif op == 6:
          break


