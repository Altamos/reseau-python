import sys

def convert_to_binary(dec):
    return bin(dec)[2:].zfill(8)

def convert_to_int(bin):
    return int(bin, base=2)

def swap_binary(dec):
    res_final = ""
    for i in range(len(dec)):
        if dec[i] == "1":
            res_final = res_final + "0"
        else:
            res_final = res_final + "1"
    return res_final

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

def logical_and_or(ip, mask, choice):
    res_final = ""
    for i in range(len(ip)):
        if choice == "and":
            if ip[i] == "1" and mask[i] == "1":
                res_final = res_final + "1"
            else:
                res_final = res_final + "0"
        else:
            if ip[i] == "0" and mask[i] == "0":
                res_final = res_final + "0"
            else:
                res_final = res_final + "1"
    return res_final

add_ip = input("Votre addresse: ")
res_ip = ""
res_mask = ""

(ip, cidr) = split_address(add_ip)
mask = get_mask(int(cidr))

n = 0
while len(ip) > n:
    nbr_mask = mask[n]
    nbr_ip = ip[n]
    res_mask = res_mask + (convert_to_binary(int(nbr_mask)))
    res_ip = res_ip + (convert_to_binary(int(nbr_ip)))
    n += 1

bin_reseau = logical_and_or(res_ip, res_mask, "and")
inverse_mask = swap_binary(res_mask)
bin_diff_mask = logical_and_or(bin_reseau, inverse_mask, "or")

tab_reseau = [(bin_reseau[0:8]),(bin_reseau[8:16]),(bin_reseau[16:24]),(bin_reseau[24:32])]
tab_diff = [(bin_diff_mask[0:8]),(bin_diff_mask[8:16]),(bin_diff_mask[16:24]),(bin_diff_mask[24:32])]
ip_reseau = ""
ip_diffusion = ""
tail = 0

while tail < 4:
    tmp_reseau = tab_reseau[tail]
    tmp_diff = tab_diff[tail]
    ip_reseau = ip_reseau + str((convert_to_int(tmp_reseau))) + "."
    ip_diffusion =  ip_diffusion +  str((convert_to_int(tmp_diff))) + "."
    tail +=1

print ("L'addresse reseau est: %s" % ip_reseau)
print ("L'addresse de diffusion est: %s" % ip_diffusion)

