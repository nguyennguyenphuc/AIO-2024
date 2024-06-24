import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum(dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x)
        exp_x = torch.exp(x - x_max)
        return exp_x / exp_x.sum(dim=0)


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])

    softmax = Softmax()
    output = softmax(data)
    expected_output = torch.Tensor([0.0900, 0.2447, 0.6652])
    assert torch.allclose(output, expected_output,
                          atol=1e-4), f"Expected {expected_output}, but got {output}"
    print(f"Softmax output: {output}")

    softmax_stable = SoftmaxStable()
    output_stable = softmax_stable(data)
    assert torch.allclose(output_stable, expected_output,
                          atol=1e-4), f"Expected {expected_output}, but got {output_stable}"
    print(f"Stable Softmax output: {output_stable}")
