import argparse
from Capture import startCapture

def main():
    parser = argparse.ArgumentParser(description="Welcome to the Packet Capture Tool!")
    parser.add_argument("-i", "--interface", type=str, required=True, help="Network interface to capture packets")
    parser.add_argument("-c", "--count", type=int, default=10, help="Number of packets to capture (default: 10)")
    args = parser.parse_args()

    startCapture(args.interface, args.count)

if __name__ == "__main__":
    main()