import cv2
import os

# Directory containing your high-resolution images
input_dir = './DogCat/data/test/dogs'


# Target size for YOLOv8 (adjust as needed)
target_size = (300, 300)

# Iterate through each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read image
        image_path = os.path.join(input_dir, filename)
        img = cv2.imread(image_path)

        # Resize image
        resized_img = cv2.resize(img, target_size)

        # Save resized image
        output_path = os.path.join(input_dir, filename)
        cv2.imwrite(output_path, resized_img)

        print(f'Resized {filename} to {target_size}')

print("Done processing file")