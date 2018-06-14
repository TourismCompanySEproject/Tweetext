import sys
txt_files = ["complaint.txt"]

for file in txt_files:
    # try:
    #     file_text = open(file, encoding=("iso-8859-1")).read()
        # print(file_text)
        with open(file, "r") as f:
            for l in f:
                print(l.encode("utf-8"))

    # except FileNotFoundError:
    #     print(file + " was not found.")
    #     sys.exit(0)
    # except UnicodeDecodeError:
    #     print("From clean_data() at feature_extraction:\n" +
    #           file + " causes unicode decode error.")
    #     continue