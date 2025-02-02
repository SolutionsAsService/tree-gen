from PIL import Image, ImageDraw
import random

# Define image size
sprite_size = 64

def generate_palm_tree(variation=1):
    image = Image.new("RGBA", (sprite_size, sprite_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    if variation == 1:
        # Draw the trunk
        draw.rectangle([(30, 40), (34, 60)], fill="saddlebrown", outline="black")
        # Draw the leaves
        draw.polygon([(32, 40), (20, 20), (28, 22)], fill="green", outline="black")
        draw.polygon([(32, 40), (44, 20), (36, 22)], fill="green", outline="black")
        draw.polygon([(32, 40), (20, 30), (28, 32)], fill="green", outline="black")
        draw.polygon([(32, 40), (44, 30), (36, 32)], fill="green", outline="black")
    elif variation == 2:
        # Draw the trunk
        draw.rectangle([(28, 40), (36, 60)], fill="saddlebrown", outline="black")
        # Draw the leaves
        draw.polygon([(32, 40), (18, 15), (26, 18)], fill="green", outline="black")
        draw.polygon([(32, 40), (46, 15), (38, 18)], fill="green", outline="black")
        draw.polygon([(32, 40), (18, 25), (26, 28)], fill="green", outline="black")
        draw.polygon([(32, 40), (46, 25), (38, 28)], fill="green", outline="black")
    else:
        # Draw the trunk
        draw.rectangle([(32, 45), (36, 60)], fill="saddlebrown", outline="black")
        # Draw the leaves
        draw.polygon([(34, 45), (22, 25), (30, 28)], fill="green", outline="black")
        draw.polygon([(34, 45), (46, 25), (38, 28)], fill="green", outline="black")
        draw.polygon([(34, 45), (22, 35), (30, 38)], fill="green", outline="black")
        draw.polygon([(34, 45), (46, 35), (38, 38)], fill="green", outline="black")

    return image

def generate_shrubbery(variation=1):
    image = Image.new("RGBA", (sprite_size, sprite_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    if variation == 1:
        # Draw the shrubbery
        draw.ellipse([(20, 40), (44, 60)], fill="darkgreen", outline="black")
    elif variation == 2:
        # Draw the shrubbery
        draw.rectangle([(18, 45), (46, 60)], fill="forestgreen", outline="black")
        draw.rectangle([(28, 35), (36, 45)], fill="forestgreen", outline="black")
    else:
        # Draw the shrubbery
        draw.ellipse([(15, 40), (49, 60)], fill="seagreen", outline="black")
        draw.ellipse([(25, 30), (39, 50)], fill="seagreen", outline="black")

    return image

def generate_green_tree(variation=1):
    image = Image.new("RGBA", (sprite_size, sprite_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    if variation == 1:
        # Draw the trunk
        draw.rectangle([(28, 40), (36, 60)], fill="saddlebrown", outline="black")
        # Draw the leaves
        draw.ellipse([(20, 20), (44, 45)], fill="green", outline="black")
    elif variation == 2:
        # Draw the trunk
        draw.rectangle([(30, 45), (34, 60)], fill="saddlebrown", outline="black")
        # Draw the leaves
        draw.ellipse([(18, 25), (46, 50)], fill="forestgreen", outline="black")
    else:
        # Draw the trunk
        draw.rectangle([(26, 40), (38, 60)], fill="saddlebrown", outline="black")
        # Draw the leaves
        draw.ellipse([(18, 20), (46, 45)], fill="limegreen", outline="black")

    return image

def save_sprite(image, filename):
    image.save(filename)

if __name__ == '__main__':
    # Generate and save palm trees
    for i in range(1, 4):
        palm_tree = generate_palm_tree(variation=i)
        save_sprite(palm_tree, f"palm_tree_{i}.png")

    # Generate and save shrubbery
    for i in range(1, 4):
        shrubbery = generate_shrubbery(variation=i)
        save_sprite(shrubbery, f"shrubbery_{i}.png")

    # Generate and save green trees
    for i in range(1, 4):
        green_tree = generate_green_tree(variation=i)
        save_sprite(green_tree, f"green_tree_{i}.png")