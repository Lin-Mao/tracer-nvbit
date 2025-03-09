import torch
import pytracer

def layer1():
    zeros = torch.zeros(10, 10, device="cuda")
    ones = torch.ones(10, 10, device="cuda")
    return zeros + ones

def layer2():
    ones = torch.ones(5, 10, device="cuda")
    zeros = torch.zeros(5, 10, device="cuda")
    return zeros + ones


def main():
    layer1()
    pytracer.start()
    layer2()
    pytracer.stop()

if __name__ == "__main__":
    main()
