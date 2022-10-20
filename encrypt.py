text = {} #Give your dictionary of websites and respective passwords
# translated = ('')
# for j in message:
alphabets = 'abcdefghijklmnopqrstuvwxyz'
def encrypt_caesar(num, text):
 results = ' '
 for k in text.lower():
  try:
    i = (alphabets.index(k) + num) % 26
    results += alphabets[i]
  except ValueError:
   results+= k
 return results.lower()
num = 17
for key in text:
   ciphertext = encrypt_caesar(num, text[key])
   print(key,ciphertext)
