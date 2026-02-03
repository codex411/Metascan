# Metascan

> A modern OSINT tool for comprehensive metadata analysis and reporting

[![Python Version](https://img.shields.io/badge/python-3.5%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-GPLv3-green.svg)](LICENSE)

Metascan is a powerful Python-based tool designed for extracting, analyzing, and visualizing metadata from a wide variety of file types. It leverages ExifTool to extract comprehensive metadata and generates detailed HTML reports with statistics, filtered views, and raw data analysis.

## Features

- **Multi-format Support**: Analyzes metadata from 20+ file types including images, documents, audio, video, and executables
- **Intelligent Filtering**: Automatically filters metadata to highlight the most relevant and important tags
- **Comprehensive Reports**: Generates interactive HTML reports with:
  - File type statistics
  - Geolocation data extraction
  - Software and device identification
  - Author and creator information
  - Custom tag filtering
  - Raw and hexadecimal metadata views
- **Batch Processing**: Analyze multiple files simultaneously
- **Organized Output**: Automatically organizes results by file type and project

## Supported File Types

| Category | Formats |
|----------|---------|
| **Images** | JPEG, PNG, GIF, SVG |
| **Documents** | PDF, DOCX, DOC, XLSX, XLS, PPTX, PPT, ODT, ODS, ODP |
| **Audio** | MP3, WAV |
| **Video** | MP4, MKV |
| **Archives** | ZIP |
| **Executables** | EXE, DLL |
| **Web** | HTML |
| **Other** | TORRENT |

## Requirements

### System Requirements

- Python 3.5 or higher
- Unix-based operating system (Linux, macOS)
- ExifTool (see installation instructions below)

### Python Dependencies

All Python dependencies are listed in `requirements.txt` and can be installed with:

```bash
pip3 install -r requirements.txt
```

**Note**: ExifTool must be installed before installing Python dependencies, as `pyexifinfo` requires it.

## Installation

### Step 1: Install ExifTool

**Debian/Ubuntu:**
```bash
sudo apt install libimage-exiftool-perl
```

**RHEL/CentOS:**
```bash
sudo yum install perl-Image-ExifTool
```

**Arch Linux:**
```bash
sudo pacman -S perl-image-exiftool
```

**macOS:**
```bash
brew install exiftool
```

### Step 2: Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### Step 3: Verify Installation

```bash
python3 metascan.py
```

## Usage

### Quick Start

1. **Place files to analyze** in the `media/` directory
2. **Run Metascan:**
   ```bash
   python3 metascan.py
   ```
3. **Follow the interactive prompts** to:
   - Set up the analysis environment
   - Name your project (or use auto-generated name)
   - Process metadata extraction
   - Generate reports
4. **View results** in the `User_Projects/` directory:
   - Navigate to your project folder
   - Open `index.html` in a web browser

### Project Workflow

Metascan follows a structured 5-step process:

1. **Condition Checking**: Verifies environment and prepares directories
2. **Project Creation**: Creates a named project directory for your analysis
3. **Metadata Extraction**: Runs ExifTool to extract metadata in JSON, HTML, and hex formats
4. **Filtering**: Sorts and filters metadata by file type and importance
5. **Report Generation**: Creates comprehensive HTML reports with statistics and visualizations

## Project Structure

```
metascan/
├── metascan.py          # Main application entry point
├── definitions.py       # Root directory definitions
├── fileinteractions.py  # File operations and directory management
├── exiftool.py          # ExifTool integration and processing
├── filter.py            # Metadata filtering logic
├── markups.py           # HTML report generation
├── requirements.txt     # Python dependencies
├── media/               # Place files to analyze here
├── Template_Data/       # HTML templates and assets
├── User_Projects/       # Generated reports and analysis results
└── exifdata/            # Temporary metadata storage (auto-generated)
```

## Report Features

### Statistics Dashboard
- File type distribution
- Largest files analysis
- Raw vs. filtered metadata comparison
- Custom tag analysis

### Filtered Metadata View
- Curated metadata showing only important tags
- Organized by file type
- Easy-to-read format

### Raw Metadata View
- Complete metadata extraction
- Full ExifTool output
- Comprehensive tag listing

### Hexadecimal View
- Binary data analysis
- Hex dump visualization
- Deep file structure inspection

## Customization

### Adding Custom Tags

To add custom metadata tags for analysis:

1. Run ExifTool manually to identify tags:
   ```bash
   exiftool -j -G <filename>
   ```
2. Edit `markups.py` and locate the `customtags` tuple
3. Add your tags in the format: `"Tag:Name", "Another:Tag"`
4. Re-run Metascan to see custom tags in reports

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **ExifTool**: [https://www.sno.phy.queensu.ca/~phil/exiftool/](https://www.sno.phy.queensu.ca/~phil/exiftool/)
- **Python Libraries**:
  - [progress](https://pypi.org/project/progress/)
  - [dominate](https://pypi.org/project/dominate/)
  - [colorama](https://pypi.org/project/colorama/)
  - [pyexifinfo](https://pypi.org/project/pyexifinfo/)

## Authors

- **Chris Morris**
- **Collin Mockbee**

---

**Note**: This tool is designed for legitimate security research, digital forensics, and OSINT purposes. Always ensure you have proper authorization before analyzing files.
