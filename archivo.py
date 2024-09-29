import zipfile
import os
from PIL import Image
from rembg import remove

# Ruta del archivo ZIP de entrada y salida
zip_file_path = 'C:/Users/Tavol/Downloads/imagenes.zip'
extract_path = 'C:/Users/Tavol/Downloads/extracted_images/'
output_zip_path = 'C:/Users/Tavol/Downloads/processed_images.zip'

# Crear un directorio temporal para extraer las imágenes
os.makedirs(extract_path, exist_ok=True)

# Extraer el archivo ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Función para remover el fondo utilizando rembg
def remove_background(image_path):
    with open(image_path, 'rb') as img_file:
        input_img = img_file.read()
        output_img = remove(input_img)  # Remover el fondo
        
    return output_img

# Procesar todas las imágenes: remover el fondo y guardarlas
processed_images_paths = []
for root, dirs, files in os.walk(extract_path):
    for file in files:
        if file.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(root, file)
            
            # Eliminar el fondo de la imagen
            output_img_data = remove_background(img_path)
            
            # Guardar la imagen procesada
            output_img_path = os.path.join(root, f"processed_{file}")
            with open(output_img_path, 'wb') as f:
                f.write(output_img_data)
            
            processed_images_paths.append(output_img_path)

# Crear un nuevo archivo ZIP con las imágenes procesadas
with zipfile.ZipFile(output_zip_path, 'w') as zipf:
    for file in processed_images_paths:
        zipf.write(file, os.path.basename(file))

print(f"Imágenes procesadas y guardadas en: {output_zip_path}")
