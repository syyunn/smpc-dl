import torch

import syft as sy
from syft.workers import websocket_client as wsc

from models import Model

import encrypts

hook = sy.TorchHook(torch)


model = Model()

bob_data = torch.tensor([[0., 0.], [0., 1.]], requires_grad=True)
bob_target = torch.tensor([[0.], [0.]], requires_grad=True)

kwargs_websocket = {"hook": hook, "verbose": True, "host": "127.0.0.1"}

alice = wsc.WebsocketClientWorker(id="alice", port=8777,
                                    **kwargs_websocket)
bob = wsc.WebsocketClientWorker(id="bob", port=8778,
                                    **kwargs_websocket)
charlie = wsc.WebsocketClientWorker(id="charlie", port=8779,
                                    **kwargs_websocket)

print(bob._objects)
bob_data.send(bob)
print(bob._objects)

# shares = encrypts.secret_share(bob_data, workers=[bob, alice],
#                                crypto_provider=charlie)
pass
if __name__ == "__main__":
    pass

## MAKE VIRTUAL WORKER AND STORE DATA Then SERVER RUN!
##