import argparse
import filecmp

parser = argparse.ArgumentParser(
    description='Quickly & recursively spot differences between two provided directories to be compared.'
)
parser.add_argument('--dir1', metavar='path', required=True, help='First directory')
parser.add_argument('--dir2', metavar='path', required=True, help='Second directory')

def compare_dirs_and_files_recursively(dir1: str, dir2: str) -> None:
    filecmp.dircmp(dir1, dir2).report_full_closure()

if __name__ == '__main__':
    args = parser.parse_args()
    dir1 = args.dir1
    dir2 = args.dir2
    assert(isinstance(dir1, str))
    assert(isinstance(dir2, str))
    compare_dirs_and_files_recursively(dir1, dir2)
