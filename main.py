# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import caesar
import fence

def try_caesar(str):

    for i in range(1,25):
        print(i)
        strr = caesar.caesar_decode(str,i)
        print(strr)

def try_fence(str):

    for i in range(2,int(len(str))-1):
        print(i)
        strr = fence.fence_cipher_decrypt(str,i)
        print(strr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # str = "oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}"
    # str = "ccehgyaefnpeoobe{lcirg}epriec_ora_g"
    # try_caesar(str)
    str = "ccehgyaefnpeoobe{lcirg}epriec_ora_g"
    try_fence(str)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
