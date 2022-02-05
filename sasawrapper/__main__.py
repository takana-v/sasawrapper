import argparse

import sasawrapper


def speak_wrapper(args: argparse.Namespace) -> None:
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


def output_to_wav_wrapper(args: argparse.Namespace) -> None:
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


def text_duration_wrapper(args: argparse.Namespace) -> None:
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


def monophone_label_wrapper(args: argparse.Namespace) -> None:
    emotion = {}
    for emotion_list in args.emotion:
        emotion[emotion_list[0]] = int(emotion_list[1])
    print(
        sasawrapper.get_monophone_label(
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


def start_cevioai_wrapper(args: argparse.Namespace) -> None:
    res = sasawrapper.start_cevioai(not args.nonblock)
    if not res:
        raise RuntimeError("起動に失敗しました。")


def close_cevioai_wrapper(args: argparse.Namespace) -> None:
    sasawrapper.close_cevioai()


def cast_info_wrapper(args: argparse.Namespace) -> None:
    print(sasawrapper.get_cast_info())


def cevioai_version_wrapper(args: argparse.Namespace) -> None:
    print(sasawrapper.get_cevioai_version())


def interface_version_wrapper(args: argparse.Namespace) -> None:
    print(sasawrapper.get_interface_version())


def self_version(args: argparse.Namespace) -> None:
    print(sasawrapper.__version__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="sasawrapper")
    subparser = parser.add_subparsers()

    parser_speak = subparser.add_parser("speak", description="指定したテキストの読み上げを行います。")
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

    parser_output_to_wav = subparser.add_parser(
        "output_to_wav", description="指定したパスにWAVファイルとして保存します。"
    )
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

    parser_text_duration = subparser.add_parser(
        "text_duration", description="指定したテキストの長さを取得します。"
    )
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
    parser_text_duration.set_defaults(func=text_duration_wrapper)

    parser_monophone_label = subparser.add_parser(
        "monophone_label", description="モノフォンラベルを取得します。リップシンク用ファイル（.lab）と同じフォーマットです。"
    )
    parser_monophone_label.add_argument("text", type=str, help="読み上げるセリフ")
    parser_monophone_label.add_argument(
        "--volume", type=int, help="音の大きさ（0～100）", default=50
    )
    parser_monophone_label.add_argument(
        "--speed", type=int, help="音の高さ（0～100）", default=50
    )
    parser_monophone_label.add_argument(
        "--tone", type=int, help="音の高さ（0～100）", default=50
    )
    parser_monophone_label.add_argument(
        "--tone_scale", type=int, help="抑揚（0～100）", default=50
    )
    parser_monophone_label.add_argument(
        "--alpha", type=int, help="声質（0～100）", default=50
    )
    parser_monophone_label.add_argument(
        "--cast", type=str, help="読み上げるキャスト", default=None
    )
    parser_monophone_label.add_argument(
        "--emotion",
        type=str,
        help="感情名、感情の値",
        default=[],
        nargs=2,
        action="append",
        metavar=("EMOTION", "EMOTION_VALUE"),
    )
    parser_monophone_label.set_defaults(func=monophone_label_wrapper)

    parser_start_cevioai = subparser.add_parser(
        "start_cevioai", description="CeVIO AIを起動します。"
    )
    parser_start_cevioai.add_argument(
        "--nonblock", action="store_true", help="即座に制御を返す"
    )
    parser_start_cevioai.set_defaults(func=start_cevioai_wrapper)

    parser_close_cevioai = subparser.add_parser(
        "close_cevioai", description="CeVIO AIに終了を要求します。"
    )
    parser_close_cevioai.set_defaults(func=close_cevioai_wrapper)

    parser_cast_info = subparser.add_parser("cast_info", description="キャストの情報を取得します。")
    parser_cast_info.set_defaults(func=cast_info_wrapper)

    parser_version = subparser.add_parser(
        "version", description="sasawrapperのバージョンを取得します。"
    )
    parser_version.set_defaults(func=self_version)

    parser_cevioai_version = subparser.add_parser(
        "cevioai_version", description="CeVIO AIのバージョンを取得します。"
    )
    parser_cevioai_version.set_defaults(func=cevioai_version_wrapper)

    parser_interface_version = subparser.add_parser(
        "interface_version", description="CeVIO AI 外部連携インターフェイスのバージョンを取得します。"
    )
    parser_interface_version.set_defaults(func=interface_version_wrapper)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception:
        parser.print_help()
