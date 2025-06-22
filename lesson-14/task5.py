from PIL import Image
import numpy as np

def flip_image(img_arr, direction='horizontal'):
    axis = 1 if direction == 'horizontal' else 0
    return np.flip(img_arr, axis=axis)

def add_noise(img_arr, noise_level=50):
    noise = np.random.randint(0, noise_level, img_arr.shape, dtype='uint8')
    noisy_img = img_arr + noise
    return np.clip(noisy_img, 0, 255)

def brighten_channel(img_arr, channel=0, value=40):
    brightened = img_arr.copy()
    brightened[:, :, channel] = np.clip(brightened[:, :, channel] + value, 0, 255)
    return brightened

def apply_mask(img_arr, mask_size=100):
    masked = img_arr.copy()
    h, w = masked.shape[:2]
    cy, cx = h // 2, w // 2
    half = mask_size // 2
    masked[cy - half:cy + half, cx - half:cx + half] = [0, 0, 0]
    return masked

with Image.open('images/birds.jpg') as img:
    img_arr = np.array(img)

    flipped_h = flip_image(img_arr, 'horizontal')
    flipped_v = flip_image(img_arr, 'vertical')
    noisy = add_noise(img_arr)
    bright_red = brighten_channel(img_arr, channel=0, value=40)
    masked = apply_mask(img_arr, mask_size=100)

    # Saving results
    Image.fromarray(flipped_h).save('images/birds_flipped.jpg')
    Image.fromarray(flipped_v).save('images/birds_flipped_vertical.jpg')
    Image.fromarray(noisy.astype('uint8')).save('images/birds_noisy.jpg')
    Image.fromarray(bright_red.astype('uint8')).save('images/birds_red_brightened.jpg')
    Image.fromarray(masked).save('images/birds_masked.jpg')
