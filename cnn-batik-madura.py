import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Path dataset
train_dir = "B:\Belajar\Analisis Citra\Final Project\TEST"
test_dir = "B:\Belajar\Analisis Citra\Final Project\TRAIN"

# Augmentasi data
datagen = ImageDataGenerator(rescale=1. / 255, rotation_range=20, zoom_range=0.2,
                             width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True)

train_data = datagen.flow_from_directory(train_dir, target_size=(128, 128), batch_size=32, class_mode='binary')
test_data = datagen.flow_from_directory(test_dir, target_size=(128, 128), batch_size=32, class_mode='binary')

# Model CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
 
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Output untuk klasifikasi biner
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training model
history = model.fit(train_data, epochs=20, validation_data=test_data)

# Simpan model
model.save("model_batik.h5")
print("Model telah disimpan sebagai 'model_batik.h5'")
