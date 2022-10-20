text = {} #Give your dictionary of websites and respective passwords
# translated = ('')
# for j in message:
alphabets = 'abcdefghijklmnopqrstuvwxyz'
# for i in alphabet:
def encrypt(num, text):
 results = ' '
 for k in text.lower():
  try:
    i = (alphabets.index(k) + num) % 26
    results += alphabets[i]
  except ValueError:
   results+= k
 return results.lower()
num = #shift value
for key in text:
   ciphertext = encrypt(num, text[key])
   print(key,ciphertext)
