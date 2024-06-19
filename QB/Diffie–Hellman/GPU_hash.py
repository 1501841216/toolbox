import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
import numpy as np
import hashlib
import multiprocessing
import string
import socket
import itertools
import hashlib

dic = string.ascii_letters + string.digits
proof_length = 4

given_string = '5f4mfVHfUpi34v4W'
given_hash = 'e338c91c35ba6719ef76187fe645cac7d824c9fbc5965f6911695be9caf04ecd'

# Define the CUDA kernel
mod = SourceModule("""
    __global__ void compute_hash(char *proof, char *hash)
    {
        int idx = threadIdx.x + blockIdx.x * blockDim.x;
        // Compute the hash for the given proof
        // This is a placeholder, you need to implement the actual hash computation
        hash[idx] = proof[idx];
    }
""")

# Get the function from the module
compute_hash = mod.get_function("compute_hash")

# Prepare the data
proofs = np.array(list(''.join(proof) for proof in itertools.product(dic, repeat=proof_length)), dtype=np.str_)
hashes = np.empty_like(proofs)

# Copy the data to the GPU
proofs_gpu = drv.mem_alloc(proofs.nbytes)
drv.memcpy_htod(proofs_gpu, proofs)

# Convert the given_string to a character array and copy it to the GPU
given_string_gpu = drv.mem_alloc(len(given_string))
drv.memcpy_htod(given_string_gpu, np.array(list(given_string), dtype=np.str_))

# Call the CUDA kernel
compute_hash(proofs_gpu, given_string_gpu, drv.Out(hashes), block=(256,1,1), grid=(len(proofs)//256,1))

# Check the result
for proof, hash in zip(proofs, hashes):
    if hash == given_hash:
        print(f'The original proof for hashis {proof}')
