
def decryption():
    """
    This function takes in two file. Encrypted file and
    it's key to decode it. I appended both contents of the
    file into lists and used the list method(index) for a place
    in the encrypted file from the key to decode the file.
    :return:
    """
    file = open("encrypted file.txt","r")
    encrypted_list = [info.strip("\n") for info in file]
    index = open("index.txt","r")
    key_list = list(int(index_list.strip("\n")) for  index_list in index)
    i = 1
    decrypted_list = []
    while i <= len(key_list):
        place_holder = key_list.index(i) # 7
        decrypted_list.append(encrypted_list[place_holder])
        i+=1
    decrypted = open("decrypter.txt","a")
    for j in decrypted_list:
        decrypted.write(j+"\n")
        file.close
def main():
    decryption()

main()