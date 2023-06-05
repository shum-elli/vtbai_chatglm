import pyaudio
import wave
import subprocess

CHUNK = 1024
wf = wave.open("output/wav/t2~1.wav", 'rb')


p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                output_device_index=9)

data = wf.readframes(CHUNK)

while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()




# import asyncio
# import edge_tts
# from pydub import AudioSegment
# import tempfile
#
# TEXT = "女士们，先生们，华南的朋友们：大家早上好！春天是一年的计划。精心策划并在此时举办了这样一场盛大的活动。旨在新年伊始与华南商圈的朋友们共同期待，把握人力资源的最新发展趋势和方向，从规划和实战两个层面进行深入探讨，为企业发展和实际工作提供最有价值的支持和帮助。"
# VOICE = "zh-CN-YunxiNeural"
# OUTPUT_FILE = "test.mp3"
#
#
# async def _main() -> None:
#     communicate = edge_tts.Communicate(TEXT, VOICE)
#     with open(OUTPUT_FILE, "wb") as file:
#         async for chunk in communicate.stream():
#             if chunk["type"] == "audio":
#                 file.write(chunk["data"])
#
#         # elif chunk["type"] == "WordBoundary":
#         #     submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(_main())
#     finally:
#         loop.close()
#
# # import pyaudio
# #
# # p = pyaudio.PyAudio()
# #
# # print(p)
# #
# # for i in range(p.get_device_count()):
# #
# #     print(p.get_device_info_by_index(i))



