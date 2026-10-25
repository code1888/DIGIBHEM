# Pixel Manipulation for Image Encryption

A simple Python project that encrypts and decrypts images by modifying each RGB pixel value using a numeric key.

## Overview

This project uses a basic pixel-level transformation:

- Encryption: adds the key to each red, green, and blue channel
- Decryption: subtracts the key from each red, green, and blue channel
- All values are wrapped to the 0–255 range using modulo 256

## Requirements

- Python 3.8+
- Pillow (`PIL`)

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install Pillow
```

## Run the Project

```bash
python image_encryption.py
```

The script will prompt you to choose:

1. Encrypt Image
2. Decrypt Image

Then it will ask for:

- input image path
- encryption key (1 to 255)
- output image path

## Example

```bash
python image_encryption.py
```

Example input:

- Choice: `1`
- Image path: `input.png`
- Key: `42`
- Output path: `encrypted.png`

## Notes

- The key must be between 1 and 255.
- This is a lightweight educational encryption method, not a secure cryptographic algorithm.
- Decryption works only when the same key used during encryption is provided.

## Files

- `image_encryption.py` – main encryption/decryption logic
