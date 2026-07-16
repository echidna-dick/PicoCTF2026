import idc, ida_idaapi

ea = idc.get_name_ea_simple("obf_bytes")
if ea == ida_idaapi.BADADDR:
    raise RuntimeError("no obf_bytes found")

raw = idc.get_bytes(ea, 16)
k = raw.index(0)
obf = raw[:k]

print(f"obf_bytes @ {ea:#x}")
print(f"raw     : {list(obf)}")
print(f"len     : {k}");

s = bytes(b ^ 0xAA for b in obf)
print(f"decoded: {s.decode('latin1')!r}")

def djb2(data):
    h = 5381
    for c in data:
        h = (h * 33 + c) & 0xFFFFFFFFFFFFFFFF
    return h
print(f"secret : {djb2(s)}")