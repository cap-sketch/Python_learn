#writing to a file
"""to write a file you need to open it in write(w),append(a),update(+) mode.
   then use the write() or writelines() methods."""

with open("hello3.txt","w") as f:
    f.write("i am learning python\n")
    lines=["hello\n","how u doing\n"]
    f.writelines(lines)

with open("hello3.txt","a") as f:
    f.write("i am appending the file")
