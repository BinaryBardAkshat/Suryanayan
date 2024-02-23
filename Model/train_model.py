import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def load_data(Images):
    images = []
    labels = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            img_path = os.path.join(folder_path, filename)
            label = filename.split(".")[0]  
            labels.append(label)
            img = cv2.imread(img_path)
            images.append(img)

    return images, labels


folder_path = "Images"
images, labels = load_data(folder_path)

# Convert images and labels to numpy arrays
images = np.array(images)
labels = np.array(labels)


images = images.reshape(images.shape[0], -1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Train Support Vector Machine (SVM) classifier
classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

