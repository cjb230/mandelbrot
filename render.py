import png

X_CANVAS_SIZE = 1920
Y_CANVAS_SIZE = 1080
ITERATION_LIMIT = 254
OUTPUT_FILE = 'background.png'

X_LOWER_LIMIT = -0.7500
X_UPPER_LIMIT = -0.7493
Y_LOWER_LIMIT = 0.034101
Y_UPPER_LIMIT = 0.034495

# These values will give the "traditional" view of the set
#X_LOWER_LIMIT = -2
#X_UPPER_LIMIT = 1
#Y_LOWER_LIMIT = -1
#Y_UPPER_LIMIT = 1

X_PIXEL_STEP = (X_UPPER_LIMIT - X_LOWER_LIMIT) / X_CANVAS_SIZE
Y_PIXEL_STEP = (Y_UPPER_LIMIT - Y_LOWER_LIMIT) / Y_CANVAS_SIZE

print((X_UPPER_LIMIT - X_LOWER_LIMIT) / (Y_UPPER_LIMIT - Y_LOWER_LIMIT))
print(X_CANVAS_SIZE / Y_CANVAS_SIZE)


def iter_score(re, im):
    x = 0
    y = 0
    iters = -1
    while iters < ITERATION_LIMIT and x * x + y * y < 4:
        next_x = x * x - y * y + re
        y = 2 * x * y + im
        x = next_x
        iters += 1
    return iter


def score_colour_map(iter_score):
    grey_val = iter_score
    return [grey_val, grey_val, grey_val]


def main():
    p = []
    for y in range(Y_CANVAS_SIZE):
        imag_part = Y_LOWER_LIMIT + (y * Y_PIXEL_STEP)
        row = []
        for x in range(X_CANVAS_SIZE):
            real_part = X_LOWER_LIMIT + (x * X_PIXEL_STEP)
            row.extend(score_colour_map(iter_score(real_part, imag_part)))
        p.append(tuple(row))

    f = open(OUTPUT_FILE, 'wb')
    w = png.Writer(X_CANVAS_SIZE, Y_CANVAS_SIZE, greyscale=False)
    w.write(f, p)
    f.close()


if __name__ == "__main__":
    main()
