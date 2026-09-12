"""
Task 1: Display Pixel Density (PPI/DPI) Calculator
"""
import math


def classify_density(dpi):
    if dpi < 100:
        return "Low Density (Standard Monitor)"
    elif dpi <= 200:
        return "Medium Density (HD Display)"
    else:
        return "High Density (Retina / Mobile)"


def main():
    w_px = int(input("Enter horizontal resolution (pixels): "))
    h_px = int(input("Enter vertical resolution (pixels): "))
    d_in = float(input("Enter physical diagonal size (inches): "))

    # Total pixel count
    total_pixels = w_px * h_px

    # Simplified aspect ratio using GCD
    g = math.gcd(w_px, h_px)
    aspect_w, aspect_h = w_px // g, h_px // g

    # Diagonal pixel count -> DPI/PPI
    diagonal_px = math.sqrt(w_px ** 2 + h_px ** 2)
    dpi = diagonal_px / d_in

    category = classify_density(dpi)

    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {total_pixels:,} pixels")
    print(f"Aspect Ratio      : {aspect_w}:{aspect_h}")
    print(f"Calculated DPI    : {dpi:.2f} DPI")
    print(f"Density Category  : {category}")


if __name__ == "__main__":
    main()
