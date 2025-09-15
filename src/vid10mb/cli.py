#!/usr/bin/env python3
import argparse

def parse_args():
    p = argparse.ArgumentParser(
        prog="vid10mb",
        description="Shrink a video to fit under 10 MB using ffmpeg."
    )
    p.add_argument("input", help="Path to input video")
    p.add_argument("-o", "--output", help="Output file (default: auto)")
    p.add_argument("--max-mb", type=float, default=10.0,
                   help="Target size in MB (default: 10)")
    return p.parse_args()

def main():
    args = parse_args()
    print(f"[CLI stub] input={args.input}, output={args.output}, target={args.max_mb}MB")

if __name__ == "__main__":
    main()
