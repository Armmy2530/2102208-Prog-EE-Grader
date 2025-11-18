from io import BufferedReader
def read_token(f: BufferedReader):
    token = ""
    while True:
        ch = f.read(1)
        if ch in "0123456789":
            token += ch
            break

    while True:
        ch = f.read(1)
        if ch in " \t\n\r":
            break
        else:
            token += ch

    return token

def get_image(f: BufferedReader):
    f.readline()  # skip magic number line
    
    dimension = f.readline()
    w,h = tuple(map(int, dimension.split()))
    # print(dimension)
    # print(f"Width: {w}, Height: {h}")

    f.readline() # skip max color value line

    img = []
    for i in range(w):
        row = []
        for j in range(h):
            r_str= read_token(f)
            g_str= read_token(f)
            b_str= read_token(f)
            # print(i,j, r_str, g_str, b_str)
            r = int(r_str)
            g = int(g_str)
            b = int(b_str)
            row.append([r, g, b])
        img.append(row)

    return img

if __name__ == "__main__":
    import numpy as np
    input_filename = "test_image1.ppm"
    # input_filename = "img.ppm"
    with open(input_filename, "r") as f:  
        img_matrix = np.array(get_image(f))
        assert img_matrix.max() <= 255 and img_matrix.min() >= 0, "Out of Bound"

    output_filename = "img_gray.pgm"
    gray_img = np.sum(img_matrix * np.array([0.299, 0.587, 0.114]), axis=-1)
    gray_img = gray_img.clip(0, 255).astype(np.uint8).astype(str)
    with open(output_filename, "w") as f:
        f.write("P2\n")
        f.write(f"{img_matrix.shape[0]} {img_matrix.shape[1]}\n")
        f.write("255\n")
        f.write(" ".join(np.ravel(gray_img)))
        print(f'"{output_filename}" saved successfully')