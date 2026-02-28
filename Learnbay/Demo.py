
nos = 4

def file_pointer_demo():
    with open("products_new.txt",'rb')  as f:  # open the file in read mode

        f.seek(0,2)
        pos = f.tell()

        lines = []
        current = b""

        while pos>0 and len(lines)<= nos:
            pos = pos - 1
            f.seek(pos)
            ch = f.read(1)

            if ch == b"\n":
                if current:
                    lines.append(current[::-1])
                    current = b""
            else:
                current = current + ch

        if current:
              lines.append(current[::-1])

        for line in reversed(lines[:nos]):
            print(line.decode().strip())

file_pointer_demo()