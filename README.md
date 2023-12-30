# HEIC-Conversion-Tool
 TKinter GUI based HEIC to JPG and PNG conversion tool

 ![HEIC-Conversion-Tool-Graphic](https://github.com/Mitchell-Conrad-20/HEIC-Conversion-Tool/assets/10098947/d33f2112-eee7-4fb5-955d-f657a526070c)

## User Guide
1. Run executable or python source file.
2. Click select source folder. Select a folder containing HEIC images.
3. Click select destination folder. Select or create a folder to save converted images in. This folder may be the same as the source.
4. Click convert to JPG or convert to PNG based on which file type you prefer. Note that JPG conversions are generally much faster than PNG conversions.

   Note: File extensions must be ".heic" or ".HEIC". Files with mixed case extensions will be ignored.
   
### Video Guide
[![User Guide Video Tutorial](https://i.ytimg.com/vi/fs0zZ2S1hls/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB1FAvKfY7B5QGpbXFcfPdLlmJu4A)](https://www.youtube.com/watch?v=fs0zZ2S1hls "User Guide Video Tutorial")

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
