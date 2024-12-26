import librosa
import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt

# song = AudioSegment.from_mp3("F:\\CTF\\CTFQD\\games\\2024BaseCTF\\misc\\wu_zhu_x_zhi_er.mp3")
y, sr = librosa.load("F:\\CTF\\CTFQD\\games\\2024BaseCTF\\misc\\wu_zhu_x_zhi_er.mp3",mono=False)
left_channel = y[0]
right_channel = y[1]
# 确保y是二维数组
if y.ndim == 1:
    print("Warning: Audio data is mono, not stereo")
    left_channel = y
    right_channel = y
else:
    left_channel = y[0]
    right_channel = y[1]
# # 假设left_channel和right_channel是已经加载或处理过的左右声道的numpy数组
# # 这里只是示例，你需要替换为你的音频处理代码
# left_channel = np.random.random(1000)  # 示例左声道数据
# right_channel = np.random.random(1000)  # 示例右声道数据

# FFT变换以计算频率内容
N = len(left_channel)
frequencies = np.fft.fftfreq(N)
left_fft = np.fft.fft(left_channel)
right_fft = np.fft.fft(right_channel)

# 计算双边频谱图（假设是对称的）
left_psd = np.abs(left_fft) ** 2
right_psd = np.abs(right_fft) ** 2
# 计算左右声道的频谱密度（PSD）差异
psd_difference = left_psd - right_psd

# 打印PSD差异
s = ''
print(psd_difference)
for i in psd_difference:
    i = int(i)%127
    s += chr(i)

print(s)