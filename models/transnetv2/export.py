# Reproduces transnetv2-1.onnx: pip install transnetv2-pytorch==1.0.5 torch onnx onnxruntime, then run
# this file. It prints the difference against PyTorch and the sha256 of the export.
# Export TransNetV2 (transnetv2-pytorch weights) to ONNX: uint8 [1,100,27,48,3] -> sigmoid(single-frame) [1,100]
import hashlib, os, numpy as np, torch, onnx
import transnetv2_pytorch as t
from transnetv2_pytorch.transnetv2_pytorch import TransNetV2
w = os.path.join(os.path.dirname(t.__file__), 'transnetv2-pytorch-weights.pth')
m = TransNetV2(); m.load_state_dict(torch.load(w, map_location='cpu')); m.eval()
class Head(torch.nn.Module):
    def __init__(s, m): super().__init__(); s.m = m
    def forward(s, frames):
        one_hot = s.m(frames)
        one_hot = one_hot[0] if isinstance(one_hot, tuple) else one_hot
        return torch.sigmoid(one_hot)[:, :, 0]
h = Head(m).eval()
x = torch.randint(0, 255, (1, 100, 27, 48, 3), dtype=torch.uint8)
torch.onnx.export(h, x, 'transnetv2.onnx', input_names=['frames'], output_names=['prob'], opset_version=17, dynamo=False)
onnx.checker.check_model('transnetv2.onnx')
import onnxruntime as ort
ref = h(x).detach().numpy(); got = ort.InferenceSession('transnetv2.onnx').run(None, {'frames': x.numpy()})[0]
print('max diff torch vs onnx', float(np.abs(ref - got).max()), 'size', os.path.getsize('transnetv2.onnx'), 'sha256', hashlib.sha256(open('transnetv2.onnx','rb').read()).hexdigest())
