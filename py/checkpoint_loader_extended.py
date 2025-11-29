import os
import sys

THIS_DIR = os.path.dirname(__file__)
if THIS_DIR not in sys.path:
    sys.path.append(THIS_DIR)

from better_combos import CheckpointLoaderSimpleWithImages

class CheckpointLoaderSimpleWithImagesAndName(CheckpointLoaderSimpleWithImages):
    """拡張版: CheckpointLoaderSimpleWithImages + ckpt_name出力"""
    
    RETURN_TYPES = (*CheckpointLoaderSimpleWithImages.RETURN_TYPES, "STRING",)
    RETURN_NAMES = (*CheckpointLoaderSimpleWithImages.RETURN_NAMES, "ckpt_name")

    @classmethod
    def INPUT_TYPES(s):
        return super().INPUT_TYPES()

    def load_checkpoint(self, **kwargs):
        ckpt_name = kwargs.get("ckpt_name", "")
        result = super().load_checkpoint(**kwargs)
        return (*result, ckpt_name)


NODE_CLASS_MAPPINGS = {
    "CheckpointLoader|pysssss|extended": CheckpointLoaderSimpleWithImagesAndName,
    # 上書きして既存フロントエンド処理を利用できるようにする（後勝ちで上書きされる）
    "CheckpointLoader|pysssss": CheckpointLoaderSimpleWithImagesAndName,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CheckpointLoader|pysssss|extended": "Checkpoint Loader Extended 🐍",
    # 元の表示名と同じにしてUIに違和感が出ないようにする
    "CheckpointLoader|pysssss": "Checkpoint Loader 🐍",
}
