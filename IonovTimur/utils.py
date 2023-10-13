import torch
import time
import torch.quantization
from torch import profiler
from torch.profiler import profile, record_function, ProfilerActivity

torch.seed = 42

def get_model_size(model: torch.nn.Module) -> float:
    """return model size im mb"""
    param_size = 0
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()
    buffer_size = 0
    for buffer in model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()

    return (param_size + buffer_size) / 1024**2


def profile_model(model, input_example: torch.Tensor = torch.randn(1, 3, 224, 224)):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    input_example = input_example.to(device)

    # cold run
    for _ in range(3):
        model(input_example)

    with profile(activities=[ProfilerActivity.CPU], profile_memory=True, with_flops=True) as prof:
        with record_function("model_inference"):
            with torch.inference_mode():
                model(input_example)

    profiling_info = prof.key_averages().table(sort_by="cpu_time_total", row_limit=1)
    return profiling_info