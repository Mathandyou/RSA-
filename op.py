from Crypto.PublicKey import RSA

# 用户输入 RSA 密钥长度
keybin = int(input('Enter RSA key length (e.g., 2048, 4096, 8192): '))

# 生成 keybin 位的 RSA 密钥对
key = RSA.generate(keybin)
public_key = key.publickey().export_key()
private_key = key.export_key()

# 保存公钥和私钥到文件
with open('public_key.pem', 'wb') as f:
    f.write(public_key)

with open('private_key.pem', 'wb') as f:
    f.write(private_key)

print(f'RSA key pair with length {keybin} generated and saved to files.')
