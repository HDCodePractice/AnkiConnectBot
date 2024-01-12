import edge_tts


async def generation_audio_file(
        text: str,
        output_file: str,
        voice: str = "Microsoft Server Speech Text to Speech Voice (en-US, AriaNeural)",
        rate: str = "+0%",
        volume: str = "+0%"):
    commuicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume)
    await commuicate.save(output_file)
