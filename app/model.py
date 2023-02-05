from torch.cuda import is_available
from transformers import pipeline

if not is_available():
    raise RuntimeError("CUDA Is Unavailable")


class Model:
    def __init__(self, engine="t5-base"):
        self.model = pipeline("summarization", model=engine)
        pass

    def __call__(self, text):
        return self.model(text)[0]["summary_text"]
