import traceback

# Task 1: Diary 

# wrap code in try block to catch exceptions and prevennt code from crushing the app
try:
    # open file
    with open('diary.txt', 'a') as file:
        user_input = input("What happened today? ")
        # loop to get input messages
        while True:
            if user_input.lower() == "done for now":
                file.write(user_input + "\n")
                break
            else:
                file.write(user_input + "\n")
                user_input = input("What else? ")

except Exception as e:
   print(f"An exception occurred. Exception type: {type(e).__name__}")

   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   message = str(e)

   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   
   if message:
      print(f"Exception message: {message}")

   print(f"Stack trace: {stack_trace}")