def isOne(char:str)->bool:
    return ord("A")<=ord(char)<=ord("Z")

def GetMask(IFC_uid: str)->str:
    mask = 0
    for ch in IFC_uid:
        mask = mask << 1 | isOne(ch)
    
    Hex_buffer = []
    table = "0123456789ABCDEF"
    for i in range(0,22, 4):
        Hex_buffer.append(table[mask % 16])
        mask //= 16
    
    Hex_buffer.extend("00")
    Hex_buffer.reverse()
    Hex = ''.join(Hex_buffer)
    print(Hex)
    return Hex  




