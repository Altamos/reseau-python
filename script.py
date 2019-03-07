import sys

def convert_to_binary(dec):
  if dec == 0:
      bin = "0"
  else:
      bin = ""
      while dec!=0:
          bin = "01"[dec&1] + bin
          dec = dec >> 1
  return bin.zfill(8)

def get_mask(cidr):
  mask = [0, 0, 0, 0]
  for i in range(cidr):
    mask[i//8] = mask[i//8] + (1 << (7 - i % 8))
  return mask

def split_address(adr):
  adr = adr.split("/")
  nbr = adr[0].split(".")
  cidr = adr[1]
  if len(nbr) != 4 and len(cidr) != 4:
    sys.exit("Format d'addresse incorrect !!")
  return nbr, cidr

def logical_and(ip, mask):
  res_final = ""
  for i in range(len(ip)):
    if ip[i] == '1' and mask[i] == '1':
      res_final = res_final + "1"
    else:
      res_final = res_final + "0"
  return res_final

add_ip = input("Votre addresse: ")
res_ip = ""
res_mask = ""

(ip, cidr) = split_address(add_ip)
mask = get_mask(int(cidr))

n = 0
while len(mask) > n:
  nbr_mask = mask[n]
  nbr_ip = ip[n]
  res_mask = res_mask + (convert_to_binary(int(nbr_mask)))
  res_ip = res_ip + (convert_to_binary(int(nbr_ip)))
  n += 1

print (logical_and(res_ip, res_mask))

