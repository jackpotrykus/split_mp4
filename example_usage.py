from split_audio.mp4 import MP4Splitter


def main() -> None:
    """Demo of functionality"""
    m = MP4Splitter(seconds_per_split=5, output_dir="./sample_outputs")
    m.split_dir("./sample_inputs")
    return


if __name__ == "__main__":
    main()
