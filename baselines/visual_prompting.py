import io
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import numpy as np
import matplotlib.pyplot as plt


# scaffold
def scaffold(img, dots_size_w, dots_size_h):
    """
    takes an original image as input, save the processed image to save_path. Each dot is labeled with two-dimensional Cartesian coordinates (x,y). Suitable for single-image tasks.
    control args:
    1. dots_size_w: the number of columns of the dots matrix
    2. dots_size_h: the number of rows of the dots matrix
    """

    if img.mode != 'RGB':
        img = img.convert('RGB')
    draw = ImageDraw.Draw(img, 'RGB')

    width, height = img.size
    grid_size_w = dots_size_w + 1
    grid_size_h = dots_size_h + 1
    cell_width = width / grid_size_w
    cell_height = height / grid_size_h

    font = ImageFont.truetype("arial.ttf", width // 40)  # Adjust font size if needed; default == width // 40

    count = 0
    for j in range(1, grid_size_h):
        for i in range(1, grid_size_w):
            x = int(i * cell_width)
            y = int(j * cell_height)

            pixel_color = img.getpixel((x, y))
            # choose a more contrasting color from black and white
            if pixel_color[0] + pixel_color[1] + pixel_color[2] >= 255 * 3 / 2:
                opposite_color = (238,75,43)
            else:
                opposite_color = (238,75,43)

            circle_radius = width // 240  # Adjust dot size if needed; default == width // 240
            draw.ellipse([(x - circle_radius, y - circle_radius), (x + circle_radius, y + circle_radius)], fill=opposite_color)

            text_x, text_y = x + 3, y
            count_w = count // dots_size_w
            count_h = count % dots_size_w
            label_str = f"({count_w+1},{count_h+1})"
            draw.text((text_x, text_y), label_str, fill=opposite_color, font=font)
            count += 1
    return img


def spacecue(img, rows, cols):
    data = np.array(img)
    fig, ax = plt.subplots()
    ax.imshow(data)
    height, width = data.shape[:2]
    for i in range(1, cols):
        ax.axvline(x=i * width / cols, color='red', linewidth=1)
    for j in range(1, rows):
        ax.axhline(y=j * height / rows, color='red', linewidth=1)

    for i in range(rows):
        for j in range(cols):
            label_number = i * cols + j + 1
            ax.text(j * width / cols + width / (cols * 2), i * height / rows + height / (rows * 2), str(label_number),
                    color='red', ha='center', va='center', fontweight='bold', fontsize=10,
                    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))

    ax.set_xticks([])
    ax.set_yticks([])

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    buf.seek(0)

    # Load buffer to PIL Image
    new_img = Image.open(buf)
    plt.imshow(new_img)
    return new_img