from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import base64
import json
import hmac

# 从文件中读取公钥
with open('public_key.pem', 'rb') as f:
    public_key = f.read()

# 用公钥加密AES密钥
def rsa_encrypt(aes_key, pub_key):
    rsa_public_key = RSA.import_key(pub_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    return base64.b64encode(encrypted_aes_key).decode('utf-8')

# 用AES加密消息并生成HMAC
def aes_encrypt(message, aes_key):
    cipher_aes = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode('utf-8'))
    hmac_obj = hmac.new(aes_key, ciphertext, SHA256)
    return base64.b64encode(cipher_aes.nonce + tag + ciphertext + hmac_obj.digest()).decode('utf-8')

# 用户输入需加密的内容
message = input('Enter the message to encrypt: ')

# 生成随机的AES密钥
aes_key = get_random_bytes(32)

# 用AES加密消息并生成HMAC
encrypted_message = aes_encrypt(message, aes_key)

# 用RSA加密AES密钥
encrypted_aes_key = rsa_encrypt(aes_key, public_key)

# 组合加密结果
encrypted_data = json.dumps({
    'aes_key': encrypted_aes_key,
    'message': encrypted_message
})

# 将加密结果写入文件
with open('encrypted_data.json', 'w') as f:
    f.write(encrypted_data)

print('Encrypted data written to encrypted_data.json')


