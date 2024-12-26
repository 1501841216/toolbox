import multiprocessing
import string
import socket
import itertools
import hashlib

# crack proof
dic = string.ascii_letters + string.digits
proof_length = 4




# Define the function to compute the hash and check if it matches the given hash
def compute_hash(args):
    proof,GIVEN_HASH,GIVEN_STRING = args
    # print(proof)
    proof = ''.join(proof)
    hash = hashlib.sha256((proof + GIVEN_STRING).encode('latin-1')).hexdigest()
    if hash == GIVEN_HASH:
        return proof


if __name__ == '__main__':
    # define ip and port
    SERVER_IP = 'crypto0.aliyunctf.com'
    SERVER_PORT = 12346

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect((SERVER_IP, SERVER_PORT))
    recv = s.recv(1024)
    print(recv)
    parts = recv.decode().split(' == ')
    GIVEN_STRING = parts[0].split(' + ')[1][:-1]
    print(GIVEN_STRING)
    GIVEN_HASH = parts[1]
    print(GIVEN_HASH)

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Generate all possible four-character combinations
        proofs = ((proof,GIVEN_HASH,GIVEN_STRING)for proof in itertools.product(dic, repeat=proof_length))
        # Compute the hash for each combination in parallel and check if it matches the given hash
        for result in pool.imap_unordered(compute_hash, proofs):
            if result is not None:
                print(f'The original proof for hash {GIVEN_HASH} is {result}')
                s.send(result.encode() + b'\n')
                recv = s.recv(1024)
                print(recv)