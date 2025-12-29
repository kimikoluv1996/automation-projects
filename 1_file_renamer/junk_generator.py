for i in range(100):
    with open(f"junk_drawer/{i}_file.txt", "x") as newfile:
        newfile.write("some text")