import pickle
with open("emp1.pick","rb") as fp: #we have given rb as unpickling works on binary files
    print("List of employee records:")
    while(True):
        try:
            record=pickle.load(fp)
            print(record,type(record))
        except EOFError: #End of file
            break
