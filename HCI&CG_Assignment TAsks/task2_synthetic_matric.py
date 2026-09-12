"""
Task 2: Environment Setup & Synthetic Image Matrix Creation
"""
import numpy as np
from PIL import Image


def main():
    H, W, C = 300, 400, 3
    img = np.zeros((H, W, C), dtype=np.uint8)

    mid_h, mid_w = H // 2, W // 2

    img[0:mid_h, 0:mid_w] = [255, 0, 0]        # Top-left: Red
    img[0:mid_h, mid_w:W] = [0, 255, 0]        # Top-right: Green
    img[mid_h:H, 0:mid_w] = [0, 0, 255]        # Bottom-left: Blue
    img[mid_h:H, mid_w:W] = [255, 255, 255]    # Bottom-right: White

    print("\n--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {img.shape}")
    print(f"Data Type             : {img.dtype}")
    print(f"Total Elements        : {img.size:,} values")
    print(f"Memory Footprint      : {img.nbytes:,} bytes ({img.nbytes / 1024:.2f} KB)")

    # Save so you can screenshot/embed the four-color result in your report
    Image.fromarray(img).save("quadrant_image.png")
    print("Saved visualization to quadrant_image.png")


if __name__ == "__main__":
    main()
