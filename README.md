# Small tool to compare the contents of two directories recursively

## Requirements
- Requires Python 3.10 or later

## Instructions
1. Make the script (i.e. `run_main.sh`) executable
   1. Open the folder where this README is located in the terminal
   2. Run `chmod +x run_main.sh` in the terminal
2. Execute the script
   1. Run `./run_main.sh ./a ./b` in the terminal, where `./a` and `./b` denote your two root directories to be compared, respectively - of course, you first have to adjust them to your needs
3. Observe the terminal outputs to see files and (sub-)directories which differ between the two root directories when being compared against each other recursively

That's it!

## Note
- `run_main.sh` is just a wrapper around `main.py`, which makes sure to omit printing all files and directories which do not differ between the two compared root directories.
- Ran, at the time of writing, on Ubuntu 16.04
