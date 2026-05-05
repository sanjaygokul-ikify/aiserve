import argparse
from aiserve.server import Server

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='aiserve Server')
    parser.add_argument('--model-path', type=str, required=True, help='Path to the AI model')
    parser.add_argument('--port', type=int, default=8080, help='Server port')
    args = parser.parse_args()
    server = Server(args.model_path, args.port)
    server.start()