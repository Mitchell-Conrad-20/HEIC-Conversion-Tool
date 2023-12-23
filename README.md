# HEIC-Conversion-Tool
 TKinter GUI based HEIC to JPG and PNG conversion tool

## User Guide
1. Run executable or python source file.
2. Click select source folder. Select a folder containing HEIC images.
3. Click select destination folder. Select or create a folder to save converted images in. This folder may be the same as the source.
4. Click convert to JPG or convert to PNG based on which file type you prefer. Note that JPG conversions are generally much faster than PNG conversions.

   Note: File extensions must be ".heic" or ".HEIC". Files with mixed case extensions will be ignored.

## Usage
### Source File
- Python source code is in the src folder.
- Feel free to modify or borrow functionality from the code.
- Requires Python installation and the following dependencies:
   - Pillow
   - pillow_heif
   - tkinter
   - os

### Standalone Executable
- The dist folder contains a Windows 8+ distribution.
- The distribution was made using Pyinstaller.
