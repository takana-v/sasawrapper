import argparse

import sasawrapper


def speak_wrapper(args: argparse.Namespace):
    emotion = {}
    for emotion_list in args.emotion:
        emotion[emotion_list[0]] = int(emotion_list[1])
    sasawrapper.speak(
        text=args.text,
        volume=args.volume,
        speed=args.speed,
        tone=args.tone,
        tone_scale=args.tone_scale,
        alpha=args.alpha,
        cast=args.cast,
        emotion=emotion,
        block=True,
    )


def output_to_wav_wrapper(args: argparse.Namespace):
    emotion = {}
    for emotion_list in args.emotion:
        emotion[emotion_list[0]] = int(emotion_list[1])
    res = sasawrapper.output_to_wav(
        text=args.text,
        path=args.path,
        volume=args.volume,
        speed=args.speed,
        tone=args.tone,
        tone_scale=args.tone_scale,
        alpha=args.alpha,
        cast=args.cast,
        emotion=emotion,
    )
    if not res:
        raise RuntimeError("出力に失敗しました。")


def get_text_duration_wrapper(args: argparse.Namespace) -> float:
    emotion = {}
    for emotion_list in args.emotion:
        emotion[emotion_list[0]] = int(emotion_list[1])
    print(
        sasawrapper.get_text_duration(
            text=args.text,
            volume=args.volume,
            speed=args.speed,
            tone=args.tone,
            tone_scale=args.tone_scale,
            alpha=args.alpha,
            cast=args.cast,
            emotion=emotion,
        )
    )


def start_cevioai_wrapper(args: argparse.Namespace):
    res = sasawrapper.start_cevioai(not args.nonblock)
    if not res:
        raise RuntimeError("起動に失敗しました。")


def close_cevioai_wrapper(args: argparse.Namespace):
    sasawrapper.close_cevioai()


def cast_info_wrapper(args: argparse.Namespace):
    print(sasawrapper.get_cast_info())


def cevioai_version_wrapper(args: argparse.Namespace):
    print(sasawrapper.get_cevioai_version())


def interface_version_wrapper(args: argparse.Namespace):
    print(sasawrapper.get_interface_version())


def self_version(args: argparse.Namespace):
    print(sasawrapper.__version__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    parser_speak = subparser.add_parser("speak")
    parser_speak.add_argument("text", type=str, help="読み上げるセリフ")
    parser_speak.add_argument("--volume", type=int, help="音の大きさ（0～100）", default=50)
    parser_speak.add_argument("--speed", type=int, help="音の高さ（0～100）", default=50)
    parser_speak.add_argument("--tone", type=int, help="音の高さ（0～100）", default=50)
    parser_speak.add_argument("--tone_scale", type=int, help="抑揚（0～100）", default=50)
    parser_speak.add_argument("--alpha", type=int, help="声質（0～100）", default=50)
    parser_speak.add_argument("--cast", type=str, help="読み上げるキャスト", default=None)
    parser_speak.add_argument(
        "--emotion",
        type=str,
        help="感情名、感情の値",
        default=[],
        nargs=2,
        action="append",
        metavar=("EMOTION", "EMOTION_VALUE"),
    )
    parser_speak.set_defaults(func=speak_wrapper)

    parser_output_to_wav = subparser.add_parser("output_to_wav")
    parser_output_to_wav.add_argument("text", type=str, help="読み上げるセリフ")
    parser_output_to_wav.add_argument("path", type=str, help="WAVファイルの保存先のパス")
    parser_output_to_wav.add_argument(
        "--volume", type=int, help="音の大きさ（0～100）", default=50
    )
    parser_output_to_wav.add_argument(
        "--speed", type=int, help="音の高さ（0～100）", default=50
    )
    parser_output_to_wav.add_argument(
        "--tone", type=int, help="音の高さ（0～100）", default=50
    )
    parser_output_to_wav.add_argument(
        "--tone_scale", type=int, help="抑揚（0～100）", default=50
    )
    parser_output_to_wav.add_argument("--alpha", type=int, help="声質（0～100）", default=50)
    parser_output_to_wav.add_argument(
        "--cast", type=str, help="読み上げるキャスト", default=None
    )
    parser_output_to_wav.add_argument(
        "--emotion",
        type=str,
        help="感情名、感情の値",
        default=[],
        nargs=2,
        action="append",
        metavar=("EMOTION", "EMOTION_VALUE"),
    )
    parser_output_to_wav.set_defaults(func=output_to_wav_wrapper)

    parser_text_duration = subparser.add_parser("text_duration")
    parser_text_duration.add_argument("text", type=str, help="読み上げるセリフ")
    parser_text_duration.add_argument(
        "--volume", type=int, help="音の大きさ（0～100）", default=50
    )
    parser_text_duration.add_argument(
        "--speed", type=int, help="音の高さ（0～100）", default=50
    )
    parser_text_duration.add_argument(
        "--tone", type=int, help="音の高さ（0～100）", default=50
    )
    parser_text_duration.add_argument(
        "--tone_scale", type=int, help="抑揚（0～100）", default=50
    )
    parser_text_duration.add_argument("--alpha", type=int, help="声質（0～100）", default=50)
    parser_text_duration.add_argument(
        "--cast", type=str, help="読み上げるキャスト", default=None
    )
    parser_text_duration.add_argument(
        "--emotion",
        type=str,
        help="感情名、感情の値",
        default=[],
        nargs=2,
        action="append",
        metavar=("EMOTION", "EMOTION_VALUE"),
    )
    parser_text_duration.set_defaults(func=get_text_duration_wrapper)

    parser_start_cevioai = subparser.add_parser("start_cevioai")
    parser_start_cevioai.add_argument(
        "--nonblock", action="store_true", help="即座に制御を返す"
    )
    parser_start_cevioai.set_defaults(func=start_cevioai_wrapper)

    parser_close_cevioai = subparser.add_parser("close_cevioai")
    parser_close_cevioai.set_defaults(func=close_cevioai_wrapper)

    parser_cast_info = subparser.add_parser("cast_info")
    parser_cast_info.set_defaults(func=cast_info_wrapper)

    parser_version = subparser.add_parser("version")
    parser_version.set_defaults(func=self_version)

    parser_cevioai_version = subparser.add_parser("cevioai_version")
    parser_cevioai_version.set_defaults(func=cevioai_version_wrapper)

    parser_interface_version = subparser.add_parser("interface_version")
    parser_interface_version.set_defaults(func=interface_version_wrapper)

    args = parser.parse_args()
    args.func(args)
