"""
Task 3: Channel Slicing & Isolation
Place an image named 'sample.jpg' in the same folder as this script,
or pass a different path to main().
"""
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use("Agg")  # safe for headless/script execution; drop this line if running in Jupyter
import matplotlib.pyplot as plt


def main(path="sample.jpg"):
    img = np.array(Image.open(path).convert("RGB"))

    print("\n--- CHANNEL EXTRACTION SUMMARY ---")
    print(f"Original Image Shape : {img.shape}")

    # 2D intensity grids via Axis 2 slicing
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    print(f"Red Channel 2D Shape  : {R.shape} | Mean Intensity: {R.mean():.2f}")
    print(f"Green Channel 2D Shape: {G.shape} | Mean Intensity: {G.mean():.2f}")
    print(f"Blue Channel 2D Shape : {B.shape} | Mean Intensity: {B.mean():.2f}")

    # Single-channel-active 3D color views
    red_only = np.zeros_like(img)
    red_only[:, :, 0] = R

    green_only = np.zeros_like(img)
    green_only[:, :, 1] = G

    blue_only = np.zeros_like(img)
    blue_only[:, :, 2] = B

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))

    axes[0, 0].imshow(red_only);   axes[0, 0].set_title("Red Only");   axes[0, 0].axis("off")
    axes[0, 1].imshow(green_only); axes[0, 1].set_title("Green Only"); axes[0, 1].axis("off")
    axes[0, 2].imshow(blue_only);  axes[0, 2].set_title("Blue Only");  axes[0, 2].axis("off")

    axes[1, 0].imshow(R, cmap="gray"); axes[1, 0].set_title("Red Intensity");   axes[1, 0].axis("off")
    axes[1, 1].imshow(G, cmap="gray"); axes[1, 1].set_title("Green Intensity"); axes[1, 1].axis("off")
    axes[1, 2].imshow(B, cmap="gray"); axes[1, 2].set_title("Blue Intensity");  axes[1, 2].axis("off")

    plt.tight_layout()
    plt.savefig("channel_extraction.png", dpi=150)
    print("Display Window : Matplotlib 2x3 Subplot Grid Rendered (saved to channel_extraction.png)")


if __name__ == "__main__":
    main()
