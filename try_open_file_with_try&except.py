file_name = None
all_attempt = 5
while all_attempt > 0:
    try:
        print("enter the file name with abs path: ")
        print(f"you have {all_attempt} tries left")
        print("Example: C:/Python/Files/yourfile.extension")
        file_name_and_path = input("File Name: => ").strip()
        file_name = open(file_name_and_path, "r")
        print(file_name.read())
        break
    except FileNotFoundError:
        print("file not found be sure the name is valid")
        all_attempt -= 1
    except:
        print("err happend")
        #all_attempt -= 1
    finally:
        if  file_name is not None:
            file_name.close()
            print("file closed")
else:
    print("all tries are done")