# tracer-nvbit

Layer-wise tracing tool for accel-sim.

# Installation

```shell
cd tracer-nvbit
./install_nvbit.sh
make

# in conda env
python setup.py bdist
pip install .
```

# Usage

The following code collects the trace of only layer2 by placing `pytracer.start()` and `pytracer.stop()` around it. See the full example: https://github.com/Lin-Mao/tracer-nvbit/blob/main/test/test_layer_wise.py.

```python
import pytracer

layer1()

pytracer.start()
layer2()
pytracer.stop()
```


