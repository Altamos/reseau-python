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

def split(adr):
  adr = adr.split("/")
  nbr = adr[0].split(".")
  cidr = adr[1]
  return nbr, cidr

add_ip = "10.92.10.1/24"
res = ""
res_mask = ""

(ip, cidr) = split(add_ip)
mask = get_mask(int(cidr))
n = 0
while len(mask) > n:
  nbr = mask[n]
  res_mask = res_mask + (convert_to_binary(int(nbr)))
  n += 1

n = 0 
while len(ip) > n:
  nbr = ip[n]
  res = res + (convert_to_binary(int(nbr)))
  n += 1

print (res)
print (res_mask)

