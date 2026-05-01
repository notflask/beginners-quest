# My Google CTF 2024 Beginner's Quest Solvers

This is a collection of my personal write-ups and scripts for various challenges I solved during the Google CTF 2024 Beginner's Quest. I built these scripts to automate the exploitation and flag retrieval processes for different categories like Web and Pwn.

## What is in this repo

I have included the scripts I used for three specific challenges:

- **message.py**: This is my solution for a challenge involving bcrypt. I found a way to manipulate the salt and password combination to brute-force the flag byte by byte. The script handles the server communication and saves progress as it goes.
- **no-refund.js**: A quick JavaScript snippet I wrote to trigger a refund via a POST request. It was a straightforward web challenge where I just needed to hit the right endpoint with specific parameters.
- **simple-echo.py**: This script helped me solve a Pwn challenge. I used pwntools to perform a format string attack on a remote echo service, iterating through offsets to see what I could leak from the stack.

## Getting Started

If you want to try these out or look at how they work, you will need a few things set up.

### Python Environment
Most of my scripts are in Python. You will need to install these dependencies:
- requests (for the web stuff)
- bcrypt (for hash checking)
- beautifulsoup4 (to parse HTML responses)
- pwntools (for the echo service exploit)

You can get them all with:
```bash
pip install requests bcrypt beautifulsoup4 pwntools
```

### Node.js
For the JavaScript script, I just used a modern Node.js environment that supports the fetch API.

## How to use them

### Brute-forcing the message flag
To run my bcrypt brute-forcer:
```bash
python3 message.py
```
It will resume from `flag.txt` if you have already started it.

### Leaking data from simple-echo
To run the format string exploit:
```bash
python3 simple-echo.py
```

### Running the refund script
To trigger the refund:
```bash
node no-refund.js
```

## Note
These are my personal solutions for learning and competition. Use them responsibly.
