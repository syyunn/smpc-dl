import torch

bob_data = torch.tensor([[0, 0], [0, 1]], requires_grad=True)
bob_target = torch.tensor([[0], [0]], requires_grad=True)

alice_data = torch.tensor([[1, 0], [1, 1.]], requires_grad=True)
alice_target = torch.tensor([[1], [1]], requires_grad=True)

