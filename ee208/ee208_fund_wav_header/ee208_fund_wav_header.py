from io import BufferedReader
def extract_wav_header(f: BufferedReader):
    prop = {}

    file_size = len(f.read())
    f.seek(0)
    prop['file_size'] = file_size

    f.seek(20)
    wave_marker = f.read(2)
    wave_marker = int.from_bytes(wave_marker, byteorder='little')
    prop['fmt'] = wave_marker

    num_channels = f.read(2)
    num_channels = int.from_bytes(num_channels, byteorder='little')
    prop['channels'] = num_channels

    sample_rate = f.read(4)
    sample_rate = int.from_bytes(sample_rate, byteorder='little')
    prop['sample_rate'] = sample_rate

    byte_rate = f.read(4)
    byte_rate = int.from_bytes(byte_rate, byteorder='little')
    bit_rate = byte_rate *8
    prop['bit_rate'] = bit_rate


    block_align = f.read(2)
    block_align = int.from_bytes(block_align, byteorder='little')
    prop['block_align'] = block_align

    bit_per_sample = f.read(2) 
    bit_per_sample = int.from_bytes(bit_per_sample, byteorder='little')
    prop['bit_per_sample'] = bit_per_sample

    f.seek(40)
    chunk_2_size = f.read(4)
    chunk_2_size = int.from_bytes(chunk_2_size, byteorder='little')
    prop['data_size'] = chunk_2_size
    
    duration = chunk_2_size / byte_rate
    prop['duration'] = duration
    return prop
if __name__ == "__main__":
    filename = "example.wav"
    with open(filename, "rb") as f:
        audio_prop = extract_wav_header(f)
    print("=" * 50)
    print("Audio Format:", "PCM" if audio_prop["fmt"] == 1 else "Other")
    print("File size:", audio_prop["file_size"])
    print("Channels:", audio_prop["channels"])
    print("Sample Rate:", audio_prop["sample_rate"])
    print("Bit rate:", audio_prop["bit_rate"])
    print("Block align:", audio_prop["block_align"])
    print("Bit per sample:", audio_prop["bit_per_sample"])
    print("Data Size:", audio_prop["data_size"])
    print("Duration(s):", audio_prop["duration"])
    print("=" * 50)