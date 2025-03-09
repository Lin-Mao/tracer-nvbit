import torch

def layer1():
    zeros = torch.zeros(10, 10, device="cuda")
    ones = torch.ones(10, 10, device="cuda")
    return zeros + ones

def layer2():
    zeros = torch.zeros(5, 10, device="cuda")
    ones = torch.ones(5, 10, device="cuda")
    return zeros + ones


def main():
    layer1()
    layer2()

if __name__ == "__main__":
    main()
