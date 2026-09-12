"""
Task 4: Spatial Downsampling & Pixelation via Striding
Place an image named 'sample.jpg' in the same folder as this script,
or pass a different path/N to main().
"""
import numpy as np
from PIL import Image


def main(path="sample.jpg", N=8):
    img = np.array(Image.open(path).convert("RGB"))
    original_shape = img.shape
    original_mem = img.nbytes

    # Downsample by taking every N-th pixel along rows/cols
    downsampled = img[::N, ::N, :]
    down_shape = downsampled.shape
    down_mem = downsampled.nbytes

    # Re-expand back toward original size to visualize pixelation
    re_expanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)
    re_expanded = re_expanded[:original_shape[0], :original_shape[1], :]

    per_axis_reduction = (1 - 1 / N) * 100
    mem_savings = (1 - down_mem / original_mem) * 100

    print(f"\n--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
    print(f"Original Shape     : {original_shape} | Memory: {original_mem:,} bytes")
    print(f"Downsampled Shape  : {down_shape} | Memory: {down_mem:,} bytes")
    print(f"Re-expanded Shape  : {re_expanded.shape} | Visual: Blocky Pixelation")
    print(f"Dimension Reduction: {per_axis_reduction:.2f}% reduction per axis")
    print(f"Memory Savings     : {mem_savings:.2f}% data reduction")

    Image.fromarray(re_expanded).save("pixelated_output.png")
    print("Saved pixelated result to pixelated_output.png")


if __name__ == "__main__":
    main()
