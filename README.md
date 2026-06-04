# SVG to PNG Batch Converter

A simple and efficient Python CLI tool to batch convert SVG files into multiple PNG files with custom dimensions and filenames based on a JSON configuration.

## Prerequisites

This script requires Python 3.8+ and the cairosvg library. You can install the dependencies using either uv or pip.

## Option A: Using uv (Recommended)

If you are using the ultra-fast Python package installer uv, you can either run the script instantly without installing anything globally, or install the dependency into your environment.

Run instantly (without installation):

```bash
uv run --with cairosvg svg_converter.py logo.svg
```

Or install to your virtual environment:

```bash
uv pip install cairosvg
```

## Option B: Using standard pip

Alternatively, you can install the required package using standard pip:

```bash
pip install cairosvg
```

Note for Windows users: CairoSVG depends on the Cairo graphics library. If you encounter initialization errors on Windows, the easiest fix is to install it via pipwin:

```bash
pip install pipwin
pipwin install cairosvg
```

## Configuration (config.json)

Define your export profiles in a config.json file placed in the same directory:

```json
{
  "output_packages": {
    "default": [
      { "name": "icon16.png", "width": 16, "height": 16 },
      { "name": "icon32.png", "width": 32, "height": 32 },
      { "name": "icon48.png", "width": 48, "height": 48 },
      { "name": "icon96.png", "width": 96, "height": 96 },
      { "name": "icon128.png", "width": 128, "height": 128 },
      { "name": "icon256.png", "width": 256, "height": 256 },
      { "name": "icon512.png", "width": 512, "height": 512 }
    ],
    "android": [
      { "name": "mdpi.png", "width": 48, "height": 48 },
      { "name": "hdpi.png", "width": 72, "height": 72 },
      { "name": "xhdpi.png", "width": 96, "height": 96 }
    ]
  }
}
```

## Usage Examples

### 1. Basic Conversion

Convert an SVG using the default preset. Outputs will be saved to the ./output folder:

```bash
python svg_converter.py logo.svg
```

### 2. Specify Output Directory

Save the generated PNG files into a specific folder (e.g., ./dist/icons):

```bash
python svg_converter.py logo.svg -o ./dist/icons
```

### 3. Use a Specific Preset

Generate icons using a different preset profile defined in your config (e.g., android):

```bash
python svg_converter.py logo.svg -p android
```

### 4. Custom Configuration File

Use a different JSON configuration file instead of the default config.json:

```bash
python svg_converter.py logo.svg -c sizes-spec.json
```

### 5. Help Menu

To see all available options and argument descriptions, run:

```bash
python svg_converter.py --help
```
