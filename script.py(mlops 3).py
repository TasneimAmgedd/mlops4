import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

import mlflow
import mlflow.pytorch


# Hyperparameters


learning_rate = 0.001
epochs = 5
batch_size = 128



# MLflow Experiment


mlflow.set_experiment("mlops3")


# Dataset

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True
)

# Model

class SimpleNN(nn.Module):

    def __init__(self):
        super(SimpleNN, self).__init__()

        self.flatten = nn.Flatten()

        self.fc1 = nn.Linear(28*28, 128)
        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):

        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x


model = SimpleNN()

# Loss & Optimizer

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=learning_rate
)

# MLflow Run

with mlflow.start_run():

    # Tags 
    mlflow.set_tag("student_id", "202201968")

    # Parameters 
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("epochs", epochs)
    mlflow.log_param("batch_size", batch_size)

    # Training Loop

    for epoch in range(epochs):

        total_loss = 0
        correct = 0
        total = 0

        for images, labels in train_loader:

            optimizer.zero_grad()

            outputs = model(images)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)

            total += labels.size(0)

            correct += (predicted == labels).sum().item()

        epoch_loss = total_loss / len(train_loader)
        accuracy = 100 * correct / total

        print(f"Epoch {epoch+1}/{epochs} | Loss: {epoch_loss:.4f} | Accuracy: {accuracy:.2f}%")

        # MLflow Metrics
        mlflow.log_metric("loss", epoch_loss, step=epoch)
        mlflow.log_metric("accuracy", accuracy, step=epoch)


    mlflow.pytorch.log_model(model, "model")

print("Training complete.")