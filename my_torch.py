import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# Define the CNN architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x))
        return x

net = Net()

# Define a loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# Load the data
transform = transforms.Compose([transforms.Resize((254, 254)),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

banana_dataset = torchvision.datasets.ImageFolder(root='banana_data', transform=transform)
dataloader = torch.utils.data.DataLoader(banana_dataset, batch_size=2, shuffle=True, drop_last=True)

# Train the model
for epoch in range(10):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(dataloader, 0):
        inputs, labels = data
        
        # convert the labels to the correct format
        labels = labels.long() 

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        
        # check the size and shape of the input tensor
        print(f'inputs size: {inputs.size()}')
        print(f'inputs shape: {inputs.shape}')

        # check the size and shape of the labels tensor
        print(f'labels size: {labels.size()}')
        print(f'labels shape: {labels.shape}')

        # check the size and shape of the output tensor
        print(f'outputs size: {outputs.size()}')
        print(f'outputs shape: {outputs.shape}')

        # check the number of elements in the input tensor
        print(f'inputs numel: {inputs.numel()}')

        # check the number of elements in the labels tensor
        print(f'labels numel: {labels.numel()}')

        # check the number of elements in the output tensor
        print(f'outputs numel: {outputs.numel()}')
        
        labels = labels.unsqueeze(1)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
    print('[%d] loss: %.3f' %
          (epoch + 1, running_loss / len(dataloader)))

print('Finished Training')

torch.save({"epoch" : epoch, 
            "model_state_dict" : net.state_dict(),
            "optimizer_state_dict" : optimizer.state_dict()}, 'model/model.pth')
