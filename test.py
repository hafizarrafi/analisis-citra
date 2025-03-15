import tensorflow as tf
import numpy as np
import cv2
import sys

# Muat model yang telah dilatih
model = tf.keras.models.load_model("model_batik.h5")


# Fungsi untuk memprediksi gambar
def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))  # Resize sesuai input model
    img = img / 255.0  # Normalisasi
    img = np.expand_dims(img, axis=0)  # Tambahkan dimensi batch

    prediction = model.predict(img)[0][0]
    label = "Batik Madura" if prediction < 0.5 else "Bukan Batik Madura"

    print(f"Hasil Prediksi: {label} (Skor: {prediction:.4f})")


# Contoh penggunaan
if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        predict_image(image_path)
    else:
        print("Gunakan: python predict.py <path_gambar>")
